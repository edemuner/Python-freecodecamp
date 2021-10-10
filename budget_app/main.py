import math

from budget import Category

food = Category("Food")
clothing = Category("Clothing")


food.deposit(100, 'deposito inicial')
clothing.deposit(100, 'o primeiro depósito realizado na categoria clothing')

food.withdraw(30, 'compras no supermercado')

food.transfer(clothing, 50)
clothing.transfer(food, 10)

print(food.get_balance())
print(clothing.get_balance())

# este bloco de teste causou confusão, as transações abaixo não são concretizadas
# por falta de saldo
food.withdraw(30)
food.transfer(clothing, 40)
print(food.get_balance())

print(food)
print(clothing)



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

    print(chart_drawer(names_and_percentages))


def chart_drawer(names_and_percentages):
    columns = len(names_and_percentages)
    values_for_balls = list(names_and_percentages.values())


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
                   f"    {columns * '---'}-"



    return chart_string



print('||||||||||||||||||||||||||||||||||||||||||||||')



create_spend_chart(food, clothing)