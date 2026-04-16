# Alguns tipos de algoritmos de aprendizado de máquina

- Classificação - determinar a classe
- Agrupamento - determinar grupos
- Regressão - previsão (geralmente têm um fator temporal, ver no passado pra prever o futuro)
- Associação - associa elementos com atributos relacionados probabilisticamente

## Árvores de Decisão - Classificação

Uma árvore de decisão é uma estrutura na qual cada nó interno corresponde a um
teste em um atributo, cada ramificação representa a saída de um teste, e cada
nó folha representa um rótulo de classe.

## Algoritmo ID3 (Iterative Dichotomiser 3) - usado para construir árvores de decisão

1. Cálculo da Entropia do Conjunto ($S$):
   - Meça o nível de desordem ou incerteza do dataset atual em relação à classe alvo.
   - Utilize a fórmula: $H(S) = - \sum p_i \log_2(p_i)$.

2. Cálculo do Ganho de Informação ($G$) para cada Atributo:
   - Para cada atributo disponível, calcule a entropia média ponderada de suas divisões.
   - O Ganho é a diferença: $G(S, A) = H(S) - \sum \frac{|S_v|}{|S|} H(S_v)$.
   - Objetivo: Identificar qual atributo reduz mais a incerteza.

3. Seleção do Nó de Decisão:
   - Escolha o atributo com o maior Ganho de Informação.
   - Este atributo torna-se o nó raiz (ou o nó atual da subárvore).

4. Particionamento dos Dados:
   - Divida o conjunto de dados original em subconjuntos, onde cada subconjunto contém apenas exemplos que possuem um valor específico do atributo selecionado.

5. Avaliação de Parada (Condições de Base) para cada Subconjunto:
   - Caso 1: Se todos os exemplos pertencem à mesma classe, crie um nó folha com o nome dessa classe.
   - Caso 2: Se não restarem mais atributos para dividir, mas ainda houver classes mistas, crie uma folha com a classe majoritária.
   - Caso 3: Se o subconjunto estiver vazio, crie uma folha com a classe majoritária do nó pai.

6. Recursão:
   - Se nenhuma das condições de parada for atendida, repita o processo a partir do Passo 1 para o subconjunto de dados, ignorando os atributos que já foram utilizados nos níveis superiores da árvore.

### Exemplo

Conjunto de dados Weather (Witten and Frank, 2005):

| Outlook  | Temp | Humidity | Windy | Play? |
| -------- | ---- | -------- | ----- | ----- |
| Sunny    | Hot  | High     | False | No    |
| Sunny    | Hot  | High     | True  | No    |
| Overcast | Hot  | High     | False | Yes   |
| Rainy    | Mild | High     | False | Yes   |
| Rainy    | Cool | Normal   | False | Yes   |
| Rainy    | Cool | Normal   | True  | No    |
| Overcast | Cool | Normal   | True  | Yes   |
| Sunny    | Mild | High     | False | No    |
| Sunny    | Cool | Normal   | False | Yes   |
| Rainy    | Mild | Normal   | False | Yes   |
| Sunny    | Mild | Normal   | True  | Yes   |
| Overcast | Mild | High     | True  | Yes   |
| Overcast | Hot  | Normal   | False | Yes   |
| Rainy    | Mild | High     | True  | No    |

Total de dados: 14

- Classe Yes: 9/14
- Classe No: 5/14

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px;">

|          | Outlook |     |
| -------- | ------- | --- |
|          | Yes     | No  |
| Sunny    | 2       | 3   |
| Overcast | 4       | 0   |
| Rainy    | 3       | 2   |

|      | Temp |     |
| ---- | ---- | --- |
|      | Yes  | No  |
| Hot  | 2    | 2   |
| Mild | 4    | 2   |
| Cool | 3    | 1   |

|        | Humidity |     |
| ------ | -------- | --- |
|        | Yes      | No  |
| High   | 3        | 4   |
| Normal | 6        | 1   |

|       | Windy |     |
| ----- | ----- | --- |
|       | Yes   | No  |
| False | 6     | 2   |
| True  | 3     | 3   |

</div>

### Cálculos da Iteração 1 (Escolha do Nó Raiz)

Entropia total do conjunto $S$:
$$H(S) = -\left(\frac{9}{14} \log_2\left(\frac{9}{14}\right) + \frac{5}{14} \log_2\left(\frac{5}{14}\right)\right) \approx 0,940$$

---

#### Atributo: Outlook

$$H(Sunny) = -\left(\frac{2}{5} \log_2\left(\frac{2}{5}\right) + \frac{3}{5} \log_2\left(\frac{3}{5}\right)\right) \approx 0,971$$

$$H(Overcast) = -\left(\frac{4}{4} \log_2\left(\frac{4}{4}\right) + 0\right) = 0$$

$$H(Rainy) = -\left(\frac{3}{5} \log_2\left(\frac{3}{5}\right) + \frac{2}{5} \log_2\left(\frac{2}{5}\right)\right) \approx 0,971$$

Ganho de Informação:
$$G(S, Outlook) = H(S) - \left( \frac{5}{14}(0,971) + \frac{4}{14}(0) + \frac{5}{14}(0,971) \right)$$

$$G(S, Outlook) = 0,940 - 0,693 = \mathbf{0,247}$$

---

#### Atributo: Temp

$$H(Hot) = -\left(\frac{2}{4} \log_2\left(\frac{2}{4}\right) + \frac{2}{4} \log_2\left(\frac{2}{4}\right)\right) = 1,0$$

$$H(Mild) = -\left(\frac{4}{6} \log_2\left(\frac{4}{6}\right) + \frac{2}{6} \log_2\left(\frac{2}{6}\right)\right) \approx 0,918$$

$$H(Cool) = -\left(\frac{3}{4} \log_2\left(\frac{3}{4}\right) + \frac{1}{4} \log_2\left(\frac{1}{4}\right)\right) \approx 0,811$$

Ganho de Informação:
$$G(S, Temp) = H(S) - \left( \frac{4}{14}(1,0) + \frac{6}{14}(0,918) + \frac{4}{14}(0,811) \right)$$

$$G(S, Temp) = 0,940 - 0,911 = \mathbf{0,029}$$

---

#### Atributo: Humidity

$$H(High) = -\left(\frac{3}{7} \log_2\left(\frac{3}{7}\right) + \frac{4}{7} \log_2\left(\frac{4}{7}\right)\right) \approx 0,985$$

$$H(Normal) = -\left(\frac{6}{7} \log_2\left(\frac{6}{7}\right) + \frac{1}{7} \log_2\left(\frac{1}{7}\right)\right) \approx 0,592$$

Ganho de Informação:
$$G(S, Humidity) = H(S) - \left( \frac{7}{14}(0,985) + \frac{7}{14}(0,592) \right)$$

$$G(S, Humidity) = 0,940 - 0,788 = \mathbf{0,152}$$

---

#### Atributo: Windy

$$H(False) = -\left(\frac{6}{8} \log_2\left(\frac{6}{8}\right) + \frac{2}{8} \log_2\left(\frac{2}{8}\right)\right) \approx 0,811$$

$$H(True) = -\left(\frac{3}{6} \log_2\left(\frac{3}{6}\right) + \frac{3}{6} \log_2\left(\frac{3}{6}\right)\right) = 1,0$$

Ganho de Informação:
$$G(S, Windy) = H(S) - \left( \frac{8}{14}(0,811) + \frac{6}{14}(1,0) \right)$$

$$G(S, Windy) = 0,940 - 0,892 = \mathbf{0,048}$$

---

### Conclusões

#### Conclusão da Iteração 1

Comparando os ganhos de informação:

- $G(S, Outlook) = 0,247$
- $G(S, Humidity) = 0,152$
- $G(S, Windy) = 0,048$
- $G(S, Temp) = 0,029$

O atributo **Outlook** possui o maior Ganho de Informação e, portanto, é selecionado como o **nó raiz** da árvore de decisão. O particionamento dos dados continuará recursivamente para cada ramo de Outlook (Sunny, Overcast, Rainy).

- **Overcast** → Resulta em entropia 0 (4 Yes, 0 No), tornando-se diretamente um **Nó Folha: Yes**.

---

#### Iteração 2: Subconjunto `Sunny`

Filtrando os dados onde `Outlook = Sunny`, temos 5 instâncias:

- Classe Yes: 2/5
- Classe No: 3/5
$$H(Sunny) = 0,971$$

Calculando o Ganho de Informação para os atributos restantes (`Temp`, `Humidity`, `Windy`) neste subconjunto, o atributo **Humidity** fornece a separação perfeita:

- **High**: 3 instâncias (0 Yes, 3 No) $\rightarrow$ Entropia = 0. **Nó Folha: No**
- **Normal**: 2 instâncias (2 Yes, 0 No) $\rightarrow$ Entropia = 0. **Nó Folha: Yes**
- $G(Sunny, Humidity) = 0,971 - 0 = \mathbf{0,971}$. (Vencedor para este ramo).

---

#### Iteração 3: Subconjunto `Rainy`

Filtrando os dados onde `Outlook = Rainy`, temos 5 instâncias:

- Classe Yes: 3/5
- Classe No: 2/5
$$H(Rainy) = 0,971$$

Calculando o Ganho de Informação para os atributos restantes (`Temp`, `Humidity`, `Windy`) neste subconjunto, o atributo **Windy** fornece a separação perfeita:

- **False**: 3 instâncias (3 Yes, 0 No) $\rightarrow$ Entropia = 0. **Nó Folha: Yes**
- **True**: 2 instâncias (0 Yes, 2 No) $\rightarrow$ Entropia = 0. **Nó Folha: No**
- $G(Rainy, Windy) = 0,971 - 0 = \mathbf{0,971}$. (Vencedor para este ramo).

---

#### Árvore de Decisão Final

```plaintext
Outlook
├── Overcast: Yes
├── Sunny
│   └── Humidity
│       ├── High: No
│       └── Normal: Yes
└── Rainy
    └── Windy
        ├── False: Yes
        └── True: No
```
