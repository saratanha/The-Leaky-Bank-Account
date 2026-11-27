class BankAccount:

    def __init__(self, owner, balance):
        self.__owner = owner
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        # BUG: Does not check for negative amounts!
        if amount > self.__balance:
            raise ValueError("Insufficient funds!")
        self.__balance -= amount

    def getBalance(self):
        return self.__balance
