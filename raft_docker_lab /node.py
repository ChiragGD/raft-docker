import sys
import asyncio
import raftos

"""
node.py

This script starts a Raft node inside a Docker container.
Each container passes its node ID as a command-line argument.

Example:
python node.py 1
python node.py 2
...
python node.py 5
"""

# =========================
# GET NODE ID FROM ARGUMENT
# =========================

if len(sys.argv) != 2:
    print("Usage: python node.py <node_id>")
    sys.exit(1)

node_id = int(sys.argv[1])

# =========================
# DEFINE CLUSTER NODES
# =========================

cluster = {
    1: ("node1", 8001),
    2: ("node2", 8002),
    3: ("node3", 8003),
    4: ("node4", 8004),
    5: ("node5", 8005),
}

# =========================
# MAIN RAFT FUNCTION
# =========================

async def main():

    print(f"Starting Node {node_id}...")

    # Configure Raft
    await raftos.configure(
        {
            "log_path": f"logs/node_{node_id}",
            "serializer": raftos.serializers.JSONSerializer,
        }
    )

    # Register node in cluster
    await raftos.register(
        cluster[node_id],
        list(cluster.values())
    )

    print(f"Node {node_id} registered successfully.")

    # =========================
    # CONTINUOUS STATUS CHECK
    # =========================

    while True:

        leader = raftos.get_leader()

        if leader is None:
            print(f"[Node {node_id}] Waiting for leader election...")

        elif leader == cluster[node_id]:
            print(f"[LEADER Node {node_id}] I am the leader")

        else:
            print(
                f"[FOLLOWER Node {node_id}] Current leader:",
                leader
            )

        await asyncio.sleep(3)


# =========================
# ENTRY POINT
# =========================

if __name__ == "__main__":

    try:
        asyncio.run(main())

    except KeyboardInterrupt:
        print(f"Node {node_id} shutting down...")