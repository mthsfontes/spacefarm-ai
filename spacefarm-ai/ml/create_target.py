import pandas as pd

df = pd.read_csv(
    "ml/datasets/sensor_data.csv"
)

df["risco_hidrico"] = (
    (df["temperatura"] * 0.3)
    +
    ((100 - df["umidade_solo"]) * 0.4)
    +
    ((df["luminosidade"] / 1000) * 10)
    +
    ((1 - df["ndvi"]) * 20)
)

df["irrigar"] = (
    df["risco_hidrico"] > 45
).astype(int)

df.to_csv(
    "ml/datasets/training_data.csv",
    index=False
)

print("Dataset gerado com sucesso")