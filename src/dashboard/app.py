import streamlit as st
import pandas as pd
import sqlite3


st.set_page_config(
    page_title="Dashboard de Celulares - Mercado Livre",
    page_icon="📱",
    layout="wide"
)

# Conectar ao banco de dados SQLite
conn = sqlite3.connect('../data/quotes.db')

#Carregar dado da tabela 'mercadolivre_celulares' em um Dataframe pandas
df = pd.read_sql_query('SELECT * FROM mercadolivre_celulares', conn)

#Fechar conexão com o banco
conn.close()

#titulo aplicacao
st.title('Pesquisas de Mercado - Celulares no Mercado Livre')

#criar subtitulo
st.subheader('Pesquisas de Mercado - Celulares no Mercado Livre')

#adicionar colunas para KPIS
col1, col2, col3 = st.columns(3)

# Adicionar número total de itens - KPI 1
#.shape() retorna tupla do formato (n_linhas,n_colunas), shape[0] retorna o indice 0 da tupla que é igual ao n_linhas da bale aque resulta na quantidade de itens
total_itens = df.shape[0]
col1.metric(label="Número Total de Itens", value=total_itens)

#Adicionar número de marcas - KPI 2
#.nunique() conta o n° de valores únicos em uma coluna
marcas = df['marca'].nunique()
col2.metric(label="Número de Marcas", value=marcas)


#Preço médio por marca
# Quantidade de itens por marca
st.subheader("Quantidade de itens por marca")
# Contar a quantidade de itens por marca
quantidade_por_marca = df['marca'].value_counts()
# Exibir o gráfico de barras e ajustá-lo para ocupar todo o espaço
st.bar_chart(quantidade_por_marca, use_container_width=True)



# Buscar modelos coletados
st.subheader("Buscar modelos específicos")
# Entrada de texto para usuário digitar modelo
modelo = st.text_input("Digite o modelo do celular que deseja buscar:")

# Filtrar do 
if modelo: #se for digitado um modelo
    #filtra dataframe com base na coluna nome /constains - realiza a busca/case - não diferencia maiusculo e minusculo/ na - evita problema com valores NaN 
    df_modelos = df[df['nome'].str.contains(modelo, case=False, na=False)]

    if not df_modelos.empty: #caso tenha o modelo
        st.write(f'Resultadps para o modelo: {modelo}')
        st.write(df_modelos[['nome','marca','preco_novo']]) 
    else: #caso não tenha o modelo
        st.srite(f'Nenhum resiltado encontrado para o moelo: {modelo}')



