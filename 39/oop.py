#Exercise 1

class Bank:
    def __init__(self, *args):
        self.accounts = list(args)

    def addAccount(self, account):
        self.accounts.append(account)

    def __str__(self):
        return '# of accounts: ' + str(len(self.accounts))

class Account:
    def __init__(self, customer, balance):
        self.customer = customer
        self.balance = balance

    def __str__(self):
        return 'Customer: ' + self.customer.name + ', balance: ' + str(self.balance)

class Customer:
    def __init__(self, name, age, creditScore):
        self.name = name
        self.age = age
        self.creditScore = creditScore

    def __str__(self):
        return 'Name: 📱' + self.name + ', age: ' + str(self.age) + ', credit score: ' + str(self.creditScore)

#Start data
billy = Customer('Billy', 45, 0)
bobby = Customer('Bobby', 12, 500)

billy_account = Account(billy, 400)
bobby_account = Account(bobby, 500)

bank = Bank(billy_account, bobby_account)

#bank.addAccount(billy_account)
