
class BankAccount:
    def __init__(self, start_balance = 0):

        self.account_balance = start_balance

    def deposit(self, amount):
        self.account_balance += amount
        print(f"Deposited: {amount}")

    def withdraw(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            return self.account_balance
        else:
            print("Insufficient funds")
            return self.account_balance


    def display_balance(self):
        print(f"Current Balance: {float(self.account_balance)}")
