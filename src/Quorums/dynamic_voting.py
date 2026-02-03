# dynamic_voting.py
# Exemple de Dynamic Voting avec 3 serveurs et redistribution des votes en cas de panne

class Server:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.active = True  # True = serveur actif, False = serveur en panne

    def respond(self):
        """Retourne le poids si le serveur est actif, sinon 0"""
        return self.weight if self.active else 0

def simulate_dynamic_voting(servers, quorum_required):
    total_votes = sum(server.respond() for server in servers)
    print("Votes reçus :", {s.name: s.respond() for s in servers})
    print("Total des votes =", total_votes)
    if total_votes >= quorum_required:
        print("Quorum atteint. Opération autorisée.\n")
    else:
        print("Quorum non atteint. Opération refusée.\n")

# -------------------------
# Situation initiale
servers = [
    Server("A", 2),
    Server("B", 1),
    Server("C", 1)
]

quorum_required = 3

print("---- Lecture / Écriture initiale ----")
simulate_dynamic_voting(servers, quorum_required)


# Cas : Serveur A tombe en panne
print("---- Serveur A est tombe en panne----")
servers[0].active = False

# Redistribution des votes (Dynamic Voting)
# Ici, on ajuste les poids comme dans l'exemple
servers[1].weight = 2  # B prend plus de poids
servers[2].weight = 2  # C prend plus de poids

simulate_dynamic_voting(servers, quorum_required)
