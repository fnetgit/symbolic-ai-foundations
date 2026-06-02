# Atividade subjetiva sobre Redes Neurais Artificiais

1. **Explique o funcionamento do neurônio artificial.**
Funciona analogamente ao neurônio biológico, recebendo sinais de entrada, processando-os e gerando uma saída. O neurônio artificial é composto por dendritos (entradas), um corpo celular (processamento) e um axônio (saída). Ele utiliza pesos para ajustar a importância de cada entrada e uma função de ativação para determinar se o sinal processado é forte o suficiente para ser transmitido como saída.

2. **Descreva os objetivos principais das funções de ativação.**
As funções de ativação têm como objetivo principal introduzir a não-linearidade nas redes neurais, permitindo que elas aprendam e modelem relações complexas nos dados. Sem elas, a rede funcionaria apenas como um modelo matemático linear simples, independentemente da quantidade de camadas que possuísse, sendo incapaz de resolver problemas sofisticados.

3. **Faça uma analogia entre os elementos constituintes do neurônio artificial e do neurônio biológico.**
Fazendo um paralelo com a biologia, os dendritos do neurônio biológico atuam como as entradas do neurônio artificial, recebendo os estímulos externos. As sinapses representam os pesos da rede, que definem a força ou a importância de cada sinal recebido. O corpo celular equivale à unidade de processamento, enquanto o axônio funciona como a saída do neurônio artificial, transmitindo o sinal processado para a próxima camada.

4. **Discorra sobre a importância envolvendo o limiar de ativação.**
Ele é importante porque funciona como um "gatilho" que determina o nível mínimo de estímulo necessário para que um neurônio dispare o seu sinal. Sem ele a rede não teria a flexibilidade para aprender.

5. **Em relação as características das redes neurais artificiais, explique em que consiste a adaptação por experiência e a capacidade de generalização.**
A adaptação por experiência refere-se à capacidade das redes neurais de ajustar seus pesos com base nos dados de treinamento, permitindo que aprendam a partir de exemplos. Já a capacidade de generalização é a habilidade da rede de aplicar o conhecimento adquirido durante o treinamento para fazer previsões ou tomar decisões sobre dados que não foram vistos anteriormente, demonstrando que a rede aprendeu padrões subjacentes e não apenas memorizou os dados de treinamento.

6. **Discorra sobre as principais características matemáticas que são cerificadas nas funções de ativação logística e tangente hiperbólica.**
Ambas exigem não-linearidade, continuidade, monotonicidade estrita e diferenciabilidade em todo o domínio real para viabilizar a otimização por retropropagação do erro. Geometricamente, formam curvas sigmóides com saturação nos extremos. A logística mapeia os reais para o intervalo $(0, 1)$, enquanto a tangente hiperbólica mapeia para $(-1, 1)$, sendo esta última centrada na origem, propriedade que acelera empiricamente a convergência da rede.

7. **Obtenha as expressões analíticas das derivadas de primeira ordem da função de ativação logística e tangente hiperbólica.**
A função logística é dada por $f(x) = \frac{1}{1 + e^{-x}}$. Sua derivada de primeira ordem é $f'(x) = f(x)(1 - f(x))$.
A função tangente hiperbólica é dada por $f(x) = \tanh(x)$. Sua derivada de primeira ordem é $f'(x) = 1 - f(x)^2$.

8. **Para um problema específico, há a possibilidade de utilizar como função de ativação tanto a função logística como a tangente hiperbólica. Em termos de implementação em hardware, discorra quais seriam os eventuais aspectos relevantes para seleção de uma dessas.**
A função logística, por ser mapeada para o intervalo (0, 1), pode ser mais adequada para problemas de classificação binária, enquanto a tangente hiperbólica, que é centrada na origem e mapeia para (-1, 1), pode ser preferida em redes neurais profundas devido à sua capacidade de acelerar a convergência durante o treinamento. Além disso, a tangente hiperbólica pode ser mais eficiente em termos de cálculo, pois sua derivada é expressa diretamente em termos da função original, o que pode reduzir o custo computacional durante a retropropagação do erro.

9. **Considerando que as operações individuais nos neurônios artificiais são realizados mais rapidamente em comparação com neurônios biológicos, explique porque diversas atividades executadas pelo cérebro humano produzem resultados mais rapidamente que um microcomputador.**
O cérebro humano é altamente paralelo, com bilhões de neurônios e trilhões de conexões sinápticas que processam informações simultaneamente. Em contraste, um microcomputador tradicionalmente processa informações de forma sequencial, o que pode levar a atrasos significativos em tarefas complexas. Além disso, o cérebro é otimizado para eficiência energética e possui uma arquitetura adaptativa que permite a aprendizagem e a generalização, enquanto os computadores dependem de algoritmos específicos e podem ser limitados por sua capacidade de processamento e memória.

10. **Quais os principais tipos de problemas em que redes neurais artificiais são aplicadas?**
São eficazes em tarefas que envolvem grandes volumes de dados e relações complexas entre as variáveis, incluindo classificação de padrões, reconhecimento de voz, processamento de linguagem natural, visão computacional, previsão de séries temporais, diagnóstico médico, detecção de fraudes, entre outros.

11. **Discorra sobre as vantagens e desvantagens envolvidas na aprendizagem usando lote de padrões e aprendizagem usando padrão-por-padrão.**
A aprendizagem usando lote de padrões (batch learning) tem a vantagem de ser mais estável e eficiente para grandes conjuntos de dados, pois os pesos são atualizados após processar todo o lote, o que pode levar a uma convergência mais suave. No entanto, pode ser menos eficiente em termos de memória e tempo de processamento, especialmente para conjuntos de dados muito grandes. Já a aprendizagem usando padrão-por-padrão (online learning) permite atualizações mais frequentes dos pesos, o que pode acelerar a aprendizagem e permitir que a rede se adapte rapidamente a mudanças nos dados. Porém, pode ser mais suscetível a ruídos e oscilações nos pesos, o que pode dificultar a convergência.

12. **Considere uma aplicação que possua quatro entradas e duas saídas. O projetista menciona que neste caso a rede feedforward de camadas múltiplas a ser implementada deve conter necessariamente quatro neurônios na primeira camada. Discorra se tal informação é pertinente.**
Não é necessariamente pertinente. O número de neurônios na primeira camada (camada escondida) não precisa ser igual ao número de entradas. O projetista pode escolher um número diferente de neurônios na camada escondida com base em experimentação, complexidade do problema e capacidade de generalização desejada. O importante é que a rede seja capaz de aprender as relações entre as entradas e as saídas, independentemente do número específico de neurônios na camada escondida.

13. **Em relação ao exercício anterior, cite alguns fatores que influenciam na determinação do número de camadas escondidas de uma rede feedforward de camadas múltiplas.**
Alguns fatores que influenciam na determinação do número de camadas escondidas incluem a complexidade do problema a ser resolvido, a quantidade e a qualidade dos dados disponíveis para treinamento, a capacidade de generalização desejada, o risco de overfitting (quando a rede se torna muito complexa e se ajusta demais aos dados de treinamento), e as limitações computacionais (como tempo de treinamento e recursos de hardware). Em geral, problemas mais complexos podem exigir mais camadas escondidas para capturar as relações não lineares entre as entradas e as saídas, enquanto problemas mais simples podem ser resolvidos com menos camadas.

14. **Quais as eventuais diferenças estruturais observadas nas redes com arquitetura recorrente em relação àquelas com arquitetura feedforward?**
As redes com arquitetura recorrente (RNNs) possuem conexões que formam ciclos, permitindo que a saída de um neurônio seja realimentada como entrada para o mesmo ou para outros neurônios, o que é útil para processar sequências de dados e capturar dependências temporais. Em contraste, as redes feedforward possuem uma estrutura acíclica, onde os dados fluem em uma única direção, da entrada para a saída, sem realimentação. Essa diferença estrutural torna as RNNs mais adequadas para tarefas como processamento de linguagem natural e séries temporais, enquanto as redes feedforward são mais comuns em tarefas de classificação e regressão estática.

15. **Mencione em que tipos de aplicações é essencial a utilização de redes neurais recorrentes.**
As redes neurais recorrentes são essenciais em aplicações que envolvem dados sequenciais ou temporais, como processamento de linguagem natural (tradução automática, análise de sentimentos), reconhecimento de fala, previsão de séries temporais (previsão do tempo, mercado financeiro), geração de texto, e modelagem de dependências em dados de sequência (como DNA ou música). Elas são capazes de capturar relações temporais e contextuais que as redes feedforward não conseguem, tornando-as indispensáveis para essas tarefas.

16. **Elabore um diagrama de blocos que ilustre o funcionamento do treinamento supervisionado.**

    ```mermaid
    graph LR
        A[Dados + Rótulos] --> B[Rede Neural]
        B -->|Previsão| C[Cálculo do Erro]
        C -->|Ajuste| D[Atualização dos Pesos]
        D -.->|Melhora a Rede| B
    ```

17. **Discorra sobre o conceito de método de treinamento e algoritmo de aprendizado, explicitando-se ainda o conceito de época de treinamento.**
O método de treinamento refere-se à abordagem geral utilizada para ajustar os pesos e os limiares de uma rede neural, como o treinamento supervisionado, não-supervisionado ou por reforço. O algoritmo de aprendizado é a implementação específica do método de treinamento, como o algoritmo de retropropagação para redes feedforward. A época de treinamento é um ciclo completo em que a rede neural é exposta a todo o conjunto de dados de treinamento uma vez, permitindo que os pesos sejam atualizados com base nos erros observados durante esse processo. Múltiplas épocas são geralmente necessárias para que a rede converja para um conjunto de pesos que minimize o erro.

18. **Quais as principais diferenças existentes entre métodos baseados em treinamento supervisionado e não-supervisionado?**
O treinamento supervisionado envolve o uso de um conjunto de dados rotulado, onde cada entrada tem uma saída desejada associada, permitindo que a rede aprenda a mapear as entradas para as saídas corretas. Já o treinamento não-supervisionado não utiliza rótulos, e a rede deve encontrar padrões ou estruturas subjacentes nos dados por conta própria, como em tarefas de clustering ou redução de dimensionalidade. O treinamento supervisionado é mais adequado para tarefas de classificação e regressão, enquanto o não-supervisionado é útil para exploração de dados e descoberta de padrões ocultos.

19. **Considere uma aplicação específica, explicite então como poderia ser um critério de desempenho utilizado para ajustes de pesos e limiares da rede que empregará método de treinamento com reforço.**
Em uma aplicação de jogo de tabuleiro, como o xadrez, um critério de desempenho para ajustes de pesos e limiares em um método de treinamento com reforço poderia ser a recompensa obtida após cada movimento. Por exemplo, a rede poderia receber uma recompensa positiva por movimentos que levam a uma posição vantajosa ou à vitória, e uma recompensa negativa por movimentos que resultam em desvantagem ou derrota. O objetivo seria maximizar a recompensa acumulada ao longo do tempo, incentivando a rede a aprender estratégias eficazes para vencer o jogo.

20. **Explique como se processa a regra de Hebb. No contexto do algoritmo de aprendizado Perceptron.**
A Regra de Hebb e o Perceptron operam de formas incompatíveis. A Regra de Hebb aumenta e reforça os pesos sempre que a entrada e a saída disparam ao mesmo tempo, baseando-se apenas em correlação. Já o Perceptron funciona sob a Regra de Correção de Erro (aprendizado supervisionado). Ele só altera os pesos quando a saída calculada é diferente da saída esperada. Se o Perceptron acerta a classificação, os pesos simplesmente não mudam. Isso contraria totalmente o princípio de Hebb. Aplicar a Regra de Hebb no Perceptron quebra a lógica do algoritmo, trocando um sistema focado em corrigir erros por um que apenas reforça conexões ativas.

21. **Mostre por intermédio de gráficos ilustrativos como pode ocorrer a instabilidade no processo de convergência do Perceptron quando da utilização de valores inapropriados para a taxa de aprendizado.**
A instabilidade no processo de convergência do Perceptron pode ocorrer quando a taxa de aprendizado é muito alta, fazendo com que os pesos sejam ajustados de forma excessiva a cada iteração. Isso pode resultar em oscilações nos pesos, onde eles alternam entre valores extremos sem se aproximar da solução ideal. Em um gráfico de convergência, isso se manifestaria como uma série de pontos que não se aproximam de um valor estável, mas sim saltam para cima e para baixo, indicando que o modelo não está aprendendo de forma eficaz. Por outro lado, uma taxa de aprendizado muito baixa pode levar a uma convergência extremamente lenta, onde os pesos se ajustam apenas marginalmente a cada iteração, resultando em um gráfico que mostra uma linha quase plana, indicando que o modelo está progredindo muito lentamente em direção à solução ideal.

22. **Explique por que o Perceptron só consegue classificar padrões cuja fronteira de separação entre classes seja linear.**
O Perceptron é um modelo de classificação linear, o que significa que ele tenta encontrar uma linha que separe as classes de dados. Se as classes de dados não forem linearmente separáveis, ou seja, se não for possível traçar uma linha que divida perfeitamente as classes, o Perceptron não será capaz de convergir para uma solução adequada. Isso ocorre porque o algoritmo de aprendizado do Perceptron ajusta os pesos com base na classificação correta ou incorreta dos padrões, e se os padrões não forem linearmente separáveis, ele continuará a ajustar os pesos sem nunca alcançar uma configuração que classifique todos os padrões corretamente, resultando em um processo de aprendizado infinito ou em uma solução subótima.

23. **Em termos de implementação computacional descreva a importância de tratarmos o limiar de ativação ($\theta$) como um dos elementos do vetor de pesos ($\mathbf{w}$).**
Tratar o limiar de ativação ($\theta$) como um dos elementos do vetor de pesos ($\mathbf{w}$) é importante para simplificar a implementação computacional do Perceptron. Ao incluir o limiar como um peso adicional, podemos representar a função de ativação de forma mais compacta e eficiente. Isso permite que o processo de atualização dos pesos seja unificado, já que o limiar pode ser ajustado da mesma maneira que os outros pesos durante o treinamento. Além disso, essa abordagem facilita a implementação de operações matriciais, tornando o código mais limpo e eficiente, especialmente quando se trabalha com grandes conjuntos de dados e múltiplas camadas em redes neurais mais complexas.

24. **Seja um problema de classificação de padrões que se desconhece a priori se as duas classes são ou não separáveis linearmente. Elabore uma estratégia para verificar a possível aplicação Perceptron em tal problema.**
Realizar uma análise exploratória dos dados, utilizando técnicas de visualização para identificar a distribuição das classes. Em seguida, aplicar um algoritmo de classificação linear, como o Perceptron, e avaliar seu desempenho utilizando métricas como acurácia, precisão, recall e F1-score. Se o modelo apresentar um desempenho significativamente inferior, pode ser um indicativo de que as classes não são linearmente separáveis.

25. **Dois projetistas de instituições diferentes estão aplicando uma rede Perceptron para mapear o mesmo problema de classificação de padrões. Discorra se é correto afirmar que ambas as redes convergirão com o mesmo número de épocas.**
Não, porque a convergência do Perceptron pode ser influenciada por diversos fatores, como a inicialização dos pesos, a ordem de apresentação dos dados de treinamento, a taxa de aprendizado e a presença de ruídos nos dados. Mesmo que ambos os projetistas estejam utilizando o mesmo algoritmo e o mesmo conjunto de dados, as diferenças na implementação e nas condições de treinamento podem levar a resultados diferentes em termos de número de épocas necessárias para a convergência.

26. **Em relação ao exercício anterior, considere-se que ambas as redes já estão devidamente treinadas. Para um conjunto contendo 10 novas amostras que devem ser identificadas, explique se os resultados produzidos por ambas serão os mesmos.**
É provável que ambas produzam os mesmos resultados para as 10 novas amostras, desde que essas amostras sejam semelhantes aos dados de treinamento. No entanto, se as amostras forem significativamente diferentes ou se houver variações nos pesos finais das redes devido a diferenças na inicialização ou no processo de treinamento, os resultados podem variar. Além disso, se as amostras apresentarem características que não foram bem representadas durante o treinamento, ambas as redes podem ter dificuldades em classificá-las corretamente, o que pode levar a resultados divergentes.

27. **Seja um problema de classificação de padrões que seja linearmente separável composto de 50 amostras. Em determinada época de treinamento observou-se que somente para uma dessas amostras a rede não estava produzindo a resposta desejada. Discorra se é então necessário apresentar novamente todas as 50 amostras na próxima época de treinamento.**
Sim, é necessário processar a época inteira novamente. A atualização dos pesos para corrigir a amostra divergente altera a posição geométrica (rotação ou translação) do hiperplano de separação. Consequentemente, amostras que antes eram classificadas corretamente pelo hiperplano antigo podem passar a ser classificadas de forma incorreta pelo novo hiperplano. A convergência só é atestada quando uma época inteira ocorre sem nenhuma alteração no vetor de pesos.

28. **Considere um problema de classificação de padrões composto de duas entradas {x 1 e x2}., cujo conjunto treinamento é composto pelas seguintes amostras de treinamento:**

    | $x_1$ | $x_2$ | Classe |
    | ----- | ----- | ------ |
    | 0,75  | 0,75  | A      |
    | 0,75  | 0,25  | B      |
    | 0,25  | 0,75  | B      |
    | 0,25  | 0,25  | A      |

    **Mostre se é possível aplicar Perceptron na resolução deste problema.**
Não é possível. Este conjunto de dados representa o problema da porta lógica XOR (Ou Exclusivo). Ao plotar as coordenadas no plano bidimensional, observa-se que as classes A e B formam diagonais opostas e cruzadas. É matematicamente impossível traçar uma única reta que separe a classe A da classe B. O Perceptron de camada simples converge exclusivamente para problemas linearmente separáveis; portanto, o treinamento entrará em loop infinito sem solução geométrica.

29. **Explique de forma detalhada quais seriam as eventuais limitações do Perceptron se considerarmos o seu limiar de ativação nulo.**
o Perceptron se torna incapaz de classificar corretamente os padrões que estão próximos da origem do espaço de entrada. Porque o Perceptron só pode produzir uma saída positiva quando a soma ponderada das entradas for maior que zero. Se o limiar for zero, qualquer combinação de entradas que resulte em uma soma ponderada igual a zero ou negativa será classificada como pertencente à classe negativa, mesmo que essas amostras possam ser parte da classe positiva. Isso limita a capacidade do Perceptron de aprender e generalizar a partir dos dados, especialmente em casos onde as classes estão próximas ou se sobrepõem, tornando-o inadequado para muitos problemas de classificação do mundo real.
