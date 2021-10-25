from prob_calculator import Hat, experiment

hat = Hat(blue=3,red=2,green=6)






teste = experiment(hat=hat,
                   expected_balls={"blue":2,"green":1},
                   num_balls_drawn=4,
                   num_experiments=1000)
print(teste)

