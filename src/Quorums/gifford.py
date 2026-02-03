# gifford.py
# Exemple de Consensus par quorum (Gifford) avec lecture et écriture

class Server:
    def __init__(self, name, value=0, version=0):
        self.name = name
        self.value = value
        self.version = version
        self.active = True  # True = serveur actif, False = serveur en panne

    def write(self, new_value):
        if self.active:
            self.value = new_value
            self.version += 1
            print(f"{self.name} écrit la valeur {new_value}, version {self.version}")
            return True
        else:
            print(f"{self.name}  serveur en panne, écriture impossible")
            return False

    def read(self):
        if self.active:
            return (self.value, self.version)
        else:
            return None

# -------------------------
# Création des 5 serveurs
S1 = Server("S1")
S2 = Server("S2")
S3 = Server("S3")
S4 = Server("S4")
S5 = Server("S5")

servers = [S1, S2, S3, S4, S5]

# Paramètres du quorum
R = 3  # quorum lecture
W = 3  # quorum écriture

# -------------------------
# Cas 1 : Écriture
print("---- Écriture ----")
write_value = 42
votes = 0
for s in servers:
    if s.write(write_value):
        votes += 1
    if votes >= W:
        break

if votes >= W:
    print(f" Écriture validée sur {votes} serveurs\n")
else:
    print(f" Écriture échouée, quorum non atteint\n")

# -------------------------
# Cas 2 : Lecture
print("---- Lecture ----")
read_values = []
for s in servers:
    result = s.read()
    if result:
        read_values.append(result)
    if len(read_values) >= R:
        break

# Choisir la valeur avec la version la plus récente
latest_value = max(read_values, key=lambda x: x[1])
print(f" Lecture cohérente : valeur = {latest_value[0]}, version = {latest_value[1]}\n")

# -------------------------
# Cas de panne : 2 serveurs tombent en panne
print("---- Panne de 2 serveurs ----")
S1.active = False
S2.active = False

# Réécriture
votes = 0
for s in servers:
    if s.write(100):
        votes += 1
    if votes >= W:
        break

if votes >= W:
    print(f" Écriture validée malgré les pannes ({votes} serveurs actifs)\n")
else:
    print(f" Écriture échouée, quorum non atteint\n")
