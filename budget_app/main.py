from budget import Category

food = Category("food")

food.deposit(100)
food.deposit(200)
food.deposit(50)

food.withdraw(30)
food.withdraw(20)

print(food.get_balance())