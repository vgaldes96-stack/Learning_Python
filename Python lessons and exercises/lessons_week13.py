# WEEK 13 LESSON 23 - 24 NOV 2026 (continued)

# Exercise: a record is eligible for analysis if its score is 
# between 0 and 10 inclusive and its questionnaire is complete.

import pandas as pd
from pathlib import Path

file_path = Path(__file__).with_name("survey_check.csv")

df = pd.read_csv(file_path)

df["score_numeric"] = pd.to_numeric(df["score"], errors="coerce")

valid_mask = df["score_numeric"].between(0, 10)
completed_mask = df["completed"] == "yes"

eligible_mask = valid_mask & completed_mask
eligible_rows = df.loc[eligible_mask, ["participant_id", "score_numeric"]]

eligible_count = eligible_mask.sum()
eligible_mean_score = eligible_rows["score_numeric"].mean()

print(eligible_rows)
print(eligible_count)
print(eligible_mean_score)


# Exercise: what happens when no records are eligible?

import pandas as pd
from pathlib import Path

file_path = Path(__file__).with_name("survey_check_no_eligible.csv")

df = pd.read_csv(file_path)

df["score_numeric"] = pd.to_numeric(df["score"], errors="coerce")

valid_mask = df["score_numeric"].between(0, 10)
completed_mask = df["completed"] == "yes"

eligible_mask = valid_mask & completed_mask
eligible_rows = df.loc[eligible_mask, ["participant_id", "score_numeric"]]

eligible_count = eligible_mask.sum()

if eligible_count > 0:
    eligible_mean_score = eligible_rows["score_numeric"].mean()
    print("Mean score:", eligible_mean_score)

else:
    print("Mean score unavailable: no eligible records")

print(eligible_rows)
print(eligible_count)


# Same exercise as above but this time using survey_check.csv 
# contaning completed questionnaires

import pandas as pd
from pathlib import Path

file_path = Path(__file__).with_name("survey_check.csv")

df = pd.read_csv(file_path)

df["score_numeric"] = pd.to_numeric(df["score"], errors="coerce")

valid_mask = df["score_numeric"].between(0, 10)
completed_mask = df["completed"] == "yes"

eligible_mask = valid_mask & completed_mask
eligible_rows = df.loc[eligible_mask, ["participant_id", "score_numeric"]]

eligible_count = eligible_mask.sum()

if eligible_count > 0:
    eligible_mean_score = eligible_rows["score_numeric"].mean()
    print("Mean score:", eligible_mean_score)

else:
    print("Mean score unavailable: no eligible records")

print(eligible_rows)
print(eligible_count)

# Create a review table showing why each record needs attention

import pandas as pd
from pathlib import Path

file_path = Path(__file__).with_name("survey_check.csv")

df = pd.read_csv(file_path)

df["score_numeric"] = pd.to_numeric(df["score"], errors="coerce")

valid_mask = df["score_numeric"].between(0, 10)
completed_mask = df["completed"] == "yes"
missing_score_mask = df["score_numeric"].isna()

out_of_range_mask = ~valid_mask & ~missing_score_mask
incompleted_mask = ~completed_mask

df["missing_score"] = missing_score_mask
df["out_of_range"] = out_of_range_mask
df["incomplete"] = incompleted_mask

review_mask = missing_score_mask | out_of_range_mask | incompleted_mask

review_rows = df.loc[review_mask, ["participant_id", "score_numeric", "missing_score", "out_of_range", "incomplete"]]

print(review_rows)