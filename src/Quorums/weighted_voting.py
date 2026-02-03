# weighted_voting.py
# Exemple de Weighted Voting avec 4 serveurs et quorum requis

class Server:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.active = True  # True = serveur actif

    def respond(self):
        """Retourne le poids si actif"""
        return self.weight if self.active else 0

def simulate_weighted_voting(servers, quorum_required, responding_servers):
    """servers : liste de tous les serveurs
       responding_servers : liste des serveurs qui répondent à la requête"""
    total_votes = sum(s.respond() for s in responding_servers)
    print("Votes reçus :", {s.name: s.respond() for s in responding_servers})
    print("Total des votes =", total_votes)
    if total_votes >= quorum_required:
        print(" Quorum atteint. Opération acceptée.\n")
    else:
        print(" Quorum non atteint. Opération refusée.\n")

# -------------------------
# Situation de départ
S1 = Server("S1", 3)
S2 = Server("S2", 2)
S3 = Server("S3", 1)
S4 = Server("S4", 1)

servers = [S1, S2, S3, S4]
quorum_required = 4

# -------------------------
# Cas 1 : Quorum atteint
print("---- Quorum atteint ----")
responding_servers = [S1, S3]  # S1=3 votes, S3=1 vote → total 4
simulate_weighted_voting(servers, quorum_required, responding_servers)

# -------------------------
# Cas 2 : Quorum non atteint
print("---- Quorum non atteint ----")
responding_servers = [S2, S3]  # S2=2 votes, S3=1 vote → total 3
simulate_weighted_voting(servers, quorum_required, responding_servers)
