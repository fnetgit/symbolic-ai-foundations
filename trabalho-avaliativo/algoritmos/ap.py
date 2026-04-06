import random

NUM_AVALIACOES = 0
TAXA_SUCESSO = 0

NUM_REPETICOES = 100
NUM_GERACOES = 100
TAXA_MUTACAO = 0.2
TAM_POPULACAO = 70
NUM_COMPETIDORES = 4


def fitness(x, y):
    return 0.25 * x**4 - 0.5 * x**2 + 0.1 * x + 0.5 * y**2


def torneio(populacao):
    competidores = random.sample(populacao, NUM_COMPETIDORES)
    return min(competidores, key=lambda x: x[2])


def elitismo(populacao):
    return min(populacao, key=lambda x: x[2])


for r in range(NUM_REPETICOES):
    pop_atual = []
    parada_antecipada = False

    for i in range(TAM_POPULACAO):
        x, y = random.uniform(-10, 10), random.uniform(-10, 10)
        fit = fitness(x, y)
        pop_atual.append([x, y, fit])
        NUM_AVALIACOES += 1

    for g in range(NUM_GERACOES):
        nova_populacao = []
        melhor_da_gera = elitismo(pop_atual)

        if melhor_da_gera[2] <= -0.35:
            break

        nova_populacao.append(list(melhor_da_gera))

        while len(nova_populacao) < TAM_POPULACAO:
            pai_1 = torneio(pop_atual)
            pai_2 = torneio(pop_atual)

            filho_x = (pai_1[0] + pai_2[0]) / 2
            filho_y = (pai_1[1] + pai_2[1]) / 2

            if random.random() < TAXA_MUTACAO:
                filho_x += random.uniform(-0.5, 0.5)
                filho_y += random.uniform(-0.5, 0.5)

            filho_x = max(min(filho_x, 10), -10)
            filho_y = max(min(filho_y, 10), -10)

            fit_filho = fitness(filho_x, filho_y)
            NUM_AVALIACOES += 1
            nova_populacao.append([filho_x, filho_y, fit_filho])

            if fit_filho <= -0.35:
                parada_antecipada = True
                break

        pop_atual = nova_populacao
        if parada_antecipada:
            break

    melhor_final = elitismo(pop_atual)
    if melhor_final[2] <= -0.35:
        TAXA_SUCESSO += 1

print(f"Média de NFE: {NUM_AVALIACOES / NUM_REPETICOES:.0f}")
print(f"Taxa de Sucesso: {(TAXA_SUCESSO / NUM_REPETICOES) * 100:.0f}%")
print(f"Melhor fitness da última rodada: {melhor_final[2]:.3f}")
