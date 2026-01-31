from collections import Counter

def try_accept(node):
    """Le nœud essaie d'accepter une valeur selon le soutien dans son quorum slice"""
    votes = node.observe_votes()
    if not votes:
        return None

    counter = Counter(votes)
    value, count = counter.most_common(1)[0]

    # Soutien suffisant = majorité du quorum slice
    if count >= (len(node.quorum_slice) // 2) + 1:
        node.accepted_value = value
        node.collection.insert_one({
            "node": node.name,
            "value": value,
            "type": "accept"
        })
        return value

    return None
