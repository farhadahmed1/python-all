class Bank:
    def __init__(self, balance):
        self.balance = balance
        self.min_withdraw =100
        self.max_withdraw =10000

    def get_balance(self): 
        return f'Your total balance  {self.balance}'

    def withdraw(self, amount):
       if amount < self.min_withdraw :
            return f'You present amount not enough to withdraw .Minimum withdraw : {self.min_withdraw}'
       elif amount > self.max_withdraw :
            return f"you crossed maximum limit : {self.max_withdraw}"
       elif amount > self.balance :
            return " You  are broke !! No money for you "
       else:
           self.balance =  self.balance - amount
           return f"Here is You money: {amount}"
    def deposit(self, amount):
        self.balance = self.balance + amount

One_bank = Bank(10000) 
withdraw = One_bank.withdraw(500)
print(withdraw)
balance = One_bank.get_balance()
print(balance)
deposit = One_bank.deposit(5000)
balance = One_bank.get_balance()
print(balance)

