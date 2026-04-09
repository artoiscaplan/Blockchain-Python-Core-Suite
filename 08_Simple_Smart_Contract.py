class SimpleSmartContract:
    def __init__(self):
        self.balances = {}

    def deposit(self, address, amount):
        if address not in self.balances:
            self.balances[address] = 0
        self.balances[address] += amount
        return True

    def transfer(self, sender, receiver, amount):
        if self.balances.get(sender,0) < amount:
            return False
        self.balances[sender] -= amount
        self.balances[receiver] = self.balances.get(receiver,0) + amount
        return True

    def get_balance(self, address):
        return self.balances.get(address,0)

if __name__ == "__main__":
    contract = SimpleSmartContract()
    contract.deposit("user1",100)
    contract.transfer("user1","user2",50)
    print(f"user2余额:{contract.get_balance('user2')}")
