import hashlib

class ZKProof:
    def __init__(self, secret):
        self.secret = secret
        self.commit = hashlib.sha256(secret.encode()).hexdigest()

    def prove(self, guess):
        return hashlib.sha256(guess.encode()).hexdigest() == self.commit

if __name__ == "__main__":
    zk = ZKProof("my_secret")
    print(f"验证结果:{zk.prove('my_secret')}")
