class Account:
    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount

    def __str__(self):
        return f"Account holder: {self.name}, Account number: {self.account_number}, Balance: {self.balance}"



class SavingsAccount:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount

    def __str__(self):
        return f"Savings Account holder: {self.name}, Balance: {self.balance}"


account1 = Account("1234", "Bugarin-Arce", 1000)
savings_account1 = SavingsAccount("1235", "Bugarin-Arce", 500)

account2 = Account("4639", "Valladares", 1500)
savings_account2 = SavingsAccount("3988", "Valladares", 750)

account3 = Account("9101", "Owora", 2000)
savings_account3 = SavingsAccount("9102", "Owora", 100000)

account4 = Account("1121", "Pope", 2500)
savings_account4 = SavingsAccount("1122", "Pope", 1250)

accounts_list = [account1, savings_account1, account2, savings_account2, account3, savings_account3, account4, savings_account4]

