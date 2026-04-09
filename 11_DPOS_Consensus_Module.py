import random

class DPOSConsensus:
    def __init__(self):
        self.candidates = []
        self.delegates = []

    def add_candidate(self, addr):
        self.candidates.append(addr)

    def vote_and_select(self, votes, count=5):
        sorted_votes = sorted(votes.items(), key=lambda x:x[1], reverse=True)
        self.delegates = [item[0] for item in sorted_votes[:count]]
        return self.delegates

    def get_block_producer(self):
        return random.choice(self.delegates)

if __name__ == "__main__":
    dpos = DPOSConsensus()
    dpos.add_candidate("nodeA")
    print("DPOS候选节点添加完成")
