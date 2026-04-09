import hashlib

class IPFSBlockStorage:
    def __init__(self):
        self.storage = {}

    def save_block(self, block):
        cid = hashlib.sha256(str(block).encode()).hexdigest()
        self.storage[cid] = block
        return cid

    def get_block(self, cid):
        return self.storage.get(cid)

if __name__ == "__main__":
    ipfs = IPFSBlockStorage()
    cid = ipfs.save_block({"data":"test"})
    print(f"存储CID:{cid}")
