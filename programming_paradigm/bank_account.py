
class BankAccount:
    def __init__(self, start_balance = 0):

        self.account_balance = start_balance

    def deposit (self, amount):
        self.account_balance += amount
        return self.account_balance

    def withdraw(self, amount):
        if (self.account_balance - amount ) >= 0:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        print(f"Your balance is: ${self.account_balance}")
