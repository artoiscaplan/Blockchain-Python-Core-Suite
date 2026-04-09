class P2PNetwork:
    def __init__(self):
        self.peers = []

    def add_peer(self, host, port):
        self.peers.append({"host":host,"port":port})

    def broadcast(self, msg):
        for p in self.peers:
            print(f"发送到{p}: {msg}")

if __name__ == "__main__":
    net = P2PNetwork()
    net.add_peer("localhost",8888)
    net.broadcast("new_block")
