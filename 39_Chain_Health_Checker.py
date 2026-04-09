class ChainHealth:
    def check_health(self, chain):
        if len(chain) <1:
            return "不健康:空链"
        if not self.check_hashes(chain):
            return "不健康:哈希错误"
        return "健康"

    def check_hashes(self, chain):
        for i in range(1,len(chain)):
            if chain[i]["prev_hash"] != chain[i-1]["hash"]:
                return False
        return True

if __name__ == "__main__":
    health = ChainHealth()
    print(health.check_health([]))
