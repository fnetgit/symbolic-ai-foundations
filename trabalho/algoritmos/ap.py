import random

num_avaliacoes = 0
taxa_sucesso = 0

num_repeticoes = 100


def fitness(x, y):
    return 0.25 * x**4 - 0.5 * x**2 + 0.1 * x + 0.5 * y**2

# criando primeira pop
tam_populacao = 50
primeira_pop = []
for i in range(tam_populacao):
    cromossomo = [random.uniform(-10, 10), random.uniform(-10, 10), 0]
    primeira_pop.append(cromossomo)

# avaliando
for individuo in primeira_pop:
    individuo[2] = fitness(individuo[0], individuo[1])
    num_avaliacoes += 1

def torneio(lista):
    ...