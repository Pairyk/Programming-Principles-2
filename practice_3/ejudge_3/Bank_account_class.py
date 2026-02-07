class Account():
    def __init__(self, balance):
        self.balance = balance

    def withdrawal(self, amount):
        if self.balance >= amount:
            return self.balance - amount
        else:
            return "Insufficient Funds"
        
balance, wtdr_amn = map(int, input().split())
acc = Account(balance)
print(acc.withdrawal(wtdr_amn))

