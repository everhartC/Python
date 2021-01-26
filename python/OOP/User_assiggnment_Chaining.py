class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
        #self.transfer_money = name

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print("User: ", self.name, ", Balance: ", self.account_balance)
        return self

    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        print(f"{self.name} transfered {amount} to {other_user.name}")
        print(f"{self.name} Account Balance: {self.account_balance}")
        print(f"{other_user.name} Account Balance: {other_user.account_balance}")
        return self

a = User("Cameron", "cam@gmail.com")
b = User("Ben", "ben@gmail.com")
c = User("Carson", "car@gmail.com")

a.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawal(250).display_user_balance()
b.make_deposit(140).make_deposit(160).make_withdrawal(100).make_withdrawal(50).display_user_balance()
c.make_deposit(300).make_withdrawal(50).make_withdrawal(20).make_withdrawal(20).display_user_balance()


print("------ TRANSFER --------")
b.transfer_money(a,150)
