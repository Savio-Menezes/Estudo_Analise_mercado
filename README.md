🛒 Dashboard Interativo de Vendas do Supermercado
Este projeto cria um dashboard interativo utilizando Python, Streamlit e Plotly para analisar os dados de vendas de um supermercado. Ele exibe gráficos para:

![Aplicação](https://github.com/user-attachments/assets/fc7a01e3-33b5-48de-91ae-19f1bf4f4e52)

Faturamento diário por unidade.
Produtos mais vendidos.
Contribuição por filial.
Desempenho das formas de pagamento.
Avaliações de cada loja.
📊 Funcionalidades
✅ Faturamento diário com separação por cidades.
✅ Visualização de vendas por linha de produto.
✅ Contribuição por unidade (filial).
✅ Análise de desempenho das formas de pagamento.
✅ Avaliações dos clientes por unidade.

🛠️ Tecnologias Utilizadas
Python 3.9+
Streamlit: Framework para dashboards interativos.
Pandas: Manipulação e análise de dados.
Plotly: Visualizações interativas e responsivas.
📂 Estrutura do Projeto
plaintext
Copiar código
.
├── supermarket_sales.csv    # Base de dados do projeto
├── dashboard.py             # Código principal da aplicação
└── README.md                # Documentação do projeto
⚙️ Como Executar o Projeto
1️⃣ Instale as Dependências
Certifique-se de que o Python 3.9+ está instalado.
Crie um ambiente virtual e instale as bibliotecas necessárias:

bash
Copiar código
# Crie o ambiente virtual
python -m venv venv

# Ative o ambiente virtual
# No Windows:
venv\Scripts\activate
# No Linux/Mac:
source venv/bin/activate

# Instale as bibliotecas
pip install streamlit pandas plotly
2️⃣ Baixe o Arquivo de Dados
Certifique-se de ter o arquivo supermarket_sales.csv, que é usado como base de dados, no mesmo diretório do código.

O arquivo deve:

Ter ; como separador.
Usar , para representar valores decimais.
3️⃣ Execute o Dashboard
Inicie o servidor local do Streamlit com o seguinte comando:

bash
Copiar código
streamlit run dashboard.py
O aplicativo será aberto automaticamente no navegador.

📋 Detalhes do Dashboard
📅 Faturamento por Dia
Mostra o faturamento diário separado por cidades.
Gráfico: Barras coloridas.

📦 Produtos Mais Vendidos
Visualiza a quantidade de vendas por tipo de produto.
Gráfico: Barras horizontais.

🏢 Contribuição por Filial
Compara o faturamento total de cada unidade.
Gráfico: Barras agrupadas.

💳 Desempenho das Formas de Pagamento
Exibe a participação de cada forma de pagamento nas vendas.
Gráfico: Pizza.

⭐ Avaliações por Unidade
Média de avaliações dos clientes por cidade.
Gráfico: Barras.

