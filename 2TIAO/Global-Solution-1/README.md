# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href="https://www.fiap.com.br/">
  <img src="../../assets/logo-fiap.png"
       alt="FIAP - Faculdade de Informática e Administração Paulista"
       width="40%">
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

## 📜 Descrição

O **SpaceFarm AI** é uma plataforma de agricultura preditiva baseada em **observação espacial**, **IoT**, **Inteligência Artificial** e **Ciência de Dados**, desenvolvida para a Global Solution 2026.1 (tema: economia espacial).

Produtores rurais têm dificuldade para identificar rapidamente situações de **estresse hídrico** e degradação da vegetação. O SpaceFarm AI resolve isso integrando leituras de sensores ambientais (temperatura, umidade do ar, umidade do solo e luminosidade) com o **NDVI** — índice de saúde da vegetação usado por satélites de observação da Terra.

O fluxo da solução: um simulador de sensores IoT envia leituras para uma **API Flask**, que valida e persiste os dados no **MongoDB Atlas**. Os dados alimentam modelos de **Machine Learning** (Decision Tree e Random Forest, com 98% de acurácia em teste) que recomendam irrigação com nível de confiança e explicabilidade (importância das variáveis). Um **dashboard Streamlit** exibe tudo em tempo real: monitoramento ambiental, módulo de observação espacial, risco hídrico, previsões da IA e comparação entre modelos.

## 📁 Estrutura de pastas

Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

- <b>docs</b>: documentação da entrega — [PDF completo do projeto](docs/SpaceFarm_AI_Documentacao.pdf) (arquitetura, códigos principais, dashboards e decisões do grupo) e [vídeo demonstrativo](docs/SpaceFarm_AI_Video.mp4).

- <b>src</b>: todo o código fonte desenvolvido — `backend/` (API Flask), `dashboard/` (Streamlit), `ml/` (pipeline de Machine Learning: exportação, geração de alvo, treino, comparação e predição), `database/` (conexão MongoDB Atlas via `.env`), `data/` (gerador de dataset sintético), `tests/` (14 testes com pytest), `sensor_simulator.py` (simulador IoT), além de `Dockerfile` e `docker-compose.yml`.

- <b>data</b>: dados utilizados no projeto — `sensor_dataset.json` (base sintética), `sensor_data.csv` (leituras exportadas do MongoDB) e `training_data.csv` (dataset de treino com a variável-alvo).

- <b>README.md</b>: este arquivo, guia geral do projeto.

## 📎 Links e Observações

- <b>Listagem de Links</b>:
  - 🎬 Vídeo demonstrativo (YouTube, não listado): https://youtu.be/b45cHwczqPU
  - 💻 Repositório: https://github.com/mthsfontes/spacefarm-ai
  - 📄 PDF da entrega: [docs/SpaceFarm_AI_Documentacao.pdf](docs/SpaceFarm_AI_Documentacao.pdf)

- <b>Explicação de decisões técnicas</b>: a Decision Tree foi mantida como modelo em produção pela interpretabilidade e desempenho equivalente ao Random Forest (98,0% vs 98,3% de acurácia em teste); as credenciais do banco ficam fora do código (`.env`); a API valida todas as leituras antes de persistir; CI no GitHub Actions executa os testes a cada push.

- <b>Observações Gerais</b>: o grupo aceita participar da competição — **QUERO CONCORRER**.

## 🔧 Como executar o código

Pré-requisitos: Python 3.12+ e uma conta no MongoDB Atlas (ou Docker).

```bash
git clone https://github.com/mthsfontes/spacefarm-ai.git
cd spacefarm-ai/2TIAO/Global-Solution-1/src

python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt

cp .env.example .env              # preencher MONGO_URI

python -m backend.app             # terminal 1 — API (porta 5000)
python sensor_simulator.py        # terminal 2 — sensores IoT
streamlit run dashboard/app.py    # terminal 3 — dashboard (porta 8501)
```

Alternativa com Docker: `docker compose up --build` (sobe API, dashboard e simulador).

Testes: `pip install pytest mongomock && pytest tests/ -v` (14 testes, também executados via GitHub Actions).

## 🗃 Histórico de lançamentos

* 1.0.0 - 09/06/2026 - Entrega da Global Solution 2026.1

## 📋 Licença

Projeto acadêmico desenvolvido para a Global Solution FIAP 2026.1.
