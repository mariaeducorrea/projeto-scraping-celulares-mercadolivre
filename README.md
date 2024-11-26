# projeto-scraping-celulares-mercadolivre


### 1. Coleta de Dados (Extract)
Utilizamos **Scrapy**, uma framework de web scraping em Python, para realizar a coleta automatizada de dados diretamente do site do Mercado Livre. Essa etapa envolve:
- Extração de informações dos produtos, como nome, preço, e outras características relevantes.
- Configuração de um **User-Agent** para evitar bloqueios.
- Armazenamento dos dados brutos em formato **JSONL** para maior flexibilidade.

**Ferramenta utilizada:** Scrapy.

---

### 2. Transformação dos Dados (Transform)
Os dados coletados são processados e transformados com **Pandas**, permitindo:
- Limpeza e organização das informações.
- Conversão de colunas para tipos apropriados (ex.: `float` para preços).
- Tratamento de valores ausentes ou inconsistentes.
- Combinação de informações, como valores de reais e centavos em uma única coluna.

**Ferramenta utilizada:** Pandas.

---

### 3. Carregamento e Visualização (Load)
Para facilitar a análise, foi desenvolvido um **dashboard interativo** utilizando **Streamlit**, que:
- Carrega os dados transformados.
- Apresenta as informações de forma visual e intuitiva, com tabelas e gráficos.
- Permite interação em tempo real para explorar os dados coletados.

**Ferramenta utilizada:** Streamlit.

---

O pipeline completo do projeto foi projetado para ser modular, permitindo a fácil atualização dos dados e sua reanálise conforme necessário.