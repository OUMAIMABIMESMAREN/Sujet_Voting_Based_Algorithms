import time
from .config import db, NODES
from .quorum_write import quorum_write
from .quorum_read import quorum_read

def init_database():
    for node in NODES:
        db[node].delete_many({})

def run_simulation():
    print("\n--- Simulation Quorum-Based Algorithm ---\n")
    init_database()

    quorum_write("x", 10)
    time.sleep(1)

    quorum_write("x", 20)
    time.sleep(1)

    value = quorum_read("x")

    print("\n Valeur finale lue :", value)

if __name__ == "__main__":
    run_simulation()
