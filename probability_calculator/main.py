from prob_calculator import Hat, experiment

hat = Hat(yellow=5,red=1,green=3,blue=9,test=1)






teste = experiment(hat=hat,
                   expected_balls={"yellow":2,"blue":3,"test":1},
                   num_balls_drawn=20,
                   num_experiments=100)
print(teste)

