# Exercício: Monte seu próprio algoritmo genético

- Definir codificação em cromossomos.
- Definir função de aptidão.
- Definir critério de parada.
- Executar pelo menos 2 rodadas (gerações).

## População inicial

| Indivíduo | Arma   | Transforma | Idade  | Classe |
| --------- | ------ | ---------- | ------ | ------ |
| p1        | lâmina | sim        | adulto | herói  |
| p2        | magia  | não        | novo   | herói  |
| p3        | magia  | sim        | velho  | vilão  |
| p4        | não    | não        | novo   | herói  |
| p5        | não    | não        | adulto | vilão  |

## Codificação (bits por cromossomo)

### Mapeamento e pontuação

Arma (2 bits):

- `00` = não -> +0
- `01` = lâmina -> +1
- `10` = magia -> +2
- `11` = lâmina e magia -> +3

Transforma (1 bit):

- `0` = não -> +0
- `1` = sim -> +1

Idade (2 bits):

- `00` = novo -> +2
- `01` = adulto -> +1
- `10` = velho -> +1

Classe (1 bit):

- `0` = vilão -> +1
- `1` = herói -> +2

## Cálculo de fitness (soma dos pontos)

| Indivíduo | Cromossomo | Fitness                 |
| --------- | ---------- | ----------------------- |
| p1        | 011011     | 1(01)+1(1)+1(01)+2(1)=5 |
| p2        | 100001     | 2(10)+0(0)+2(00)+2(1)=6 |
| p3        | 101100     | 2(10)+1(1)+1(10)+1(0)=5 |
| p4        | 000001     | 0(00)+0(0)+2(00)+2(1)=4 |
| p5        | 000010     | 0(00)+0(0)+1(01)+1(0)=2 |

Melhor fitness possível: 3(11)+1(1)+2(00)+2(1)=8

## Função de aptidão

f = fitness / 8

## Critério de parada

- Parar após 2 gerações
