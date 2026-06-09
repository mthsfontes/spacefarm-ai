import streamlit as st
from services.api_client import (
    get_latest_data,
    get_history
)
import pandas as pd
from streamlit_autorefresh import (
    st_autorefresh
)

history = get_history()
df = pd.DataFrame(history)

st.set_page_config(
    page_title="SpaceFarm AI",
    layout="wide"
)

st.title("🚀 SpaceFarm AI")

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