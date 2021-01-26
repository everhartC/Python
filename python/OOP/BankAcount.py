class BankAccount:
    def __init__(self, int_rate=0.01, balance=0):
        self.int_rate = int_rate
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self
    
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        else:
            print("No interest due to $0 in account")
        return self

a = BankAccount()
b = BankAccount()

a.deposit(100).deposit(100).deposit(100).withdraw(50).yield_interest().display_account_info()
b.deposit(500).deposit(100).withdraw(100).withdraw(50).withdraw(50).withdraw(500).yield_interest().display_account_info()
