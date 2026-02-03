# majority_quorum.py
# Exemple de Quorum Majoritaire avec 5 serveurs

class Server:
    def __init__(self, name):
        self.name = name
        self.active = True  # True = serveur répond OK

    def respond(self):
        """Retourne True si le serveur répond OK, False sinon"""
        return self.active

def simulate_majority_quorum(servers, quorum_required, responding_servers):
    total_ok = sum(s.respond() for s in responding_servers)
    print("Serveurs ayant répondu OK :", [s.name for s in responding_servers])
    print("Total OK =", total_ok)
    if total_ok >= quorum_required:
        print(" Quorum atteint. Opération acceptée.\n")
    else:
        print(" Quorum non atteint. Opération refusée.\n")

# -------------------------
# Situation de départ
S1 = Server("S1")
S2 = Server("S2")
S3 = Server("S3")
S4 = Server("S4")
S5 = Server("S5")

servers = [S1, S2, S3, S4, S5]
quorum_required = 3  # majorité

# -------------------------
# Cas 1 : Lecture réussie
print("---- Lecture ----")
responding_servers = [S1, S2, S3]  # 3 serveurs répondent OK
simulate_majority_quorum(servers, quorum_required, responding_servers)

# -------------------------
# Cas 2 : Écriture refusée
print("---- Écriture ----")
responding_servers = [S2, S4]  # 2 serveurs répondent OK
simulate_majority_quorum(servers, quorum_required, responding_servers)
