# Anotações sobre a atividade

Primeiro comecei renomeando os títulos das tabelas do [old-dataset-tsc.csv](old-dataset-tsc.csv), também excluí a coluna 'Cabelo 1'(Cabelo 2 virou tipo_cabelo), pois todos os dados eram iguais('curto').

Padronizei os dados, coloquei as primeiras letras em maiúsculas, tirei acentos (incluindo os 'não') e os espaços finais. coloquei as alturas com separador de ponto e não vírgula. [new-dataset-tsc.csv](new-dataset-tsc.csv)

Transformei alguns campos com números em string, como idade e altura. Deixei um espaço antes dos simbolos de >
Fiz o arquivo arff [new-dataset-tsc.arff](new-dataset-tsc.arff) removendo os nomes dos alunos, corrigi nomes com espaços, barras e parênteses (no arrf, se o nome tiver espaços, deve ser colocado entre aspas). Nas chaves, coloquei todos os valores possiveis de algumas colunas, mesmo os que não estavam presentes no dataset, como por exemplo, o atributo 'estado_civil', que tinha apenas 'solteiro' e 'casado', mas adicionei 'viuvo' e 'separado judicialmente'.
