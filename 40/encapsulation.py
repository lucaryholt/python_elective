# Ex 1

class Car:
    def __init__(self, make, model, bhp, mph):
        self.make = make
        self.model = model
        self.bhp = bhp
        self.mph = mph

    @property
    def make(self):
        return self.__make

    @property
    def model(self):
        return self.__model

    @property
    def bhp(self):
        return self.__bhp

    @property
    def mph(self):
        return self.__mph

    @make.setter
    def make(self, make):
        self.__make = make

    @model.setter
    def model(self, model):
        self.__model = model

    @bhp.setter
    def bhp(self, bhp):
        self.__bhp = bhp

    @mph.setter
    def mph(self, mph):
        self.__mph = mph

# Ex 2

class Bank:
    def __init__(self):
        self.__accounts = []

    @property
    def accounts(self):
        return self.__accounts

    @accounts.setter
    def accounts(self, accounts):
        self.__accounts = accounts

    def addAccount(self, account):
        self.accounts.append(account)

    def __str__(self):
        return '# of accounts: ' + str(len(self.accounts))

class Account:
    def __init__(self, customer, balance):
        self.customer = customer
        self.balance = balance

    @property
    def customer(self):
        return self.__customer

    @property
    def balance(self):
        return self.__balance

    @customer.setter
    def customer(self, customer):
        self.__customer = customer

    @balance.setter
    def balance(self, balance):
        self.__balance = balance

    def __str__(self):
        return 'Customer: ' + self.customer.name + ', balance: ' + str(self.balance)

class Customer:
    def __init__(self, name, age, creditScore):
        self.name = name
        self.age = age
        self.creditScore = creditScore

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @property
    def creditScore(self):
        return self.__creditScore

    @name.setter
    def name(self, name):
        self.__name = name

    @age.setter
    def age(self, age):
        self.__age = age

    @creditScore.setter
    def creditScore(self, creditScore):
        self.__creditScore = creditScore

    def __str__(self):
        return 'Name: 📱' + self.name + ', age: ' + str(self.age) + ', credit score: ' + str(self.creditScore)
'''
#Start data
billy = Customer('Billy', 45, 0)
bobby = Customer('Bobby', 12, 500)

billy_account = Account(billy, 400)
bobby_account = Account(bobby, 500)

bank = Bank()
'''

# Ex 3

class Machine:
    def __init__(self):
        self.status = False

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        self.__status = status

    def changeState(self):
        self.__status = not self.__status

class Printer(Machine):
    def __init__(self, papertray):
        self.papertray = papertray

    @property
    def papertray(self):
        return self.__papertray

    @papertray.setter
    def papertray(self, papertray):
        self.__papertray = papertray

    def print(self, text):
        if self.papertray.nrOfPapers != 0:
            self.papertray.usePaper()
            print(text)
        else:
            print('not enough paper')

class Papertray:
    def __init__(self):
        self.nrOfPapers = 10

    @property
    def nrOfPapers(self):
        return self.__nrOfPapers

    @nrOfPapers.setter
    def nrOfPapers(self, nrOfPapers):
        self.__nrOfPapers = nrOfPapers

    def usePaper(self):
        self.__nrOfPapers -= 1

    def addPaper(self, papers):
        self.__nrOfPapers = self.nrOfPapers + papers
