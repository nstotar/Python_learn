# Define the BankAccount class
class BankAccount:
    def __init__(self):
        self.balance = 0  # Initialize balance to 0

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        print(f"Deposit of {amount} successful. Current balance: {self.balance}")

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        self.balance -= amount
        print(f"Withdrawal of {amount} successful. Current balance: {self.balance}")

# Create an instance of BankAccount
account = BankAccount()

# Get user input for deposit and withdrawal amounts
try:
    deposit_amount = int(input("Deposit amount: ").split(': ')[-1])
    account.deposit(deposit_amount)
except ValueError as e:
    print(f"Deposit failed. {e}")

try:
    withdraw_amount = int(input("Withdraw amount: ").split(': ')[-1])
    account.withdraw(withdraw_amount)
except ValueError as e:
    print(f"Withdrawal failed. {e}")