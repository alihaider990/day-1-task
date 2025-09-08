class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance  

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds or invalid amount.")

    @property
    def balance(self):
        return self.__balance


account = BankAccount(100)
account.deposit(50)
account.withdraw(30)
print("Current balance:", account.balance)  



    






















