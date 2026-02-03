# hierarchical_quorum.py
# Exemple de Quorum Hiérarchique avec 3 niveaux de serveurs

class Server:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.active = True  # True = serveur actif, False = serveur en panne

    def add_child(self, child):
        self.children.append(child)

    def request_vote(self):
        """Demande le quorum à ce serveur et ses enfants"""
        if not self.active:
            print(f"{self.name} __Serveur en panne!")
            return False
        
        print(f"{self.name} = OK")
        # Demande à tous les enfants
        for child in self.children:
            if not child.request_vote():
                return False
        return True

# -------------------------
# Création de la hiérarchie
A = Server("A")  # Niveau 1 (racine)
B = Server("B")  # Niveau 2
C = Server("C")  # Niveau 2
D = Server("D")  # Niveau 3
E = Server("E")  # Niveau 3

# Construction de la hiérarchie
A.add_child(B)
A.add_child(C)
B.add_child(D)
C.add_child(E)

# -------------------------
# Cas normal : lecture/écriture
print("---- Lecture / Écriture normale ----")
A.request_vote()
print("\n")

# -------------------------
# Cas de panne : C est en panne
print("---- Panne du serveur C ----")
C.active = False
A.request_vote()
