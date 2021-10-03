from budget import Category

food = Category("Food")
clothing = Category("Clothing")


food.deposit(100)
clothing.deposit(100)

food.withdraw(30)

food.transfer(clothing, 50)
clothing.transfer(food, 10)

print(food.get_balance())
print(clothing.get_balance())

food.withdraw(40)
food.transfer(clothing, 40)
print(food.get_balance())