class BankAccount:
    def __init__(self, owner, balance=0):
        self.__owner = owner       
        self.__balance = balance 

    def deposit(self, amount):
        if amount > 0:           
            self.__balance += amount
        else:
            print("Deposit must be positive")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal must be positive")
        elif amount > self.__balance:
            print("Not enough balance")
        else:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

account = BankAccount("Ali", 1000)

account.deposit(500)
print(account.get_balance())   

account.withdraw(300)
print(account.get_balance())   
account.withdraw(2000)        
account.deposit(-10)  