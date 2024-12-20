# Sobre o Projeto 


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


# Passos para Rodar o Projeto

Siga os passos abaixo para configurar o ambiente e executar o projeto localmente.

```bash
# 1. Clone o repositório do projeto
git clone https://github.com/seu-usuario/projeto-scraping-celulares-mercadolivre.git
cd projeto-scraping-celulares-mercadolivre

# 2. Criar e ativar um ambiente virtual
# Para sistemas Linux/MacOS
python3 -m venv .venv
source .venv/bin/activate

# Para Windows
python -m venv .venv
source .venv/Scripts/activate

# 3. Instalar as dependências com o pip
pip install scrapy pandas streamlit

# 4. Navegue até a pasta src
cd src

# 5. Execute o dashboard interativo
streamlit run dashboard/app.py

