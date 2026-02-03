# maekawa.py
# Exemple de l'algorithme de Maekawa avec 5 processus et quorums chevauchants

class Process:
    def __init__(self, name):
        self.name = name
        self.in_cs = False  # True si le processus est dans la section critique

    def vote(self, requester):
        """Donne un vote si libre"""
        if not self.in_cs:
            print(f"{self.name} vote OK pour {requester.name}")
            return True
        else:
            print(f"{self.name} ne peut pas voter pour {requester.name}, déjà en section critique")
            return False

# -------------------------
# Création des processus
P1 = Process("P1")
P2 = Process("P2")
P3 = Process("P3")
P4 = Process("P4")
P5 = Process("P5")

# Définition des quorums
quorums = {
    P1: [P1, P2, P3],
    P2: [P2, P3, P4],
    P3: [P3, P4, P5],
    # P4 et P5 peuvent avoir leurs quorums si besoin
}

# -------------------------
# Étape 1 : P1 demande à entrer dans la section critique
requester = P1
requester_quorum = quorums[requester]

print(f"--- {requester.name} demande l'accès à la section critique ---")

# Étape 2 : Votes
votes = []
for p in requester_quorum:
    if p.vote(requester):
        votes.append(p)

# Étape 3 : Vérification quorum
if len(votes) == len(requester_quorum):
    print(f" {requester.name} entre dans la section critique")
    requester.in_cs = True
else:
    print(f" {requester.name} ne peut pas entrer, quorum non atteint")
