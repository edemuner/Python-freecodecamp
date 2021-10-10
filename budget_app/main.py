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
    chart_string = "Percentage spent by category\n" \
                   "100|\n" \
                   " 90|\n" \
                   " 80|\n" \
                   " 70|\n" \
                   " 60|\n" \
                   " 50|\n" \
                   " 40|\n" \
                   " 30|\n" \
                   " 20|\n" \
                   " 10|\n" \
                   f"  0|{columns * ' o '}\n" \
                   f"    {columns * '---'}-"
    return chart_string


print('||||||||||||||||||||||||||||||||||||||||||||||')



create_spend_chart(food, clothing)