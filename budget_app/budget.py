class Category:

    # essa classe cria categorias de orçamento (food, clothing, etc)
    # os objetos recebem transações financeiras e registram em ledger

    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=''):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({"amount": - amount, "description": description})

    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += item["amount"]
        return balance

    def get_total_withdrawals(self):
        total = 0
        for item in self.ledger:
            int_amount = int(item["amount"])
            if int_amount < 0:
                total += int_amount
        return total

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

    @staticmethod
    def create_spend_chart(*args):

        # este primeiro bloco coleta os totais
        total = 0
        for i in args:
            total += i.get_total_withdrawals()

        # aqui são gerados dicionários com os nome das categorias como keys
        # e os values são as proporções de cada categoria diante do total de saques
        # numa proporção de 0 a 10
        names_and_percentages = {}
        for i in args:
            names_and_percentages[i.name] = round(10 * (i.get_total_withdrawals() / total))

        return Category.chart_drawer(names_and_percentages)


    # este método desenha a tabela, para isso o desenho do "esqueleto" é feito na própria função
    # enquanto as linhas individuais são feitas pelo balls_drawer()
    @staticmethod
    def chart_drawer(names_and_percentages):
        columns = len(names_and_percentages)
        values_for_balls = list(names_and_percentages.values())

        # esta função foi definida aqui dentro, para usar o namespace de chart_drawer()
        # pois a cada vez q a função é chamada (em cada linha), os valores são modificados
        # para que ela desenhe "o" ou " " quando for necessário em cada caso
        def balls_drawer():
            balls_line = ""
            for i in range(columns):
                if values_for_balls[i] < 10:
                    balls_line += "   "
                    values_for_balls[i] += 1
                else:
                    balls_line += " o "
            return balls_line

        chart_string = "Percentage spent by category\n" \
                       f"100|{balls_drawer()}\n" \
                       f" 90|{balls_drawer()}\n" \
                       f" 80|{balls_drawer()}\n" \
                       f" 70|{balls_drawer()}\n" \
                       f" 60|{balls_drawer()}\n" \
                       f" 50|{balls_drawer()}\n" \
                       f" 40|{balls_drawer()}\n" \
                       f" 30|{balls_drawer()}\n" \
                       f" 20|{balls_drawer()}\n" \
                       f" 10|{balls_drawer()}\n" \
                       f"  0|{columns * ' o '}\n" \
                       f"    {columns * '---'}-\n"
        chart_string += Category.columns_drawer(list(names_and_percentages.keys()))

        return chart_string

    @staticmethod
    def columns_drawer(names):
        rows = len(max(names, key=len))
        columns_string = ""
        print(names)
        for i in range(rows):
            for j in range(len(names)):
                if j == 0:
                    columns_string += "    "
                if i < len(names[j]):
                    columns_string += " " + names[j][i] + " "
                else:
                    columns_string += "   "
            columns_string += "\n"
        return columns_string