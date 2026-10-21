# ⚙️ Raft Consensus Algorithm — Dockerized Distributed Cluster

A distributed systems project that demonstrates **Raft-based leader election and cluster coordination** using Python, Docker, and Docker Compose. The project launches five independent nodes that register with a shared cluster and periodically report the elected leader and their own role.

## 📌 Project Overview

Distributed systems consist of multiple independent nodes that communicate over a network. To coordinate their operations, nodes need a mechanism to agree on important cluster state, even when individual nodes have different roles or experience delays.

This project demonstrates a five-node cluster using the Raft consensus implementation provided by the `raftos` Python library.

Each node runs in its own Docker container. The containers communicate over a dedicated Docker bridge network, register with the cluster, and periodically check the current leader.

The main objective is to explore distributed node coordination, leader election, containerized services, and the practical setup of a multi-node environment.

## 🎯 Objectives

- Understand the role of consensus in distributed systems.
- Demonstrate a multi-node cluster using the Raft protocol implementation.
- Observe leader and follower roles across five nodes.
- Containerize individual nodes using Docker.
- Orchestrate multiple services using Docker Compose.
- Configure network communication between distributed containers.
- Observe cluster status through periodic console logs.

## ✨ Key Features

### 1. Five-Node Distributed Cluster

The cluster consists of five independently running nodes:

- Node 1
- Node 2
- Node 3
- Node 4
- Node 5

Each node runs in its own container, allowing the services to operate independently while participating in the same cluster.

### 2. Raft-Based Leader Election

The project uses the `raftos` library to register nodes and query the cluster's current leader.

Each node periodically checks the leader and reports one of the following states:

- **Leader:** The node identifies itself as the current leader.
- **Follower:** The node reports the current leader.
- **Waiting:** No leader has been reported yet.

This provides a simple way to observe leader election and cluster coordination in action.

### 3. Docker Containerization

The `Dockerfile` defines the environment required to run a node, including Python and the Raft library.

Each container executes `node.py` with a node ID supplied through its startup command.

### 4. Docker Compose Orchestration

The `docker-compose.yml` file defines all five services and starts them together.

It also configures a dedicated bridge network with static IP addresses for the containers.

### 5. Independent Node Configuration

A shared Python script is reused for every node. The node ID determines its log path and identifies its entry in the cluster configuration.

This avoids maintaining five separate implementations of the same node logic.

### 6. Periodic Cluster Monitoring

Each node prints its observed leader status every three seconds, making it easier to inspect the cluster's behavior through Docker logs.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Node implementation and asynchronous execution |
| `raftos` | Raft-based cluster coordination |
| Docker | Containerization of individual nodes |
| Docker Compose | Multi-container orchestration |
| Docker Bridge Network | Communication between cluster containers |
| asyncio | Asynchronous node execution |

## 🏗️ System Architecture

The system consists of five Docker containers connected through a dedicated bridge network.

```text
                  Docker Compose
                        |
              Dedicated Bridge Network
                        |
        +---------------+---------------+
        |               |               |
     +------+        +------+        +------+
     |Node 1|        |Node 2|        |Node 3|
     +------+        +------+        +------+
        |               |               |
        +---------------+---------------+
                        |
                 +------+------+
                 |             |
              +------+      +------+
              |Node 4|      |Node 5|
              +------+      +------+

        Raft-based cluster coordination
        Leader / Follower status logging
```

Each node registers its address with the cluster using the shared cluster configuration. The Raft library handles the underlying protocol behavior, while the Python application periodically reports the observed leader.

## 📂 Project Structure

```text
raft_docker_lab/
├── node.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .gitignore
└── README.md
```

### File Descriptions

- **`node.py`** — Reads the node ID, configures Raft, registers the node, and periodically prints leader status.
- **`Dockerfile`** — Builds the node image with Python and installs the `raftos` dependency.
- **`docker-compose.yml`** — Defines five node services and their network configuration.
- **`requirements.txt`** — Lists the project's Python dependencies.
- **`.gitignore`** — Excludes generated logs, Python caches, virtual environments, and other local artifacts.
- **`README.md`** — Documents the architecture, setup, execution, and project scope.

## ⚙️ Prerequisites

Install the following tools:

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) or Docker Engine
- [Docker Compose](https://docs.docker.com/compose/)
- Git, if cloning the repository
- A terminal such as PowerShell, Bash, or the VS Code terminal

Ensure Docker is running before starting the cluster.

## 🚀 Getting Started

### 1. Clone the repository

Replace the example URL with your actual GitHub repository URL.

```bash
git clone https://github.com/ChiragGD/raft-docker-lab.git
cd raft-docker-lab
```

### 2. Build the Docker images

```bash
docker compose build
```

This builds the image defined in the `Dockerfile`. The image installs the required Python environment and the Raft library.

### 3. Start the five-node cluster

```bash
docker compose up
```

To start the services in the background:

```bash
docker compose up -d
```

Docker Compose starts all five containers using their respective node IDs.

### 4. View the logs

To inspect logs from all services:

```bash
docker compose logs -f
```

To inspect one node:

```bash
docker compose logs -f node1
```

The output should show node startup, registration messages, and periodic leader-status reports.

### 5. Check running containers

```bash
docker compose ps
```

This lists the containers and their current status.

### 6. Stop the cluster

```bash
docker compose down
```

This stops and removes the containers and the Compose-managed network.

## 🧠 How It Works

1. **Container startup:** Docker Compose launches five instances of the node service.
2. **Node identification:** Each instance receives its node ID as a command-line argument.
3. **Raft configuration:** The application configures the Raft library and its node-specific log path.
4. **Cluster registration:** Each node registers its configured address and the complete list of cluster addresses.
5. **Leader observation:** Each node periodically queries the library for the current leader.
6. **Status reporting:** The application prints whether it observes itself as leader, another node as leader, or no leader.
7. **Continuous operation:** The asynchronous loop continues until the process is stopped.

## 📚 Concepts Demonstrated

### Distributed Systems

A distributed system consists of independent processes that communicate over a network to coordinate their behavior.

### Consensus

Consensus protocols help distributed nodes coordinate decisions and maintain consistent cluster state. Raft is designed around leader election, replicated logs, and safety properties under specified failure assumptions.

### Leader and Follower Roles

Raft uses a leader to coordinate certain operations, while followers respond to protocol messages and can participate in elections. This project exposes the observed leader role through console output.

### Containerization

Docker packages the node runtime and its dependencies into a repeatable execution environment.

### Service Orchestration

Docker Compose defines the five services, their startup commands, and their shared network.

## ⚠️ Project Scope and Limitations

This implementation is a **cluster coordination and leader-observation demonstration**, not a complete production-grade distributed database.

- It relies on the behavior implemented by the `raftos` library.
- It does not implement a separate application-level replicated key-value store.
- It does not currently demonstrate client requests, replicated application data, or committed-log consistency.
- Leader-status output alone does not prove fault tolerance or consensus safety.
- Network partitions, node failures, recovery, and split-vote scenarios require additional testing.
- The project uses an older Python base image and dependency setup; updating and validating the runtime would be advisable before production use.

## 🔮 Future Improvements

- Add a client interface for submitting commands to the cluster.
- Implement and verify replicated state-machine operations.
- Add controlled node-failure and recovery experiments.
- Measure leader-election time and recovery behavior.
- Collect structured logs and metrics for each node.
- Add automated tests for cluster startup and node availability.
- Upgrade the Python image and dependency versions after compatibility testing.
- Add a visualization dashboard showing node roles and cluster status.

## 🎓 Learning Outcomes

This project provides practical exposure to:

- Distributed systems and consensus concepts.
- Raft leader election.
- Asynchronous Python programming.
- Containerized service design.
- Multi-container orchestration with Docker Compose.
- Network configuration and service discovery.
- Debugging and observing multi-node applications.

## 👨‍💻 Author

**Chirag GD**

- GitHub: [@ChiragGD](https://github.com/ChiragGD)
- LeetCode: [chiraggd](https://leetcode.com/u/chiraggd/)

---

*Developed as a learning project to explore distributed systems, Raft-based cluster coordination, and Docker orchestration.*
