class Mempool:
    def __init__(self):
        self.pending_txs = []

    def add_tx(self, tx):
        self.pending_txs.append(tx)

    def get_txs_for_block(self, max_count=10):
        selected = self.pending_txs[:max_count]
        self.pending_txs = self.pending_txs[max_count:]
        return selected

if __name__ == "__main__":
    mem = Mempool()
    mem.add_tx({"id":"tx1"})
    print(mem.get_txs_for_block())
