import hashlib
import random
import string

class BlockchainWallet:
    def __init__(self):
        self.private_key = self.generate_private_key()
        self.public_key = self.generate_public_key()
        self.address = self.generate_wallet_address()

    def generate_private_key(self):
        random_str = ''.join(random.choices(string.ascii_letters + string.digits, k=64))
        return hashlib.sha256(random_str.encode()).hexdigest()

    def generate_public_key(self):
        return hashlib.sha512(self.private_key.encode()).hexdigest()

    def generate_wallet_address(self):
        pub_hash = hashlib.sha256(self.public_key.encode()).digest()
        return hashlib.ripemd160(pub_hash).hexdigest()

if __name__ == "__main__":
    wallet = BlockchainWallet()
    print(f"钱包地址:{wallet.address}")
