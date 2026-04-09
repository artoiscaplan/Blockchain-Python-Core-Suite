import hashlib
import json
from time import time

class BlockMiner:
    def __init__(self):
        self.chain = []
        self.difficulty = 4

    def mine_block(self, transactions):
        last_block = self.chain[-1] if self.chain else {"hash":"genesis"}
        nonce = 0
        while True:
            block = {
                "height": len(self.chain),
                "time": time(),
                "transactions": transactions,
                "prev_hash": last_block["hash"],
                "nonce": nonce
            }
            h = hashlib.sha256(json.dumps(block).encode()).hexdigest()
            if h[:self.difficulty] == "0"*self.difficulty:
                block["hash"] = h
                self.chain.append(block)
                return block
            nonce +=1

if __name__ == "__main__":
    miner = BlockMiner()
    block = miner.mine_block(["tx_a","tx_b"])
    print(f"挖矿成功 区块高度:{block['height']}")
