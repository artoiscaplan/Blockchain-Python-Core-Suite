import time

class TimeLockContract:
    def __init__(self, unlock_time):
        self.unlock_time = unlock_time
        self.funds = {}

    def deposit(self, addr, amount):
        self.funds[addr] = amount

    def withdraw(self, addr):
        if time.time() >= self.unlock_time:
            return self.funds.pop(addr,0)
        return 0

if __name__ == "__main__":
    lock = TimeLockContract(time.time()+3600)
    lock.deposit("user",500)
    print("时间锁存款完成")
