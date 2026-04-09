class UTXOGenerator:
    def __init__(self):
        self.utxo_set = {}

    def create_utxo(self, tx_id, index, address, amount):
        key = f"{tx_id}_{index}"
        self.utxo_set[key] = {
            "address": address,
            "amount": amount,
            "spent": False
        }

    def spend_utxo(self, tx_id, index):
        key = f"{tx_id}_{index}"
        if key in self.utxo_set and not self.utxo_set[key]["spent"]:
            self.utxo_set[key]["spent"] = True
            return True
        return False

if __name__ == "__main__":
    utxo = UTXOGenerator()
    utxo.create_utxo("tx001",0,"addr_test",200)
    print("UTXO创建成功")
