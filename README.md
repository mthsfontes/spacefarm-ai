SpaceFarm AI
Integrantes do Grupo
Richard Wrobel dos Santos
Matheus Fontes
[Nome do integrante 3]
[Nome do integrante 4]
Substitua os campos entre colchetes pelos nomes completos dos demais integrantes do grupo, conforme solicitado no README da raiz da atividade.
Proposta do Projeto
O SpaceFarm AI é uma plataforma de monitoramento agrícola baseada em observação espacial, IoT, Inteligência Artificial e Ciência de Dados.
A proposta da solução é auxiliar produtores rurais na identificação de situações de estresse hídrico, degradação da vegetação e necessidade de irrigação, utilizando dados ambientais e indicadores inspirados em tecnologias de observação da Terra por satélites.
O projeto aplica conceitos da economia espacial no agronegócio, demonstrando como dados derivados de observação terrestre podem apoiar decisões agrícolas mais eficientes, sustentáveis e baseadas em dados.
Problema Abordado
Produtores rurais muitas vezes enfrentam dificuldades para identificar rapidamente quando uma plantação está sofrendo com falta de água, baixa umidade do solo ou sinais de perda de vigor vegetal.
A ausência de monitoramento contínuo pode causar:
desperdício de água;
decisões tardias de irrigação;
redução da produtividade;
aumento de custos operacionais;
dificuldade na análise da saúde da vegetação.
Funcionamento da Solução
O SpaceFarm AI funciona por meio da integração de dados ambientais, indicadores espaciais e modelos de Machine Learning.
O fluxo principal da solução é:
Coleta de dados ambientais
São considerados dados como temperatura, umidade do ar, umidade do solo e luminosidade.
Uso de indicador espacial NDVI
O sistema utiliza o NDVI (Normalized Difference Vegetation Index), indicador amplamente associado à observação terrestre por satélites, para representar a saúde da vegetação.
Envio dos dados para uma API
Os dados são recebidos e tratados por uma API desenvolvida com Flask.
Armazenamento em banco de dados
As informações são armazenadas no MongoDB Atlas, permitindo persistência e consulta dos registros.
Processamento e análise dos dados
A biblioteca Pandas é utilizada para manipulação, organização e preparação dos dados.
Aplicação de Inteligência Artificial
Modelos de Machine Learning, como Decision Tree e Random Forest, analisam os dados e recomendam ações, como necessidade de irrigação.
Visualização no Dashboard
O usuário acompanha os indicadores por meio de um dashboard desenvolvido com Streamlit, contendo dados ambientais, histórico, NDVI, riscos hídricos e previsões da IA.
Arquitetura da Solução
Sensores Ambientais
        ↓
Dados Espaciais / NDVI
        ↓
API Flask
        ↓
MongoDB Atlas
        ↓
Pandas
        ↓
Machine Learning
Decision Tree / Random Forest
        ↓
Dashboard Streamlit
        ↓
Alertas e Recomendações Inteligentes
Tecnologias Utilizadas
Python: linguagem principal do projeto;
Flask: criação da API para recebimento e integração dos dados;
MongoDB Atlas: banco de dados em nuvem para armazenamento das informações;
Pandas: tratamento, organização e análise dos dados;
Scikit-Learn: criação dos modelos de Machine Learning;
Decision Tree: modelo utilizado para classificação e recomendação;
Random Forest: modelo utilizado para comparação e melhoria das previsões;
Streamlit: desenvolvimento do dashboard interativo;
NDVI: indicador inspirado em observação espacial para análise da saúde da vegetação.
Inteligência Artificial
A solução utiliza modelos de Machine Learning para analisar variáveis ambientais e espaciais, como:
temperatura;
umidade do ar;
umidade do solo;
luminosidade;
NDVI.
Com base nesses dados, a IA pode:
prever a necessidade de irrigação;
indicar risco hídrico;
comparar resultados entre modelos;
apresentar nível de confiança da previsão;
apoiar a tomada de decisão do produtor.
Dashboard
O dashboard do SpaceFarm AI apresenta de forma visual e interativa:
indicadores ambientais;
histórico de medições;
módulo de observação espacial;
valor de NDVI;
risco hídrico;
recomendações de irrigação;
comparação entre modelos de IA.
Benefícios da Solução
Redução do desperdício de água;
Apoio à tomada de decisão baseada em dados;
Monitoramento contínuo da plantação;
Maior eficiência operacional;
Uso prático de conceitos de economia espacial;
Integração entre IoT, dados espaciais e Inteligência Artificial;
Contribuição para uma agricultura mais sustentável.
Instruções Básicas de Execução
1. Clonar o repositório
git clone <URL_DO_REPOSITORIO>
cd <NOME_DA_PASTA_DO_PROJETO>
2. Criar um ambiente virtual
python -m venv venv
3. Ativar o ambiente virtual
No Windows:
venv\Scripts\activate
No Linux ou macOS:
source venv/bin/activate
4. Instalar as dependências
pip install -r requirements.txt
5. Configurar as variáveis de ambiente
Crie um arquivo .env na raiz do projeto e configure as variáveis necessárias, como a conexão com o MongoDB Atlas:
MONGO_URI=<SUA_STRING_DE_CONEXAO_MONGODB>
6. Executar a API Flask
python app.py
Caso o arquivo principal da API tenha outro nome, substitua app.py pelo nome correto.
7. Executar o Dashboard Streamlit
streamlit run dashboard.py
Caso o dashboard esteja em outra pasta ou possua outro nome, ajuste o comando conforme a estrutura do projeto.
Estrutura Sugerida do Projeto
SpaceFarm-AI/
│
├── README.md
├── requirements.txt
├── app.py
├── dashboard.py
├── .env.example
│
├── data/
│   └── README.md
│
├── models/
│   └── README.md
│
├── src/
│   └── README.md
│
└── docs/
    └── README.md
Observação Sobre os READMEs das Pastas
Cada pasta do projeto deve possuir seu próprio arquivo README.md, seguindo o template definido para aquela seção da atividade.
O README.md da raiz deve conter obrigatoriamente:
nome do projeto;
proposta da solução;
funcionamento geral;
tecnologias utilizadas;
integrantes do grupo;
instruções básicas de execução.
Conclusão
O SpaceFarm AI demonstra como tecnologias de observação espacial, IoT e Inteligência Artificial podem ser combinadas para criar uma solução agrícola inteligente, eficiente e sustentável.
A plataforma contribui para o uso mais consciente da água, melhora o acompanhamento da saúde da vegetação e auxilia produtores na tomada de decisões com base em dados.