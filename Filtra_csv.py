#Bibliotecas utilizadas
import pandas as pd
import io

#Faça uploud do csv original
uploaded = files.upload()
#Colocando os dados em uma variavel
uplcsv=io.BytesIO(uploaded['arquivo_que_deve_ser_lido.csv'])
#Transfomando esses dados da variavel em um DataFrame
df2 = pd.read_csv(uplcsv, sep=';', header=0, encoding = "ISO-8859-1")
#Fazendo o Filtro e salvando em uma nova variavel
dfCon=df2.loc[df2["Nome_da_coluna"]=="O_que_irá_filtrar"]
#Classificando os dados
dfInd=dfCon.set_index('Nome da coluna para funcionar como indice')
#Salvando em um novo arquivo
dfInd.to_csv("Nome_do_novo_arquivo.csv",sep=';',encoding = "ISO-8859-1")
