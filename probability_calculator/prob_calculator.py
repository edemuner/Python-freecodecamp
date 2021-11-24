import random
import copy

class Hat:

    
    def __init__(self, **kwargs):
        # insere as cores na lista contents, pela quantidade de vezes que for passado quando instanciado
        self.contents = []
        for i, j in kwargs.items():
            for l in range(j):
                self.contents.append(i)


    def draw(self, number):
        # caso a quantidade de bolas removidas não seja menor que o total de bolas
        # ele esvazia o atributo contents e retorna um objeto-cópia (cópia profunda) da lista de contents
        if number >= len(self.contents):
            temp_contents = copy.deepcopy(self.contents)
            self.contents.clear()
            return temp_contents
        # se number for menor que contents, a quantidade passada é selecionada aleatoriamente
        # as bolas selecionadas são guardadas, removidas do chapéu, e retornadas
        else:
            selected = random.sample(self.contents, number)
            for i in selected:
                self.contents.remove(i)
            return selected

# é uma função que trabalha com o objeto hat
# expected_balls é a especificação de uma combinação de cores e quantidades que se quer extrair, p.e. {"blue":2, "red":1} 
# num_balls_drawn é o número de bolas retiradas, passada ao chamar o método draw()
# num_experiments é a quantidade de vezes que tudo isso acima é feito, a probabilidade é calculada com base nesse número
def experiment(hat,
               expected_balls,
               num_balls_drawn,
               num_experiments):
    times = 0  # ocorrências da combinação testada

    for exp in range(num_experiments):

        temp = hat.draw(num_balls_drawn)  # lista com as bolas retiradas em cada experimento 
        match = 0  # número de vezes que a quantidade de cores retiradas foi maior que o número de cores esperada

        for ball, number in expected_balls.items():

            # se a quantidade de bolas na lista retornada em draw() for >= que o esperado, soma 1 match
            if temp.count(ball) >= number:
                match += 1
        # se der match em todos os elementos de expected_balls, é uma ocorrência que entra na estatística
        if match == len(expected_balls):
            times += 1
        
        # ao fim de cada laço, as bolas são devolvidas ao chapéu
        hat.contents += temp
        
        # o cálculo da estatística: número de ocorrência / número de experimentos
    return times / num_experiments
