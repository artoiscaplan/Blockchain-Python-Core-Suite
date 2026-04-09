class MultiSigWallet:
    def __init__(self, owners, required):
        self.owners = owners
        self.required = required
        self.signatures = []

    def add_signature(self, owner):
        if owner in self.owners and owner not in self.signatures:
            self.signatures.append(owner)

    def can_execute(self):
        return len(self.signatures)>=self.required

if __name__ == "__main__":
    wallet = MultiSigWallet(["a","b","c"],2)
    wallet.add_signature("a")
    print(f"可执行:{wallet.can_execute()}")
