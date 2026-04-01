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


def torneio(populacao):
    ganhador = random.sample(populacao, 2)
    if ganhador[0][2] < ganhador[1][2]:
        return ganhador[0]
    else:
        return ganhador[1]


def elitismo(populacao):
    return min(populacao, key=lambda x: x[2])


nova_populacao = []
pop_atual = primeira_pop

for g in range(num_repeticoes):
    nova_populacao = []

    melhor_ind = elitismo(pop_atual)
    nova_populacao.append(melhor_ind)

    for i in range(tam_populacao - 1):
        pai_1 = torneio(pop_atual)
        pai_2 = torneio(pop_atual)

        filho = [(pai_1[0] + pai_2[0]) / 2, (pai_1[1] + pai_2[1]) / 2, 0]

        if random.random() < taxa_mutacao:
            filho[0] += random.uniform(-0.5, 0.5)
            filho[1] += random.uniform(-0.5, 0.5)
        nova_populacao.append(filho)

    for individuo in nova_populacao:
        if individuo[2] == 0:
            individuo[2] = fitness(individuo[0], individuo[1])
            num_avaliacoes += 1

    pop_atual = nova_populacao
