class BankAccount:
    def __init__(self, owner, balance=0):
        self.__owner = owner
        self.__balance = balance
    def deposit(self, amount):
        if amount <= 0:
            print("Deposit must be positive")
            return
        self.__balance += amount
    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds")
            return
        self.__balance -= amount
    def get_balance(self):
        return self.__balance
account = BankAccount("Alex", 1000)
account.deposit(500)
account.withdraw(300)
print(account.get_balance())