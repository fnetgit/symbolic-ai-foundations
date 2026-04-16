# Aprendendo com Vizinhos Próximos - KNN

O KNN (K-Nearest Neighbors) é um algoritmo de aprendizado de máquina supervisionado que pode ser usado para classificação e regressão. Ele é baseado na ideia de que os dados semelhantes estão próximos uns dos outros no espaço de características. O KNN classifica um novo ponto de dados com base na maioria dos rótulos dos seus vizinhos mais próximos. K é o número de vizinhos a serem considerados para a classificação ou regressão.

- Ele é lazy, diferentemene da arvore de decisão que é gulosa
- Ele é sensível a escala, ou seja, é importante normalizar os dados antes de usar o KNN
- Ele é sensível a outliers, pois os vizinhos mais próximos podem ser influenciados por pontos de dados atípicos
- Ele é computacionalmente caro, especialmente para grandes conjuntos de dados, pois precisa calcular a distância entre o ponto de dados e todos os outros pontos no conjunto de dados para encontrar os vizinhos mais próximos
- Ele é fácil de entender e implementar, o que o torna uma escolha popular para problemas de classificação e regressão simples.
