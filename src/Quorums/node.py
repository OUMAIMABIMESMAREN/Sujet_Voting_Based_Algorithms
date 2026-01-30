class Node:
    def __init__(self, name, collection):
        self.name = name
        self.collection = collection
        self.active = True  # Simule si le noeud est actif ou non

    def write(self, data):
        if self.active:
            self.collection.insert_one(data)

    def read(self, key):
        if not self.active:
            return None
        return self.collection.find_one(
            {"key": key},
            sort=[("timestamp", -1)]
        )
