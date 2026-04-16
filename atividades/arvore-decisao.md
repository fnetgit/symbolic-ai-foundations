# Desafio

Construir a árvore de decisão para os dados a
seguir. Deseja-se saber se o time F irá ganhar
considerando as condições da partida

| Time      | Match type | Court surface | Best effort | Outcome |
| --------- | ---------- | ------------- | ----------- | ------- |
| Morning   | Master     | Grass         | 1           | F       |
| Afternoon | Grand slam | Clay          | 1           | F       |
| Night     | Friendly   | Hard          | 0           | F       |
| Afternoon | Friendly   | Mixed         | 0           | N       |
| Afternoon | Master     | Clay          | 1           | N       |
| Afternoon | Grand slam | Grass         | 1           | F       |
| Afternoon | Grand slam | Hard          | 1           | F       |
| Afternoon | Grand slam | Hard          | 1           | F       |
| Morning   | Master     | Grass         | 1           | F       |
| Afternoon | Grand slam | Clay          | 1           | N       |
| Night     | Friendly   | Hard          | 0           | F       |
| Night     | Master     | Mixed         | 1           | N       |
| Afternoon | Master     | Clay          | 1           | N       |
| Afternoon | Master     | Grass         | 1           | F       |
| Afternoon | Grand slam | Hard          | 1           | F       |
| Afternoon | Grand slam | Clay          | 1           | F       |

## Solução

### Dados da classe

|     | Outcome |     |
| --- | ------- | --- |
|     | F       | N   |
|     | 11      | 5   |

#### Separando os dados por atributos

|           | Time |     |
| --------- | ---- | --- |
|           | F    | N   |
| Morning   | 2    | 0   |
| Afternoon | 7    | 4   |
| Night     | 2    | 1   |

|            | Match type |     |
| ---------- | ---------- | --- |
|            | F          | N   |
| Master     | 3          | 3   |
| Grand slam | 6          | 1   |
| Friendly   | 2          | 1   |

|       | Court surface |     |
| ----- | ------------- | --- |
|       | F             | N   |
| Grass | 4             | 0   |
| Clay  | 2             | 3   |
| Hard  | 5             | 0   |
| Mixed | 0             | 2   |

|     | Best effort |     |
| --- | ----------- | --- |
|     | F           | N   |
| 0   | 2           | 1   |
| 1   | 9           | 4   |

#### info do outcome

$$info = (11,5)$$

$$info(Outcome) = -11/16*log2(11/16) - 5/16*log2(5/16) = 0,896$$

#### Info do time

$$info = (2,0)(7,4)(2,1)$$

$$info(Time) = 2/16 *info[2,0] + 11/16* info[7,4] + 3/16 * info[2,1]$$
descomposto em: $\downarrow$

$$info[2,0] = -2/2 *log2(2/2) - 0/2* log2(0/2) = 0$$

$$info[7,4] = -7/11 *log2(7/11) - 4/11* log2(4/11) = 0,946$$

$$info[2,1] = -2/3 *log2(2/3) - 1/3* log2(1/3) = 0,918$$

$$expected information = 2/16 *0 + 11/16* 0,946 + 3/16 *0,918$$

$$ei = 0 + 0,687 * 0,946 + 0,187 * 0,918 = 0,821$$

---

#### info do match type

$$info = (3,3)(6,1)(2,1)$$

$$info(mt) = 6/16*info[3,3] + 7/16*info[6,1] + 3/16*info[2,1]$$
descomposto em: $\downarrow$

$$info[3,3] = -3/6*log2(3/6) - 3/6*log2(3/6) = 1$$

$$info[6,1] = -6/7*log2(6/7) - 1/7*log2(1/7) = 0,592$$

$$info[2,1] = -2/3*log2(2/3) - 1/3*log2(1/3) = 0,918$$

$$expected information = 6/16 * 1 + 7/16 * 0,592 + 3/16 * 0,918 = 0,61$$

$$ei = 0.375 + 0.259 + 0.172 = \mathbf{0.806}$$

---

#### info do court surface

$$info = (4,0)(2,3)(5,0)(0,2)$$

$$
\begin{aligned}
info(cs) &= 4/16 * info[4,0] + 5/16 * info[2,3] \\
 &\quad + 5/16 * info[5,0] + 2/16 * info[0,2]
\end{aligned}
$$

descomposto em: $\downarrow$

$$info[4,0]= -4/4*log2(4/4) - 0/4*log2(0/4) = 0$$

$$info[2,3] = -2/5*log2(2/5) - 3/5*log2(3/5) = 0,971$$

$$info[5,0] = -5/5*log2(5/5) - 0/5*log2(0/5) = 0 $$

$$info[0,2] = -0/2*log2(0/2) - 2/2*log2(2/2) = 0$$

$$ei = 4/16 * 0 + 5/16 * 0,971 + 5/16 * 0$$

$$ei = 0 + 0,302 + 0 = 0,302$$

#### info do best effort

$$info= (2,1)(9,4)$$

$$info(be)= 3/16 * info[2,1] + 13/16 * info[9,4]$$

$$
\begin{aligned}
info(0)= -2/3*log2(2/3) - 1/3*log2(1/3) = \\
-0.666* (-0,586) - 0.333* (-1,586) = 0,918
\end{aligned}
$$

$$info(1)= -9/13*log2(9/13) - 4/13*log2(4/13) = 0.891$$

$$ ei = 3/16 * 0,918 + 13/16 * (0,891)$$

$$ ei = 0.172 + 0.724 = 0.896$$

### Ganho de Informação

Outcome: 0,896

* Gt: $0,896 - 0,822 = 0,074$
* Gmt: $0,896 - 0,806 = 0,090$
* Gc: $0,896 - 0,303 = 0,593$
* Gb: $0,896 - 0,896 = 0,000$

Nó raíz = Court surface (Maior Ganho de Informação)

---

### Primeira Ramificação: Court surface

Analisando os *subsets* gerados pelo Nó raíz:

* **Grass**: 4 instâncias (`F`, `F`, `F`, `F`) $\rightarrow$ Entropia = 0. **Nó Folha: F**
* **Hard**: 5 instâncias (`F`, `F`, `F`, `F`, `F`) $\rightarrow$ Entropia = 0. **Nó Folha: F**
* **Mixed**: 2 instâncias (`N`, `N`) $\rightarrow$ Entropia = 0. **Nó Folha: N**
* **Clay**: 5 instâncias (`F`, `N`, `N`, `N`, `F`) $\rightarrow$ Entropia > 0. **Requer nova ramificação.**

---

### Segunda Ramificação: Subset Clay

Dados filtrados onde `Court surface` = `Clay`:

| Time      | Match type | Best effort | Outcome |
| :-------- | :--------- | :---------- | :------ |
| Afternoon | Grand slam | 1           | F       |
| Afternoon | Master     | 1           | N       |
| Afternoon | Grand slam | 1           | N       |
| Afternoon | Master     | 1           | N       |
| Afternoon | Grand slam | 1           | F       |

**Análise de variância dos atributos restantes neste subset:**

* Time: Apenas o valor 'Afternoon'. (Information Gain = 0)
* Best effort: Apenas o valor '1'. (Information Gain = 0)
* Match type: Valores 'Grand slam' e 'Master'. (Único atributo elegível para a ramificação).

Separando o nó `Clay` por `Match type`:

* **Master**: 2 instâncias (`N`, `N`) $\rightarrow$ Entropia = 0. **Nó Folha: N**
* **Grand slam**: 3 instâncias (`F`, `N`, `F`) $\rightarrow$ Entropia > 0.

#### Esgotamento de Atributos e Majority Vote

No nó `Clay` $\rightarrow$ `Grand slam`, ainda há impureza da classe alvo (2 instâncias `F` e 1 instância `N`). No entanto, todos os atributos preditivos do *dataset* (`Time`, `Match type`, `Court surface`, `Best effort`) já foram utilizados ou não possuem mais variância nesta ramificação. A árvore não pode crescer mais.

Aplicando o algoritmo de Voto Majoritário para resolver a colisão determinística e forçar o nó folha:

* Contagem: F = 2, N = 1.
* Nó Folha: F

---

### Árvore de Decisão Final

```plaintext
Court surface
├── Grass: F
├── Hard: F
├── Mixed: N
└── Clay
    ├── Master: N
    └── Grand slam: F
```
