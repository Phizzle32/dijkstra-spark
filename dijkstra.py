from pyspark import SparkContext

INF = float('inf')

def parse_edge(line):
    parts = line.strip().split()
    return int(parts[0]), int(parts[1]), int(parts[2])

def dijkstra_rdd(sc: SparkContext, filename, source):
    lines = sc.textFile(filename)
    header = lines.first()
    num_nodes = int(header.split()[0])
    edges = lines.filter(lambda x: x != header).map(parse_edge)

    # adjacency list: (u, [(v, weight)])
    adj = edges.map(lambda x: (x[0], (x[1], x[2]))).groupByKey().mapValues(list).cache()

    # (node, distance)
    distances = sc.parallelize([(i, INF) for i in range(num_nodes)]) \
                  .map(lambda x: (x[0], 0) if x[0] == source else x).cache()
    
    # set the number of partitions equal to the number of cores
    num_partitions = sc.defaultParallelism

    converged = False
    while not converged:
        # (u, (current_distance, [(v1, w1), ...]))
        joined = distances.join(adj)
        # calculate distances for all nodes (non-visted, non-neighboring nodes will be infinity)
        updated = joined.flatMap(lambda x: [(v, x[1][0] + w) for (v, w) in x[1][1]])
        # update distances for visted and neighboring nodes with minimum distance
        new_distances = distances.union(updated).coalesce(num_partitions).reduceByKey(lambda a, b: min(a, b)).cache()

        # Stop when no more updates to distances are made
        converged = new_distances.join(distances).filter(lambda x: x[1][0] != x[1][1]).isEmpty()
        distances = new_distances

    return distances

if __name__ == "__main__":
    sc = SparkContext(appName="DijkstraRDD")
    input_path = "weighted_graph.txt"
    source_node = 0

    result = dijkstra_rdd(sc, input_path, source_node)

    print(f"Shortest distances from node {source_node}:")

    for node, distance in result.collect():
        print(f"Node {node}: {'INF' if distance == INF else distance}")

    sc.stop()