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

food.withdraw(40)
food.transfer(clothing, 40)
print(food.get_balance())

print(food)
print(clothing)