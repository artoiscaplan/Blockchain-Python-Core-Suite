class ChainSharding:
    def __init__(self, shard_count=3):
        self.shards = {i:[] for i in range(shard_count)}

    def assign_transaction(self, tx, shard_id):
        if shard_id in self.shards:
            self.shards[shard_id].append(tx)

    def get_shard_txs(self, shard_id):
        return self.shards.get(shard_id,[])

if __name__ == "__main__":
    shard = ChainSharding()
    shard.assign_transaction("shard_tx",0)
    print(shard.get_shard_txs(0))
