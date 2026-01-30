import time
from .config import db
from .node import Node

# -----------------------------
# Configuration FAUSSE (volontaire)
# -----------------------------
NODES = ["node1", "node2", "node3", "node4", "node5"]
W = 2   # Write quorum (trop petit)
R = 2   # Read quorum (trop petit)

def init_database():
    for node in NODES:
        db[node].delete_many({})

def write_to_nodes(nodes, key, value):
    timestamp = time.time()
    for node_name in nodes:
        node = Node(node_name, db[node_name])
        node.write({
            "key": key,
            "value": value,
            "timestamp": timestamp
        })

def read_from_nodes(nodes, key):
    results = []
    for node_name in nodes:
        node = Node(node_name, db[node_name])
        data = node.read(key)
        if data:
            results.append(data)

    if not results:
        return None

    latest = max(results, key=lambda x: x["timestamp"])
    return latest["value"]

def run_simulation_contradiction():
    print("Configuration : N=5, W=2, R=2  => R + W = 4 ≤ 5 \n")

    init_database()

    # Écriture 1
    print("Écriture de la valeur 10 sur node1, node2")
    write_to_nodes(["node1", "node2"], "x", 10)
    time.sleep(1)

    # Écriture 2 (nouvelle valeur)
    print("Écriture de la valeur 20 sur node3, node4")
    write_to_nodes(["node3", "node4"], "x", 20)
    time.sleep(1)

    # Lecture depuis des noeuds qui N'ONT PAS la dernière valeur
    print("Lecture depuis node1, node2 (anciennes valeurs)")
    value = read_from_nodes(["node1", "node2"], "x")

    print("\n Valeur lue :", value)
    print("La dernière valeur écrite était 20")
    print("Le quorum-based algorithm a ÉCHOUÉ\n")

if __name__ == "__main__":
    run_simulation_contradiction()
