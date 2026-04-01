import random

random.seed(24)

num_avaliacoes = 0
taxa_sucesso = 0

num_repeticoes = 100
taxa_mutacao = 0.1


def fitness(x, y):
    return 0.25 * x**4 - 0.5 * x**2 + 0.1 * x + 0.5 * y**2


# criando primeira pop
tam_populacao = 50
primeira_pop = []
for i in range(tam_populacao):
    cromossomo = [random.uniform(-10, 10), random.uniform(-10, 10), 0]
    primeira_pop.append(cromossomo)

# avaliando primeira pop
for individuo in primeira_pop:
    individuo[2] = fitness(individuo[0], individuo[1])
    num_avaliacoes += 1

print(primeira_pop[:2])


def torneio(populacao):
    ganhador = random.sample(populacao, 2)
    if ganhador[0][2] < ganhador[1][2]:
        return ganhador[0]
    else:
        return ganhador[1]


def elitismo(populacao):
    return min(populacao, key=lambda x: x[2])


nova_populacao = []
for i in range(tam_populacao):
    pai1 = torneio(primeira_pop)
    pai2 = torneio(primeira_pop)
    filho = [(pai1[0] + pai2[0]) / 2, (pai1[1] + pai2[1]) / 2, 0]
    nova_populacao.append(filho)
