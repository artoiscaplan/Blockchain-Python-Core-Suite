class ForkResolver:
    def resolve(self, chains):
        return max(chains, key=lambda x:len(x))

if __name__ == "__main__":
    fr = ForkResolver()
    best = fr.resolve([[1,2],[1,2,3]])
    print(f"最优链长度:{len(best)}")
