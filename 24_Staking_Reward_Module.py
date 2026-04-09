class StakingReward:
    def __init__(self, apy=0.05):
        self.stakes = {}
        self.apy = apy

    def stake(self, addr, amount):
        self.stakes[addr] = self.stakes.get(addr,0)+amount

    def calculate_reward(self, addr, days):
        return self.stakes.get(addr,0)*self.apy*(days/365)

if __name__ == "__main__":
    stake = StakingReward()
    stake.stake("user",1000)
    print(f"奖励:{stake.calculate_reward('user',30)}")
