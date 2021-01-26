#%%
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
        #self.transfer_money = name

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print("User: ", self.name, ", Balance: ", self.account_balance)
    
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        print(f"{self.name} transfered {amount} to {other_user.name}")
        print(f"{self.name} Account Balance: {self.account_balance}")
        print(f"{other_user.name} Account Balance: {other_user.account_balance}")

a = User("Cameron", "cam@gmail.com")
b = User("Ben", "ben@gmail.com")
c = User("Carson", "car@gmail.com")

a.make_deposit(100)
a.make_deposit(200)
a.make_deposit(300)
a.make_withdrawal(250)
a.display_user_balance()

b.make_deposit(140)
b.make_deposit(160)
b.make_withdrawal(100)
b.make_withdrawal(50)
b.display_user_balance()

c.make_deposit(300)
c.make_withdrawal(50)
c.make_withdrawal(20)
c.make_withdrawal(20)
c.display_user_balance()

print("------ TRANSFER --------")
b.transfer_money(a,150)

