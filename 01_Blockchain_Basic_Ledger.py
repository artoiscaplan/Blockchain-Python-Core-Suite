import hashlib
import json
from time import time

class BasicBlockchainLedger:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = {
            "index": 0,
            "timestamp": time(),
            "data": "genesis_block",
            "previous_hash": "0",
            "hash": self.compute_hash({})
        }
        self.chain.append(genesis_block)

    def compute_hash(self, block):
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def add_new_block(self, data):
        last_block = self.chain[-1]
        new_block = {
            "index": len(self.chain),
            "timestamp": time(),
            "data": data,
            "previous_hash": last_block["hash"],
            "hash": self.compute_hash({
                "index": len(self.chain),
                "data": data,
                "previous_hash": last_block["hash"]
            })
        }
        self.chain.append(new_block)
        return new_block

if __name__ == "__main__":
    ledger = BasicBlockchainLedger()
    ledger.add_new_block("user_transfer_100")
    print("区块链账本创建完成")
