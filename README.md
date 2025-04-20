# Dijkstra's Algorithm with Apache Spark
This project demonstrates the implementation of Dijkstra’s shortest path algorithm in a distributed computing environment using Apache Spark.
The main goal is to efficiently compute the shortest paths from a single source node to all other nodes in a large, weighted graph.

## Input Format
The program expects the input graph in edge list format:
```
num_nodes num_edges
u1 v1 weight1
u2 v2 weight2
...
```

## Output Format
The program outputs the shortest distances from a specified source node to all other nodes. Unreachable nodes are labeled as `INF`.
```
Shortest distances from node 0:
Node 0: 0
Node 1: 7
Node 2: 3
Node 3: 10
Node 4: 7
...
```
