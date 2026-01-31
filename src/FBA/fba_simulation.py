from config import db, QUORUM_SLICES
from node import FBANode
from fba_accept import try_accept
import time

def init_db():
    """Supprime toutes les données existantes dans MongoDB"""
    for n in QUORUM_SLICES.keys():
        db[n].delete_many({})

def run_simulation():
    print("\n--- Simulation FBA ---\n")
    init_db()

    # Création des nœuds
    nodes = {
        name: FBANode(name, db[name], QUORUM_SLICES[name])
        for name in QUORUM_SLICES
    }

    # --------------------------
    # Phase 1 : votes initiaux
    # --------------------------
    print("Phase 1 : Votes initiaux\n")
    
    nodes["A"].vote("TX1")
    print("Node A voted TX1")
    nodes["B"].vote("TX1")
    print("Node B voted TX1")
    nodes["C"].vote("TX2")
    print("Node C voted TX2")
    nodes["D"].vote("TX1")
    print("Node D voted TX1")
    nodes["E"].vote("TX2")
    print("Node E voted TX2")

    time.sleep(1)

    # --------------------------
    # Phase 2 : acceptation
    # --------------------------
    print("\nPhase 2 : Acceptation\n")
    for node in nodes.values():
        accepted = try_accept(node)
        if accepted:
            print(f"Node {node.name} ACCEPTS {accepted}")
        else:
            print(f"Node {node.name} did not accept any value")

if __name__ == "__main__":
    run_simulation()
