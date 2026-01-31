from pymongo import MongoClient

# Liste des nœuds
NODES = ["A", "B", "C", "D", "E"]

# Quorum slices : chaque nœud choisit son quorum slice (les nœuds de confiance)
QUORUM_SLICES = {
    "A": ["B", "C", "D"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D"],
    "D": ["A", "B", "C"],
    "E": ["C", "D"]
}

# Connexion à MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["fba_system"]
