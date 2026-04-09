import hashlib

class MerkleTree:
    def __init__(self, transactions):
        self.transactions = transactions
        self.root = self.build_merkle_root()

    def hash_node(self, data):
        return hashlib.sha256(str(data).encode()).hexdigest()

    def build_merkle_root(self):
        if len(self.transactions) == 0:
            return self.hash_node("empty")
        nodes = [self.hash_node(tx) for tx in self.transactions]
        while len(nodes) > 1:
            temp = []
            for i in range(0, len(nodes), 2):
                left = nodes[i]
                right = nodes[i+1] if i+1 < len(nodes) else left
                temp.append(self.hash_node(left+right))
            nodes = temp
        return nodes[0]

if __name__ == "__main__":
    txs = ["tx1","tx2","tx3","tx4"]
    mt = MerkleTree(txs)
    print(f"默克尔树根:{mt.root}")
