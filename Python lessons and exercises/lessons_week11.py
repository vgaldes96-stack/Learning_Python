#    # WEEK 11 LESSON 20 - 10 NOV 2026

import pandas as pd
from pathlib import Path

file_path = Path(__file__).with_name("scores.csv")

df = pd.read_csv(file_path)

df["score_numeric"] = pd.to_numeric(df["score"], errors="coerce")

print(df)


## Select the rows whose numeric scores are within 0–10.

import pandas as pd
from pathlib import Path

file_path = Path(__file__).with_name("scores.csv")

df = pd.read_csv(file_path)

df["score_numeric"] = pd.to_numeric(df["score"], errors="coerce")

valid_mask = df["score_numeric"].between(0, 10)

valid_rows = df[valid_mask]

print(valid_mask)
print(valid_rows)


## mean of the valid numeric scores, number of valid rows, number of invalid rows

mean = valid_rows["score_numeric"].mean()

valid_count = len(valid_rows)

invalid_count = len(df) - len(valid_rows)

print(mean)
print(valid_count)
print(invalid_count)

## retrieve the invalid participant IDs

invalid_rows = df[~valid_mask]

invalid_ids = invalid_rows["participant_id"].tolist()

print(invalid_ids)