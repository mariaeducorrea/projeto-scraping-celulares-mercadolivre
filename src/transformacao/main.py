#cria alias pd para usar funções da biblioteca de forma compacta, ex: pd.DataFrame()
import pandas as pd 
#importa biblioteca SQLite3 para trabalhas com banco SQLite, SQLite3 permite interação com bd com python
import sqlite3
#biblioteca que fornece classes para manipulação de datas e horas.
from datetime import datetime
#importa biblioteca os que fornece interface para interagir com o sistema operacional.
import os

#definir o caminho para o arquivo jsonl com a coleta
df = pd.read_json('../data/data.jsonl', lines=True)

# executar: bash > python tranformacao/main.py

# adicionar a coluna_source com um valor fixo - a coluna source informa de onde esses dados vieram
df['_source'] = "https://lista.mercadolivre.com.br/celular#D[A:celular]"


# adicionar coluna de data de coleta usando a biblioteca datetime - from datetime import datetime
df['_data_coleta'] = datetime.now()


#tratar os valores nulos para colunas valores
df['valor_antigo'] = df['valor_antigo'].fillna(0).astype(float)
df['valor_atual'] = df['valor_atual'].fillna(0).astype(float)
df['valor_antigo_cent'] = df['valor_antigo_cent'].fillna(0).astype(float)
df['valor_atual_cent'] = df['valor_atual_cent'].fillna(0).astype(float)

#tratar valores nulos na coluna marca
df['marca'] = df['marca'].fillna('Desconhecido')

#tratar os valores 
df['preco_antigo'] = df['valor_antigo'] + df['valor_antigo_cent'] / 100
df['preco_novo'] = df['valor_atual'] + df['valor_atual_cent'] / 100


#dropar colunas antigas 
# df.drop(columns=['valor atual', 'valor_atual_cent'])
df.drop(columns=['valor_antigo','valor_atual', 'valor_antigo_cent','valor_atual_cent'], inplace=True)


#conectar ou criar banco de dados novo np sqlite
conn = sqlite3.connect('../data/quotes.db')

#salvar o dataframe no banco de dados sqlite criando uma tabela 
df.to_sql('mercadolivre_celulares', conn, if_exists='replace', index=False)

conn.close()

print(df.head())

#bash : python transfromacao/main.py


