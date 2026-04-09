class PBFTNode:
    def __init__(self, node_id):
        self.id = node_id
        self.state = "init"

    def pre_prepare(self, msg):
        self.state = "pre_prepared"
        return True

    def prepare(self):
        if self.state == "pre_prepared":
            self.state = "prepared"
            return True
        return False

    def commit(self):
        if self.state == "prepared":
            self.state = "committed"
            return True
        return False

if __name__ == "__main__":
    node = PBFTNode(1)
    node.pre_prepare("tx_msg")
    node.prepare()
    print(f"PBFT状态:{node.state}")
