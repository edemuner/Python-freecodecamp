import budget
from budget import Category
#
# food = Category("Food")
# clothing = Category("Clothing")
#
#
# food.deposit(100, 'deposito inicial')
# clothing.deposit(100, 'o primeiro depósito realizado na categoria clothing')
#
# food.withdraw(30, 'compras no supermercado')
#
# food.transfer(clothing, 50)
# clothing.transfer(food, 10)
#
# print(food.get_balance())
# print(clothing.get_balance())
#
# # este bloco de teste causou confusão, as transações abaixo não são concretizadas
# # por falta de saldo
# food.withdraw(30)
# food.transfer(clothing, 40)
# print(food.get_balance())
#
# print(food)
# print(clothing)
#
#
# print('||||||||||||||||||||||||||||||||||||||||||||||')
#
# food.deposit(1000)
# clothing.deposit(1000)
# food.withdraw(300)
# clothing.withdraw(150)
#
# car = Category("Car")
# car.deposit(1000)
# car.withdraw(500)
#
# print(car)
#
#
#
# print(Category.create_spend_chart(food, clothing, car))

food = Category('Food')
entertainment = Category('Entertainment')
business = Category('Business')

food.deposit(900, "deposit")
food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
food.transfer(20, entertainment)

print(food)