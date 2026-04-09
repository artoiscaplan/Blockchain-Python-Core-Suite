class ChainAPISim:
    def get_chain(self):
        return {"chain_length":100,"status":"ok"}

    def get_balance(self, addr):
        return {"address":addr,"balance":1000}

if __name__ == "__main__":
    api = ChainAPISim()
    print(api.get_chain())
