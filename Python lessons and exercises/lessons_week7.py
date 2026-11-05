# WEEK 7 LESSON 15 - 29 SEP 2026

## Last excercise done in previous lesson

import csv

valid_participants = []
invalid_participants = []

with open("survey_responses.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for participant in reader:
        try:
            cleaned_participant = {
                "participant_id": participant["participant_id"],
                "age": int(participant["age"]),
                "wellbeing_score": int(participant["wellbeing_score"])
            }

            valid_participants.append(cleaned_participant)

        except ValueError:
            invalid_participants.append(participant["participant_id"])

print("Valid participant records:")
for participant in valid_participants:
    print(participant)

print("Invalid participants:", invalid_participants)

fieldnames = ["participant_id", "age", "wellbeing_score"]

with open("cleaned_survey_responses.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(valid_participants)

print("Cleaned CSV file created.")

### pandas and DataFrames

import pandas as pd

print("pandas version:", pd.__version__)

#### Reading your first CSV with pandas

import pandas as pd

survey_data = pd.read_csv("cleaned_survey_responses.csv")

print(survey_data)
print(type(survey_data))


#### Inspecting your DataFrame

print("Rows and columns:", survey_data.shape)
print("Column names:", survey_data.columns.tolist())

#### Selecting one column

print(survey_data["wellbeing_score"])

print(survey_data["age"])


# WEEK 8 LESSON 15 (continued previous lesson) - 8 Oct 2026


print(survey_data[["participant_id", "age"]])


survey_data = pd.read_csv("cleaned_survey_responses.csv")

print(survey_data[["participant_id", "wellbeing_score"]])


## Calculating a mean from a column

mean_score = survey_data["wellbeing_score"].mean()

print("Mean wellbeing score:", mean_score)


print(survey_data["age"] == 16)

participants_aged_16 = survey_data[survey_data["age"] == 16]

print(participants_aged_16)


selected_participants = survey_data[survey_data["wellbeing_score"] >= 7]

print(selected_participants)
