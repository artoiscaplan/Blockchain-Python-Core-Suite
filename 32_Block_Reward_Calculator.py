class BlockReward:
    def __init__(self, initial=50, halving=210000):
        self.initial = initial
        self.halving = halving

    def get_reward(self, height):
        halvings = height // self.halving
        return self.initial / (2 ** halvings)


if __name__ == "__main__":
    br = BlockReward()
    print(f"区块奖励:{br.get_reward(0)}")
