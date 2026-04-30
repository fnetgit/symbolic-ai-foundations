# Tarefa

1. Buscar no Repositório UCI um dataset
2. Gerar o arquivo .arff
3. Realizar a Análise dos Atributos
4. Realizar 3 tarefas de Classificação
   - Árvore de Decisão
   - *Perceptron (Rede Neural)*
   - Random Forest
5. Análise dos Resultados

---

- Dataset escolhido: <https://archive.ics.uci.edu/dataset/320/student+performance>

- Apaguei as colunas G1 e G2, pois elas são notas parciais e mantê-las causaria Data Leakage (vazamento de dados). Isso viciaria o algoritmo, mascarando a real correlação dos atributos socioeconômicos e de contexto com a aprovação final do aluno.

- Converti a G3 para variável categórica (Fail para notas < 10, e Pass para notas >= 10).

---

## Análise dos Resultados

1. Random Forest:
Teve a maior Accuracy global (69.11%), mas falhou no problema de negócio. Ele atingiu esse número agindo de forma "preguiçosa": classificou quase todos como Pass (classe majoritária).
Falha: Gerou assustadores 97 False Negatives. Na prática, ignorou 97 alunos que reprovaram.

2. Multilayer Perceptron:
A Accuracy caiu para 64.30%, mas o Recall da classe minoritária (Fail) foi o melhor dos três.
Vantagem: Reduziu os False Negatives para 72. Identificou melhor os alunos em risco, pagando o preço de gerar mais alarmes falsos (False Positives).
Sofreu overfitting devido à alta complexidade matemática para escassas 395 instâncias e atuou como uma Black Box inauditável.

3. J48:
Entregou o melhor equilíbrio estatístico (F-Meansure de 0.650). Accuracy de 66.32% e 82 False Negatives.
Vantagem: É um modelo White Box. O algoritmo identificou matematicamente que o histórico de reprovações (failures) é o preditor mais forte (nó-raiz). Entregou regras lógicas rastreáveis e justificáveis, o que possui altíssimo Business Value.

## Conclusão

O maior problema foi a natureza do próprio Dataset, visto que a métrica Kappa não ultrapassou 0.18 em nenhum modelo. Após retirar as notas parciais (G1 e G2), sobram outros dados, porém o problema central é que essas variáveis não determinam a nota de um aluno. O desempenho de um aluno é influenciado por uma série de fatores externos, como motivação, apoio familiar, saúde mental, entre outros, que não estão presentes no dataset.
