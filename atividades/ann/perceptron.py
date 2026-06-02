import os

import numpy as np

TAXA_APRENDIZADO = 0.01
MAX_EPOCAS = 1000

caminho_arquivo = os.path.join(os.path.dirname(__file__), "dados-de-treinamento.txt")
conjunto_dados = np.loadtxt(caminho_arquivo, skiprows=1, dtype=float)

entradas_brutas = conjunto_dados[:, :3]
coluna_bias = np.full((entradas_brutas.shape[0], 1), -1.0)
entradas_treino = np.hstack((coluna_bias, entradas_brutas))
alvos_treino = conjunto_dados[:, -1]


def treinar_preceptron(entradas: np.ndarray, alvos: np.ndarray):
    pesos = np.random.rand(4)
    pesos_iniciais = pesos.copy()

    epocas = 0
    tem_erro = True

    while tem_erro and epocas < MAX_EPOCAS:
        tem_erro = False

        for i in range(len(entradas)):
            ativacao = np.dot(entradas[i], pesos)
            previsao = 1.0 if ativacao >= 0 else -1.0

            if previsao != alvos[i]:
                pesos += TAXA_APRENDIZADO * alvos[i] * entradas[i]
                tem_erro = True

        epocas += 1

    return pesos_iniciais, pesos, epocas


lista_pesos_treinados = []

print("\n" + "=" * 115)
print(" TABELA 1: RESULTADOS DOS TREINAMENTOS")
print("=" * 115)
print(
    f"{'Treino':<7} | {'W0 Ini':<8} | {'W1 Ini':<8} | {'W2 Ini':<8} | {'W3 Ini':<8} | {'W0 Fin':<8} | {'W1 Fin':<8} | {'W2 Fin':<8} | {'W3 Fin':<8} | {'Épocas'}"
)
print("-" * 115)

for treino_idx in range(1, 6):
    pesos_ini, pesos_fin, num_epocas = treinar_preceptron(
        entradas_treino, alvos_treino
    )
    lista_pesos_treinados.append(pesos_fin.copy())

    print(
        f"T{treino_idx:<6} | {pesos_ini[0]:8.4f} | {pesos_ini[1]:8.4f} | {pesos_ini[2]:8.4f} | {pesos_ini[3]:8.4f} | "
        f"{pesos_fin[0]:8.4f} | {pesos_fin[1]:8.4f} | {pesos_fin[2]:8.4f} | {pesos_fin[3]:8.4f} | {num_epocas}"
    )

amostras_teste_brutas = np.array(
    [
        [-0.3665, 0.0620, 5.9891],
        [-0.7842, 1.1267, 5.5912],
        [0.3012, 0.5611, 5.8234],
        [0.7757, 1.0648, 8.0677],
        [0.1570, 0.8028, 6.3040],
        [-0.7014, 1.0316, 3.6005],
        [0.3748, 0.1536, 6.1537],
        [-0.6920, 0.9404, 4.4058],
        [-1.3970, 0.7141, 4.9263],
        [-1.8842, -0.2805, 1.2548],
    ]
)

bias_teste = np.full((amostras_teste_brutas.shape[0], 1), -1.0)
entradas_teste = np.hstack((bias_teste, amostras_teste_brutas))

print("\n\n" + "=" * 48)
print(" TABELA 2: CLASSIFICAÇÃO DAS NOVAS AMOSTRAS")
print("=" * 48)
print(f"{'Amostra':<7} | {'T1':<4} | {'T2':<4} | {'T3':<4} | {'T4':<4} | {'T5':<4}")
print("-" * 48)

for i in range(len(entradas_teste)):
    resultados_linha = []

    for pesos in lista_pesos_treinados:
        ativacao = np.dot(entradas_teste[i], pesos)
        classe_prevista = "P1" if ativacao >= 0 else "P2"
        resultados_linha.append(classe_prevista)

    print(
        f"{i + 1:02d}      | {resultados_linha[0]:<4} | {resultados_linha[1]:<4} | "
        f"{resultados_linha[2]:<4} | {resultados_linha[3]:<4} | {resultados_linha[4]:<4}"
    )
print("=" * 48 + "\n")
