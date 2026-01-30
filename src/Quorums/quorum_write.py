import time
import random
from .config import NODES, W, db
from .node import Node

def quorum_write(key, value):
    timestamp = time.time()
    selected_nodes = random.sample(NODES, W)

    print(f" Écriture sur les noeuds : {selected_nodes}")

    for node_name in selected_nodes:
        node = Node(node_name, db[node_name])
        node.write({
            "key": key,
            "value": value,
            "timestamp": timestamp
        })
