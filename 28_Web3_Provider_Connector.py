class Web3Provider:
    def __init__(self, rpc_url):
        self.rpc = rpc_url
        self.connected = False

    def connect(self):
        self.connected = True
        return f"已连接:{self.rpc}"

    def get_block_number(self):
        return 1000 if self.connected else -1

if __name__ == "__main__":
    w3 = Web3Provider("http://localhost:8545")
    print(w3.connect())
