from config import db

class FBANode:
    def __init__(self, name, collection, quorum_slice):
        self.name = name
        self.collection = collection       # Collection MongoDB du nœud
        self.quorum_slice = quorum_slice   # Liste des nœuds de confiance
        self.accepted_value = None         # Valeur acceptée

    def vote(self, value):
        """Le nœud vote pour une valeur et stocke le vote dans sa collection"""
        self.collection.insert_one({
            "node": self.name,
            "value": value,
            "type": "vote"
        })

    def observe_votes(self):
        """Observe les votes de tous les nœuds dans son quorum slice"""
        votes = []
        for node_name in self.quorum_slice:
            votes_collection = db[node_name]  # Collection du nœud dans le quorum slice
            votes_docs = votes_collection.find({"type": "vote"})
            votes.extend([v["value"] for v in votes_docs])
        return votes

    def try_accept(self):
        """Essaye d’accepter une valeur si le quorum slice soutient suffisamment la même valeur"""
        votes = self.observe_votes()
        if not votes:
            return None

        # Compte les occurrences de chaque valeur
        counts = {}
        for v in votes:
            counts[v] = counts.get(v, 0) + 1

        # Vérifie si une valeur atteint la majorité simple du quorum slice
        majority = (len(self.quorum_slice) // 2) + 1
        for value, count in counts.items():
            if count >= majority:
                self.accepted_value = value
                return value

        return None
