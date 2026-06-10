# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href="https://www.fiap.com.br/">
  <img src="assets/logo-fiap.png" alt="FIAP" width="40%">
</a>
</p>

<br>

# SpaceFarm AI

## Grupo 62

## 👨‍🎓 Integrantes:
- Richard Wrobel dos Santos — RM573998
- Douglas Felicio da Silva — RM572312
- Matheus Fontes — RM570457

## 👩‍🏫 Professores:
### Tutor(a)
- Nome do Tutor(a)
### Coordenador(a)
- Nome do Coordenador(a)

## 🎬 Vídeo demonstrativo
- YouTube (não listado): https://youtu.be/b45cHwczqPU

## 📄 Documentação da entrega
- [PDF da entrega](docs/SpaceFarm_AI_Documentacao.pdf)

## 🗂 Estrutura do template TIAO-2026
- A atividade está documentada em [`1TIAO/Global-Solution-1`](1TIAO/Global-Solution-1), seguindo a hierarquia do [TEMPLATE-TIAO-2026](https://github.com/CaiqueFiap-2026/TEMPLATE-TIAO-2026)

---


---

## Proposta do Projeto

O **SpaceFarm AI** é uma plataforma de monitoramento agrícola baseada em **observação espacial**, **IoT**, **Inteligência Artificial** e **Ciência de Dados**.

A proposta da solução é auxiliar produtores rurais na identificação de situações de **estresse hídrico**, degradação da vegetação e necessidade de irrigação, utilizando dados ambientais e indicadores inspirados em tecnologias de observação da Terra por satélites.

O projeto aplica conceitos da **economia espacial** no agronegócio, demonstrando como dados derivados de observação terrestre podem apoiar decisões agrícolas mais eficientes, sustentáveis e baseadas em dados.

---

## Problema Abordado

Produtores rurais muitas vezes enfrentam dificuldades para identificar rapidamente quando uma plantação está sofrendo com falta de água, baixa umidade do solo ou sinais de perda de vigor vegetal.

A ausência de monitoramento contínuo pode causar:

- desperdício de água;
- decisões tardias de irrigação;
- redução da produtividade;
- aumento de custos operacionais;
- dificuldade na análise da saúde da vegetação.

---

## Funcionamento da Solução

O **SpaceFarm AI** funciona por meio da integração de dados ambientais, indicadores espaciais e modelos de Machine Learning.

O fluxo principal da solução é:

1. **Coleta de dados ambientais**  
   São considerados dados como temperatura, umidade do ar, umidade do solo e luminosidade.

2. **Uso de indicador espacial NDVI**  
   O sistema utiliza o **NDVI (Normalized Difference Vegetation Index)**, indicador amplamente associado à observação terrestre por satélites, para representar a saúde da vegetação.

3. **Envio dos dados para uma API**  
   Os dados são recebidos e tratados por uma API desenvolvida com **Flask**.

4. **Armazenamento em banco de dados**  
   As informações são armazenadas no **MongoDB Atlas**, permitindo persistência e consulta dos registros.

5. **Processamento e análise dos dados**  
   A biblioteca **Pandas** é utilizada para manipulação, organização e preparação dos dados.

6. **Aplicação de Inteligência Artificial**  
   Modelos de Machine Learning, como **Decision Tree** e **Random Forest**, analisam os dados e recomendam ações, como necessidade de irrigação.

7. **Visualização no Dashboard**  
   O usuário acompanha os indicadores por meio de um dashboard desenvolvido com **Streamlit**, contendo dados ambientais, histórico, NDVI, riscos hídricos e previsões da IA.

---

## Arquitetura da Solução

```text
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
```

---

## Tecnologias Utilizadas

- **Python**: linguagem principal do projeto;
- **Flask**: criação da API para recebimento e integração dos dados;
- **MongoDB Atlas**: banco de dados em nuvem para armazenamento das informações;
- **Pandas**: tratamento, organização e análise dos dados;
- **Scikit-Learn**: criação dos modelos de Machine Learning;
- **Decision Tree**: modelo utilizado para classificação e recomendação;
- **Random Forest**: modelo utilizado para comparação e melhoria das previsões;
- **Streamlit**: desenvolvimento do dashboard interativo;
- **NDVI**: indicador inspirado em observação espacial para análise da saúde da vegetação.

---

## Inteligência Artificial

A solução utiliza modelos de Machine Learning para analisar variáveis ambientais e espaciais, como:

- temperatura;
- umidade do ar;
- umidade do solo;
- luminosidade;
- NDVI.

Com base nesses dados, a IA pode:

- prever a necessidade de irrigação;
- indicar risco hídrico;
- comparar resultados entre modelos;
- apresentar nível de confiança da previsão;
- apoiar a tomada de decisão do produtor.

---

## Dashboard

O dashboard do **SpaceFarm AI** apresenta de forma visual e interativa:

- indicadores ambientais;
- histórico de medições;
- módulo de observação espacial;
- valor de NDVI;
- risco hídrico;
- recomendações de irrigação;
- comparação entre modelos de IA.

---

## Benefícios da Solução

- Redução do desperdício de água;
- Apoio à tomada de decisão baseada em dados;
- Monitoramento contínuo da plantação;
- Maior eficiência operacional;
- Uso prático de conceitos de economia espacial;
- Integração entre IoT, dados espaciais e Inteligência Artificial;
- Contribuição para uma agricultura mais sustentável.

---

## Instruções Básicas de Execução

### 1. Clonar o repositório e entrar na pasta do projeto

```bash
git clone https://github.com/mthsfontes/spacefarm-ai.git
cd spacefarm-ai/spacefarm-ai
```

### 2. Criar e ativar o ambiente virtual

```bash
python -m venv venv
source venv/bin/activate        # Linux/Mac
# venv\Scripts\activate         # Windows
```

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 4. Configurar as variáveis de ambiente

```bash
cp .env.example .env
# edite o .env e preencha o MONGO_URI com as credenciais do MongoDB Atlas
```

### 5. Executar (3 terminais)

```bash
python -m backend.app             # terminal 1 — API Flask (porta 5000)
python sensor_simulator.py        # terminal 2 — simulador de sensores IoT
streamlit run dashboard/app.py    # terminal 3 — dashboard (porta 8501)
```

### Alternativa com Docker

```bash
cp .env.example .env              # preencher MONGO_URI
docker compose up --build         # sobe API, dashboard e simulador
```

### Testes

```bash
pip install pytest mongomock
pytest tests/ -v
```

## Estrutura do Projeto

```text
spacefarm-ai/
│
├── README.md                  # Este arquivo
├── assets/                    # Imagens e logos
├── docs/                      # Entregáveis: PDF da documentação e vídeo
│
└── spacefarm-ai/              # Código-fonte do projeto
    ├── backend/               # API Flask (validação, rotas, serviços)
    ├── dashboard/             # Dashboard Streamlit
    ├── database/              # Conexão com MongoDB Atlas (via .env)
    ├── ml/                    # Pipeline de Machine Learning
    ├── data/                  # Geração de dataset sintético
    ├── tests/                 # Testes automatizados (pytest)
    ├── sensor_simulator.py    # Simulador de sensores IoT
    ├── Dockerfile / docker-compose.yml
    └── requirements.txt
```

Mais detalhes técnicos (rotas da API, pipeline de ML, CI) no [README do código](spacefarm-ai/README.md).

## Conclusão

O **SpaceFarm AI** demonstra como tecnologias de observação espacial, IoT e Inteligência Artificial podem ser combinadas para criar uma solução agrícola inteligente, eficiente e sustentável.

A plataforma contribui para o uso mais consciente da água, melhora o acompanhamento da saúde da vegetação e auxilia produtores na tomada de decisões com base em dados.
