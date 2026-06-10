import json
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent
sys.path.append(str(ROOT_DIR))

import pandas as pd
import plotly.graph_objects as go
import requests
import streamlit as st
from streamlit_autorefresh import st_autorefresh

from ml.predict_service import model, predict_irrigation
from services.api_client import (
    get_latest_data,
    get_history
)

METRICS_PATH = ROOT_DIR / "ml" / "models" / "model_metrics.json"

FEATURE_LABELS = {
    "temperatura": "Temperatura",
    "umidade_ar": "Umidade do Ar",
    "umidade_solo": "Umidade do Solo",
    "luminosidade": "Luminosidade",
    "ndvi": "NDVI"
}

st.set_page_config(
    page_title="SpaceFarm AI",
    page_icon="🚀",
    layout="wide"
)

st_autorefresh(
    interval=15000,
    key="refresh"
)

st.title("🚀 SpaceFarm AI")

st.markdown("""
#### Agricultura Preditiva Baseada em Observação Espacial

Monitoramento inteligente utilizando sensores IoT, dados espaciais e Inteligência Artificial para otimizar o uso de recursos agrícolas.
""")

try:
    data = get_latest_data()
    history = get_history()

except requests.exceptions.RequestException:
    st.error(
        "⚠ Não foi possível conectar à API. "
        "Verifique se o backend está rodando (python -m backend.app)."
    )
    st.stop()

if not isinstance(data, dict) or "temperatura" not in data:
    st.warning(
        "Ainda não há leituras no banco. "
        "Execute o simulador (python sensor_simulator.py) para gerar dados."
    )
    st.stop()

prediction, confidence = (
    predict_irrigation(data)
)

df = pd.DataFrame(history[::-1])

if "timestamp" in df.columns:
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df = df.set_index("timestamp")

with st.sidebar:

    st.header("🚀 SpaceFarm AI")

    st.caption(
        "Observação espacial + IoT + IA "
        "aplicadas à agricultura"
    )

    st.success("🟢 API conectada")

    st.metric(
        "Leituras recentes",
        len(df)
    )

    if isinstance(df.index, pd.DatetimeIndex) and len(df):
        st.caption(
            f"Última leitura: "
            f"{df.index.max():%d/%m/%Y %H:%M:%S}"
        )

# ----------------------------------------
# 1. Monitoramento Ambiental
# ----------------------------------------

st.header("🌡 Monitoramento Ambiental")

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

# ----------------------------------------
# 2. Módulo de Observação Espacial
# ----------------------------------------

st.header("🛰 Módulo de Observação Espacial")

ndvi = data["ndvi"]

media_ndvi = (
    df["ndvi"].mean()
    if "ndvi" in df.columns
    else ndvi
)

col_ndvi, col_grafico = st.columns([1, 2])

with col_ndvi:

    st.metric(
        "NDVI atual",
        ndvi,
        delta=f"{ndvi - media_ndvi:+.2f} vs média recente"
    )

    if ndvi >= 0.6:
        st.success("🟢 Vegetação saudável")

    elif ndvi >= 0.4:
        st.warning("🟡 Vegetação em condição moderada")

    else:
        st.error("🔴 Possível estresse ou degradação")

with col_grafico:

    st.caption("Evolução do NDVI nas últimas leituras")

    if "ndvi" in df.columns:
        st.line_chart(df["ndvi"])

st.caption(
    "O NDVI (Normalized Difference Vegetation Index) é o índice usado por "
    "satélites de observação terrestre para medir a saúde da vegetação: "
    "quanto mais próximo de 1, mais densa e saudável é a cobertura vegetal."
)

st.divider()

# ----------------------------------------
# 3. Risco Hídrico
# ----------------------------------------

st.header("🌾 Risco Hídrico")

# Cada componente vai de 0 a 100; o score final é a média ponderada
risco_solo = 100 - data["umidade_solo"]

risco_temperatura = min(
    max((data["temperatura"] - 20) * 5, 0),
    100
)

risco_vegetacao = (1 - data["ndvi"]) * 100

risk_score = int(
    (risco_solo * 0.45)
    + (risco_temperatura * 0.25)
    + (risco_vegetacao * 0.30)
)

farm_score = (
    (data["umidade_solo"] * 0.4)
    +
    (data["ndvi"] * 100 * 0.4)
    +
    ((100 - risk_score) * 0.2)
)

farm_score = int(min(farm_score, 100))

col_risco, col_fazenda = st.columns(2)

with col_risco:

    gauge_risco = go.Figure(go.Indicator(
        mode="gauge+number",
        value=risk_score,
        title={"text": "Risco Hídrico (%)"},
        gauge={
            "axis": {"range": [0, 100]},
            "bar": {"color": "#1f4e79"},
            "steps": [
                {"range": [0, 50], "color": "#c8e6c9"},
                {"range": [50, 80], "color": "#fff9c4"},
                {"range": [80, 100], "color": "#ffcdd2"}
            ]
        }
    ))

    gauge_risco.update_layout(height=260, margin=dict(t=40, b=10))

    st.plotly_chart(gauge_risco, use_container_width=True)

with col_fazenda:

    gauge_fazenda = go.Figure(go.Indicator(
        mode="gauge+number",
        value=farm_score,
        title={"text": "Índice Geral da Fazenda"},
        gauge={
            "axis": {"range": [0, 100]},
            "bar": {"color": "#2e7d32"},
            "steps": [
                {"range": [0, 40], "color": "#ffcdd2"},
                {"range": [40, 70], "color": "#fff9c4"},
                {"range": [70, 100], "color": "#c8e6c9"}
            ]
        }
    ))

    gauge_fazenda.update_layout(height=260, margin=dict(t=40, b=10))

    st.plotly_chart(gauge_fazenda, use_container_width=True)

if risk_score > 80:

    st.warning(
        "💡 Recomendação: realizar irrigação imediatamente."
    )

elif risk_score > 50:

    st.info(
        "💡 Recomendação: monitorar a área nas próximas horas."
    )

else:

    st.success(
        "💡 Recomendação: condição adequada, nenhuma ação necessária."
    )

st.divider()

# ----------------------------------------
# 4. Inteligência Artificial
# ----------------------------------------

st.header("🤖 Inteligência Artificial")

if prediction == 1:

    st.error(
        f"🚨 Irrigação Recomendada "
        f"(confiança: {confidence:.0%})"
    )

else:

    st.success(
        f"✅ Irrigação Não Necessária "
        f"(confiança: {confidence:.0%})"
    )

col_motivos, col_importancia = st.columns(2)

with col_motivos:

    st.subheader("📋 Motivos da Recomendação")

    motivos = []

    if data["umidade_solo"] < 35:
        motivos.append(
            "Baixa umidade do solo"
        )

    if data["temperatura"] > 32:
        motivos.append(
            "Temperatura elevada"
        )

    if data["ndvi"] < 0.5:
        motivos.append(
            "Vegetação em possível estresse"
        )

    if not motivos:
        motivos.append(
            "Condições dentro da normalidade"
        )

    for motivo in motivos:
        st.write(
            f"• {motivo}"
        )

with col_importancia:

    st.subheader("🔍 O que a IA mais considera")

    importancias = pd.Series(
        model.feature_importances_,
        index=[
            FEATURE_LABELS.get(nome, nome)
            for nome in model.feature_names_in_
        ]
    ).sort_values(ascending=False)

    st.bar_chart(importancias)

    st.caption(
        "Importância de cada variável na decisão do modelo (Decision Tree)."
    )

st.subheader("⚖️ Comparação de Modelos")

if METRICS_PATH.exists():

    metricas = json.loads(
        METRICS_PATH.read_text(encoding="utf-8")
    )

    metricas_df = (
        pd.DataFrame(metricas)
        .set_index("Modelo")
    )

    st.dataframe(
        metricas_df.style.format("{:.1%}"),
        use_container_width=True
    )

    st.caption(
        "Métricas calculadas em dados de teste (20% do dataset). "
        "O modelo em produção é a Decision Tree."
    )

else:

    st.info(
        "Execute `python ml/compare_models.py` para gerar a comparação de modelos."
    )

st.divider()

# ----------------------------------------
# 5. Histórico
# ----------------------------------------

st.header("📈 Histórico de Leituras")

if not df.empty:

    col6, col7 = st.columns(2)

    with col6:
        st.subheader("Temperatura")
        st.line_chart(
            df["temperatura"]
        )

    with col7:
        st.subheader("Umidade do Solo")
        st.line_chart(
            df["umidade_solo"]
        )
