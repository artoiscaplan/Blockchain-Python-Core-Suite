import hashlib
import json
from time import time

class FullBlockchainCore:
    def __init__(self):
        self.chain = []
        self.mempool = []
        self.difficulty = 4
        self.create_genesis()

    def create_genesis(self):
        block = {
            "height":0,"time":time(),"txs":[],"prev_hash":"0",
            "hash":hashlib.sha256(b"genesis").hexdigest()
        }
        self.chain.append(block)

    def add_tx(self, tx):
        self.mempool.append(tx)

    def mine(self):
        last = self.chain[-1]
        txs = self.mempool[:10]
        self.mempool = self.mempool[10:]
        nonce = 0
        while True:
            b = {
                "height":len(self.chain),"time":time(),"txs":txs,
                "prev_hash":last["hash"],"nonce":nonce
            }
            h = hashlib.sha256(json.dumps(b).encode()).hexdigest()
            if h[:self.difficulty] == "0"*self.difficulty:
                b["hash"]=h
                self.chain.append(b)
                return b
            nonce +=1

if __name__ == "__main__":
    core = FullBlockchainCore()
    print("区块链核心引擎启动完成")
