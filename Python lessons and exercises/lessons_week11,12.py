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

## retrieve the invalid participant IDs by reversing the mask with ~

invalid_rows = df[~valid_mask]

invalid_ids = invalid_rows["participant_id"].tolist()

print(invalid_ids)



# WEEK 12 LESSON 21 - 17 NOV 2026

## Combining 2 conditions in pandas

import pandas as pd
from pathlib import Path

file_path = Path(__file__).with_name("scores.csv")

df = pd.read_csv(file_path)

df["score_numeric"] = pd.to_numeric(df["score"], errors="coerce")

valid_mask = df["score_numeric"].between(0, 10)
valid_rows = df[valid_mask]

completed_mask = df["completed"] == "yes"

eligible_mask = valid_mask & completed_mask
eligible_rows = df[eligible_mask]

eligible_ids = eligible_rows["participant_id"].tolist()
print(eligible_ids)

mean = eligible_rows["score_numeric"].mean()
print(mean)


# Create a small review table of participants who completed the questionnaire but have an invalid score.

import pandas as pd
from pathlib import Path

file_path = Path(__file__).with_name("scores.csv")

df = pd.read_csv(file_path)

df["score_numeric"] = pd.to_numeric(df["score"], errors="coerce")

valid_mask = df["score_numeric"].between(0, 10)

completed_mask = df["completed"] == "yes"

completed_invalid_mask = ~valid_mask & completed_mask

completed_invalid_table = df.loc[completed_invalid_mask, ["participant_id", "score", "score_numeric"]]

print(completed_invalid_table)


# Create a small review table of who anyone who did not complete the questionnaire or has an invalid score.

import pandas as pd
from pathlib import Path

file_path = Path(__file__).with_name("scores.csv")

df = pd.read_csv(file_path)

df["score_numeric"] = pd.to_numeric(df["score"], errors="coerce")

valid_mask = df["score_numeric"].between(0, 10)

completed_mask = df["completed"] == "yes"

notcompleted_invalid_mask = ~valid_mask | ~completed_mask

notcompleted_invalid_table = df.loc[notcompleted_invalid_mask, ["participant_id", "completed", "score"]]

print(notcompleted_invalid_table)


# Reverse that mask with ~eligible_mask

import pandas as pd
from pathlib import Path

file_path = Path(__file__).with_name("scores.csv")

df = pd.read_csv(file_path)

df["score_numeric"] = pd.to_numeric(df["score"], errors="coerce")

valid_mask = df["score_numeric"].between(0, 10)

completed_mask = df["completed"] == "yes"

eligible_mask = valid_mask & completed_mask
notcompleted_invalid_mask = ~eligible_mask

notcompleted_invalid_table = df.loc[notcompleted_invalid_mask, ["participant_id", "completed", "score"]]

print(notcompleted_invalid_table)



# WEEK 12 LESSON 22 - 18 NOV 2026

import pandas as pd
from pathlib import Path

file_path = Path(__file__).with_name("scores.csv")

df = pd.read_csv(file_path)

df["score_numeric"] = pd.to_numeric(df["score"], errors="coerce")

valid_mask = df["score_numeric"].between(0, 10)

completed_mask = df["completed"] == "yes"

review_mask = ~valid_mask | ~completed_mask

eligible_mask = valid_mask & completed_mask
notcompleted_invalid_mask = ~eligible_mask

print(df.loc[review_mask, "participant_id"].tolist())
print(df.loc[notcompleted_invalid_mask, "participant_id"].tolist())


# Count the reasons records were flagged

import pandas as pd
from pathlib import Path

file_path = Path(__file__).with_name("survey_check.csv")

df = pd.read_csv(file_path)

df["score_numeric"] = pd.to_numeric(df["score"], errors="coerce")

valid_mask = df["score_numeric"].between(0, 10)
completed_mask = df["completed"] == "yes"
missing_score_mask = df["score_numeric"].isna()

missing_count = missing_score_mask.sum()

out_of_range_mask = ~valid_mask & ~missing_score_mask
out_of_range_count = out_of_range_mask.sum()

incompleted_mask = ~completed_mask
incomplete_count = incompleted_mask.sum()

review_mask = missing_score_mask | ~valid_mask | incompleted_mask
review_count = review_mask.sum()

print("Missing scores:", missing_count)
print("Numeric scores outside 0-10:", out_of_range_count)
print("Incomplete questionanires:", incomplete_count)
print("Records that neew review:", review_count)