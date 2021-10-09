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
    # total é o total de saques em todas as categorias (*args) passadas
    # total_list é o conjunto do total de saques em cada categoria

    # este primeiro bloco faz uma interface com Budget
    total = 0
    total_list = []
    for i in args:
        total += i.get_total_withdrawals
        total_list.append(i.get_total_withdrawals)


    # aqui é calculada a proporção dos saques de cada categoria relativamente ao total de saques
    percentage_list = []
    for i in total_list:
        percentage_list.append(10 * (i / total))


print('||||||||||||||||||||||||||||||||||||||||||||||')

print(food.get_total_withdrawals())
print(clothing.get_total_withdrawals())