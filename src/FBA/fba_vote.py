from .config import db

def fba_vote(node_name, value):
    """Enregistre le vote d'un nœud"""
    db[node_name].insert_one({
        "node": node_name,
        "value": value,
        "type": "vote"
    })
