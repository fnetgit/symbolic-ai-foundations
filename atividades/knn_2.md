# Atividade 2 KNN

## Tabela de dados relacionados a flor Iris

| ID  | SepalLength (cm) | SepalWidth (cm) | PetalLength (cm) | PetalWidth (cm) | Species         |
| --- | ---------------- | --------------- | ---------------- | --------------- | --------------- |
| 63  | 6                | 2,2             | 4                | 1               | Iris-versicolor |
| 105 | 6,5              | 3               | 5,8              | 2,2             | Iris-virginica  |
| 83  | 5,8              | 2,7             | 3,9              | 1,2             | Iris-versicolor |
| 33  | 5,2              | 4,1             | 1,5              | 0,1             | Iris-setosa     |
| 148 | 6,5              | 3               | 5,2              | 2               | Iris-virginica  |
| 6   | 5,4              | 3,9             | 1,7              | 0,4             | Iris-setosa     |
| 124 | 6,3              | 2,7             | 4,9              | 1,8             | Iris-virginica  |
| 40  | 5,1              | 3,4             | 1,5              | 0,2             | Iris-setosa     |
| 7   | 4,6              | 3,4             | 1,4              | 0,3             | Iris-setosa     |
| 72  | 6,1              | 2,8             | 4                | 1,3             | Iris-versicolor |

## Desafio de completude, descubra o valor de PetalLength (cm) para o ID #90

|     |     |     |     |     |                 |
| --- | --- | --- | --- | --- | --------------- |
| #90 | 5,5 | 2,5 | ??? | 1,3 | iris-versicolor |

## Resposta

Para dados categóricos, ou não se usa (já que não são numéricos) ou usa-se 0 quando for igual ao valor categórico comparado e 1 quando for diferente.

d(63)= $\sqrt{(5,5 - 6,0)^2 + (2,5 - 2,2)^2 + (1,3 - 1)^2}$
d(105)= $\sqrt{(5,5 - 6,5)^2 + (2,5 - 3)^2 + (1,3 - 2,2)^2}$
d(83)= $\sqrt{(5,5 - 5,8)^2 + (2,5 - 2,7)^2 + (1,3 - 1,2)^2}$
d(33)= $\sqrt{(5,5 - 5,2)^2 + (2,5 - 4,1)^2 + (1,3 - 0,1)^2}$
d(148)= $\sqrt{(5,5 - 6,5)^2 + (2,5 - 3)^2 + (1,3 - 2)^2}$
d(6)= $\sqrt{(5,5 - 5,4)^2 + (2,5 - 3,9)^2 + (1,3 - 0,4)^2}$
d(124)= $\sqrt{(5,5 - 6,3)^2 + (2,5 - 2,7)^2 + (1,3 - 1,8)^2}$
d(40)= $\sqrt{(5,5 - 5,1)^2 + (2,5 - 3,4)^2 + (1,3 - 0,2)^2}$
<!-- d(7)= $\sqrt{(5,5 - 4,6)^2 + (2,5 - 3,4)^2 + (1,3 - 0,3)^2}$ -->
<!-- d(72)= $\sqrt{(5,5 - 6,1)^2 + (2,5 - 2,8)^2 + (1,3 - 1,3)^2}$ -->

d(63) = 0,65
d(105) = 1,43
d(83) = 0,37
d(33) = 2,02
d(148) = 1,31
d(6) = 1,66
d(124) = 0,96
d(40) = 1,47
<!-- d(7) = 1,61 -->
<!-- d(72) = 0,67 -->

3 mais próximos: 83, 63, 124
petal length = 3,9 + 4 + 4,9 / 3 = 4,26 cm

4 mais próximos: 83, 63, 124, 148
petal length =  3,9 + 4 + 4,9 + 1,3 / 4 = 4,5 cm
