# Atividade KNN

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

## Descubra as distâncias euclidianas e classfique os dados da tabela abaixo utilizando o algoritmo KNN

|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |
| #7  | 4,6 | 3,4 | 1,4 | 0,3 | ?   |
| #72 | 6,1 | 2,8 | 4   | 1,3 | ?   |

## Resposta

### #7

d(63)= $\sqrt{(4,6 - 6,0)^2 + (3,4 - 2,2)^2 + (1,4 - 4,0)^2 + (0,3 - 1,0)^2}$
d(105)= $\sqrt{(4,6 - 6,5)^2 + (3,4 - 3,0)^2 + (1,4 - 5,8)^2 + (0,3 - 2,2)^2}$
d(83)= $\sqrt{(4,6 - 5,8)^2 + (3,4 - 2,7)^2 + (1,4 - 3,9)^2 + (0,3 - 1,2)^2}$
d(33)= $\sqrt{(4,6 - 5,2)^2 + (3,4 - 4,1)^2 + (1,4 - 1,5)^2 + (0,3 - 0,1)^2}$
d(148)= $\sqrt{(4,6 - 6,5)^2 + (3,4 - 3,0)^2 + (1,4 - 5,2)^2 + (0,3 - 2,0)^2}$
d(6)= $\sqrt{(4,6 - 5,4)^2 + (3,4 - 3,9)^2 + (1,4 - 1,7)^2 + (0,3 - 0,4)^2}$
d(124)= $\sqrt{(4,6 - 6,3)^2 + (3,4 - 2,7)^2 + (1,4 - 4,9)^2 + (0,3 - 1,8)^2}$
d(40)= $\sqrt{(4,6 - 5,1)^2 + (3,4 - 3,4)^2 + (1,4 - 1,5)^2 + (0,3 - 0,2)^2}$

#### Ranking e resultados de proximidade (#7)

d(40) = 0,51
d(33) = 0,94
d(6) = 0,99
d(83) = 2,99
d(63) = 3,26
d(124) = 4,22
d(148) = 4,59
d(105) = 5,17

1N = Iris-setosa (ID: 40)
2N = Iris-setosa (ID: 33)
3N = Iris-setosa (ID: 6)
4N = Iris-versicolor (ID: 83)

Classificação final para #7: Iris-setosa (Pois 3 os 4 vizinhos são da espécie Iris-setosa).

### #72

d(63)= $\sqrt{(6,1 - 6,0)^2 + (2,8 - 2,2)^2 + (4,0 - 4,0)^2 + (1,3 - 1,0)^2}$
d(105)= $\sqrt{(6,1 - 6,5)^2 + (2,8 - 3,0)^2 + (4,0 - 5,8)^2 + (1,3 - 2,2)^2}$
d(83)= $\sqrt{(6,1 - 5,8)^2 + (2,8 - 2,7)^2 + (4,0 - 3,9)^2 + (1,3 - 1,2)^2}$
d(33)= $\sqrt{(6,1 - 5,2)^2 + (2,8 - 4,1)^2 + (4,0 - 1,5)^2 + (1,3 - 0,1)^2}$
d(148)= $\sqrt{(6,1 - 6,5)^2 + (2,8 - 3,0)^2 + (4,0 - 5,2)^2 + (1,3 - 2,0)^2}$
d(6)= $\sqrt{(6,1 - 5,4)^2 + (2,8 - 3,9)^2 + (4,0 - 1,7)^2 + (1,3 - 0,4)^2}$
d(124)= $\sqrt{(6,1 - 6,3)^2 + (2,8 - 2,7)^2 + (4,0 - 4,9)^2 + (1,3 - 1,8)^2}$
d(40)= $\sqrt{(6,1 - 5,1)^2 + (2,8 - 3,4)^2 + (4,0 - 1,5)^2 + (1,3 - 0,2)^2}$

#### Ranking e resultados de proximidade (#72)

d(83) = 0,34
d(63) = 0,67
d(124) = 1,05
d(148) = 1,45
d(105) = 2,06
d(6) = 2,79
d(40) = 2,97
d(33) = 3,19

1N = Iris-versicolor (ID: 83)
2N = Iris-versicolor (ID: 63)
3N = Iris-virginica (ID: 124)
4N = Iris-virginica (ID: 148)

Classificação final para #72: Empate (Pois 2 vizinhos são da espécie Iris-versicolor e 2 são da espécie Iris-virginica) Teria que ser resolvido por outro critério.
