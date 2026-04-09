class DynamicDifficulty:
    def __init__(self, base=4, target_time=10):
        self.base = base
        self.target = target_time

    def adjust(self, last_block_time):
        if last_block_time < self.target:
            return self.base +1
        elif last_block_time > self.target*2:
            return max(1, self.base-1)
        return self.base

if __name__ == "__main__":
    dd = DynamicDifficulty()
    print(f"调整难度:{dd.adjust(5)}")
