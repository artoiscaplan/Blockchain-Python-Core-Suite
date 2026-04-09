class GovernanceVote:
    def __init__(self):
        self.proposals = {}

    def create_proposal(self, pid, title):
        self.proposals[pid] = {"title":title,"for":0,"against":0}

    def vote(self, pid, choice):
        if pid in self.proposals:
            self.proposals[pid][choice] +=1

if __name__ == "__main__":
    gov = GovernanceVote()
    gov.create_proposal(1,"upgrade_chain")
    print("提案创建完成")
