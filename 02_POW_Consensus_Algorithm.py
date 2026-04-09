import hashlib
import json
from time import time

class POWConsensus:
    def __init__(self, difficulty=4):
        self.difficulty = difficulty
        self.chain = []

    def hash_block(self, block):
        encoded = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded).hexdigest()

    def proof_of_work(self, prev_hash, index, data):
        nonce = 0
        while True:
            block = {
                "index": index,
                "prev_hash": prev_hash,
                "data": data,
                "nonce": nonce
            }
            hash_val = self.hash_block(block)
            if hash_val[:self.difficulty] == "0"*self.difficulty:
                return nonce, hash_val
            nonce += 1

if __name__ == "__main__":
    pow = POWConsensus(difficulty=3)
    nonce, res_hash = pow.proof_of_work("init_hash", 1, "tx_data")
    print(f"POW计算完成 随机数:{nonce} 哈希:{res_hash}")
