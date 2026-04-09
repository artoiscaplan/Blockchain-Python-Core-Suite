class ChainAnalytics:
    def __init__(self, chain):
        self.chain = chain

    def total_blocks(self):
        return len(self.chain)

    def average_block_time(self):
        if len(self.chain) <2:
            return 0
        times = [b["timestamp"] for b in self.chain]
        diffs = [times[i]-times[i-1] for i in range(1,len(times))]
        return sum(diffs)/len(diffs)

if __name__ == "__main__":
    tracker = ChainAnalytics([])
    print(f"区块总数:{tracker.total_blocks()}")
