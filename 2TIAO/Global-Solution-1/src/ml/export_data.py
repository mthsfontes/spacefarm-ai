import sys
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent
sys.path.append(str(ROOT_DIR))

import pandas as pd

from database.mongo_service import sensor_collection

data = list(sensor_collection.find())

for item in data:
    item.pop("_id", None)

df = pd.DataFrame(data)

df.to_csv(
    "ml/datasets/sensor_data.csv",
    index=False
)

print(f"{len(df)} registros exportados")
