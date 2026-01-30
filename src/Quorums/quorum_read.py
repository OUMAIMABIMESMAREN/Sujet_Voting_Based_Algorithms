import random
from .config import NODES, R, db
from .node import Node

def quorum_read(key):
    selected_nodes = random.sample(NODES, R)
    results = []

    print(f" Lecture depuis les noeuds : {selected_nodes}")

    for node_name in selected_nodes:
        node = Node(node_name, db[node_name])
        data = node.read(key)
        if data:
            results.append(data)

    if not results:
        return None

    latest = max(results, key=lambda x: x["timestamp"])
    return latest["value"]
