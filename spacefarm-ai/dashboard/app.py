import sys
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent
sys.path.append(str(ROOT_DIR))

from ml.predict_service import predict_irrigation

import streamlit as st
from services.api_client import (
    get_latest_data,
    get_history
)
import pandas as pd
from streamlit_autorefresh import (
    st_autorefresh
)

data = get_latest_data()
prediction, confidence = (
    predict_irrigation(data)
)

history = get_history()
df = pd.DataFrame(history)

st.set_page_config(
    page_title="SpaceFarm AI",
    layout="wide"
)

st.title("🚀 SpaceFarm AI")

st.markdown("""
### Agricultura Preditiva Baseada em Observação Espacial

Monitoramento inteligente utilizando sensores IoT, dados espaciais e Inteligência Artificial para otimizar o uso de recursos agrícolas.
""")



data = get_latest_data()

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric(
    "🌡 Temperatura",
    f"{data['temperatura']} °C"
)

col2.metric(
    "💧 Umidade Ar",
    f"{data['umidade_ar']} %"
)

col3.metric(
    "🌱 Umidade Solo",
    f"{data['umidade_solo']} %"
)

col4.metric(
    "☀️ Luminosidade",
    data['luminosidade']
)

col5.metric(
    "🛰 NDVI",
    data['ndvi']
)

st.divider()

st.subheader(
    "🤖 Inteligência Artificial"
)

if prediction == 1:

    st.error(
        f"🚨 Irrigação Recomendada "
        f"({confidence:.0%})"
    )

else:

    st.success(
        f"✅ Irrigação Não Necessária "
        f"({confidence:.0%})"
    )
    
st.subheader(
    "📋 Motivos da Recomendação"
)

motivos = []

if data["umidade_solo"] < 35:
    motivos.append(
        "Baixa umidade do solo"
    )

if data["umidade_solo"] < 35:
    motivos.append(
        "Baixa umidade do solo"
    )
    
if data["ndvi"] < 0.5:
    motivos.append(
        "Vegetação em possível estresse"
    )
    
for motivo in motivos:
    st.write(
        f"• {motivo}"
    )
    
risk_score = 0

risk_score += data["temperatura"] * 1.5

risk_score += (
    100 - data["umidade_solo"]
)

risk_score += (
    (1 - data["ndvi"]) * 100
)

risk_score = min(
    int(risk_score),
    100
)

farm_score = (
    (data["umidade_solo"] * 0.4)
    +
    (data["ndvi"] * 100 * 0.4)
    +
    ((100 - risk_score) * 0.2)
)

farm_score = int(min(farm_score,100))

st.metric(
    "🌎 Índice Geral da Fazenda",
    f"{farm_score}/100"
)

st.subheader(
    "🌾 Risco Hídrico"
)

st.progress(
    risk_score / 100
)

st.write(
    f"{risk_score}%"
)

st.subheader(
    "💡 Recomendações"
)

if risk_score > 80:

    st.warning(
        "Realizar irrigação imediatamente."
    )

elif risk_score > 50:

    st.info(
        "Monitorar área nas próximas horas."
    )

else:

    st.success(
        "Condição adequada."
    )

st.subheader(
    "Status Atual da Fazenda"
)

if data["umidade_solo"] < 25:

    st.error(
        "⚠ Risco de estresse hídrico"
    )

elif data["umidade_solo"] < 40:

    st.warning(
        "🟡 Atenção ao solo"
    )

else:

    st.success(
        "🟢 Condição saudável"
    )


col6, col7 = st.columns(2)
with col6:
    st.subheader("Histórico de Temperatura")
    st.line_chart(
        df["temperatura"]
    )
    
with col7:
    st.subheader(
        "Histórico de Umidade do Solo"
    )
    st.line_chart(
        df["umidade_solo"]
    )

st.subheader(
    "Índice NDVI"
)

st.line_chart(
    df["ndvi"]
)



st_autorefresh(
    interval=15000,
    key="refresh"
)