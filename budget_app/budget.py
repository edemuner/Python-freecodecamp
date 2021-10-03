class Category:

    name = ''
    ledger = []

    def __init__(self, name):
        self.name = name

    def deposit(self, amount, description=''):
            self.ledger.append( {"amount": amount, "description":description} )

    def withdraw(self, amount, description=''):
        self.ledger.append( {"amount": - amount, "description": description} )

    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += item["amount"]
        return balance



