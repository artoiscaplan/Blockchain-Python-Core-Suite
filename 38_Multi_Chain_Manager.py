class MultiChainManager:
    def __init__(self):
        self.chains = {}

    def add_chain(self, chain_name, chain_obj):
        self.chains[chain_name] = chain_obj

    def get_chain(self, chain_name):
        return self.chains.get(chain_name)

if __name__ == "__main__":
    mcm = MultiChainManager()
    mcm.add_chain("eth",[])
    print("多链管理完成")
