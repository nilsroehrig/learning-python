class Account:

    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, "r") as balance_file:
            self.balance = int(balance_file.read())

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def commit(self):
        with open(self.filepath, 'w') as balance_file:
            balance_file.write(str(self.balance))


class CheckingAccount(Account):
    type = "checking"

    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)
        self.fee = fee

    def transfer(self, amount):
        self.balance -= amount
        self.balance -= self.fee


jacks_account = CheckingAccount("jack.txt", 2)
gingers_account = CheckingAccount("ginger.txt", 1)

print(jacks_account.type)
print(gingers_account.type)
