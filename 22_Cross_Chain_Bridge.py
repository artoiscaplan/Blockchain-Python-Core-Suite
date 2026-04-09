class CrossChainBridge:
    def __init__(self):
        self.locked_assets = {}

    def lock_asset(self, chain, addr, asset_id, amount):
        key = f"{chain}_{asset_id}"
        self.locked_assets[key] = {"addr":addr,"amount":amount}
        return True

    def unlock_asset(self, chain, asset_id):
        key = f"{chain}_{asset_id}"
        return self.locked_assets.pop(key, None)

if __name__ == "__main__":
    bridge = CrossChainBridge()
    bridge.lock_asset("chainA","user1","token1",500)
    print("跨链资产锁定完成")
