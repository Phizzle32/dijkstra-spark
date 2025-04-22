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

## Instructions

### Prerequisites
Before proceeding, ensure your system meets the following requirements:
- Operating System: Ubuntu-based VM
- Dependencies: Apache Spark, OpenJDK, Git
- Setup: Spark Standalone Cluster

### 1. Install dependencies
```
sudo apt update
sudo apt install openjdk-11-jdk -y
sudo apt install git
```
### 2. Download and Configure Apache Spark
```
wget https://archive.apache.org/dist/spark/spark-3.3.0/spark-3.3.0-bin-hadoop3.tgz
tar -xvzf spark-3.3.0-bin-hadoop3.tgz
mv spark-3.3.0-bin-hadoop3 ~/spark
```
### 3. Set Up Environment Variables
```
echo "export SPARK_HOME=~/spark" >> ~/.bashrc
echo "export PATH=$SPARK_HOME/bin:$PATH" >> ~/.bashrc
source ~/.bashrc
```

### 4. Configure Spark
Edit `~/spark/conf/spark-env.sh`
```
SPARK_MASTER_HOST="master-vm-ip"
export SPARK_WORKER_CORES=2
export SPARK_WORKER_MEMORY=4G
```

### 5. Start Spark Cluster
On the Master VM, start the master node:
```
~/spark/sbin/start-master.sh
```
On the Worker VMs, start the worker nodes and link them to the master node:
```
~/spark/sbin/start-worker.sh spark://<master-vm-ip>:7077
```

### 6. Running the Application
Once the cluster is running, deploy the Spark job from the master VM:
```
git clone https://github.com/Phizzle32/dijkstra-spark
cd dijkstra-spark/
spark-submit --master spark://<master-vm-ip>:7077 dijkstra.py
```