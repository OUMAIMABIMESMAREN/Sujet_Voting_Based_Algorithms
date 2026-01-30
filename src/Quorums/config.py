from pymongo import MongoClient

# Nombre de noeuds
NODES = ["node1", "node2", "node3", "node4", "node5"]

# Taille des quorums
W = 3  # Write quorum
R = 3  # Read quorum

# Vérification de la condition de cohérence
assert R + W > len(NODES), "Condition R + W > N non respectée"

# Connexion MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["quorum_system"]
