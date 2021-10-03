class Category:

    # essa classe cria categorias de orçamento (food, clothing, etc)
    # os objetos recebem transações financeiras e registram em ledger


    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=''):
        self.ledger.append( {"amount": amount, "description":description} )

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append( {"amount": - amount, "description": description} )

    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += item["amount"]
        return balance

    # esses 2 primeiros métodos realizam um depósito ou saque, get_balance retorna o saldo


    # transfer realiza transferências entre diferentes objetos
    def transfer(self, category, amount):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {category.name}')
            category.deposit(amount, f'Transfer from {self.name}')
            return True
        else:
            return False

    # esse método verifica se o saldo é suficiente, é usado em transfer e withdraw
    def check_funds(self, amount):
        return self.get_balance() > amount

    def __str__(self):
        columnspam = 30
        fstr = ''
        fstr += self.name.center(30, '*') + '\n'
        for item in self.ledger:
            fstr += f'{item["description"][:24] : <23}'
            fstr += f'{item["amount"] : >7}' + '\n'

        return fstr
