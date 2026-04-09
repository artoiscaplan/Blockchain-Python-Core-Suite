class DEX:
    def __init__(self):
        self.order_book = []

    def create_order(self, owner, side, price, amount):
        self.order_book.append({
            "owner":owner,"side":side,"price":price,"amount":amount
        })

    def match_orders(self):
        buy = [o for o in self.order_book if o["side"]=="buy"]
        sell = [o for o in self.order_book if o["side"]=="sell"]
        return len(buy)>0 and len(sell)>0

if __name__ == "__main__":
    dex = DEX()
    dex.create_order("user","buy",100,10)
    print("订单创建完成")
