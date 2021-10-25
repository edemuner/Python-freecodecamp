from prob_calculator import Hat, experiment

hat = Hat(blue=2, red=4, yellow=6)

print(hat.contents)
print(hat.draw(6))




teste = experiment(hat,
           {'red': 2, 'yellow': 3, 'blue': 0},
           10,
           10)
print(teste)

