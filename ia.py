from pymerkle import MerkleTree

tree = MerkleTree()


def create_merkle_tree(xi):
    for data in xi:
        tree.append_entry(data)


def verify_merkle_path(root):
    proof = tree.prove_inclusion(root)
    return proof.serialize()
