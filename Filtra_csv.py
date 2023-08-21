# Bibliotecas utilizadas

import pandas as pd

# Colocando o nome do arquivo em uma variável
nome_arquivo = "endereço_do_arquivo.csv"

# Transformando esses dados da variável em um DataFrame
df2 = pd.read_csv(nome_arquivo, sep=';', header=0, encoding="ISO-8859-1")
# Fazendo o Filtro e salvando em uma nova variável
dfCon = df2.loc[df2["coluna_do_filtro"] == "filtro"]
# Classificando os dados
dfInd = dfCon.set_index('seta uma coluna como indice')
# Salvando em um novo arquivo
dfInd.to_csv("nome_do_novo_arquivo.csv", sep=';', encoding="ISO-8859-1")

