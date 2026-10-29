# WEEK 6 LESSON 12 - 22 SEP 2026

participants = [
    {
        "participant_id": "P001",
        "consent_given": True,
        "survey_complete": True,
        "wellbeing_category": "High"
    },
    {
        "participant_id": "P002",
        "consent_given": True,
        "survey_complete": True,
        "wellbeing_category": "Medium"
    },
    {
        "participant_id": "P003",
        "consent_given": False,
        "survey_complete": True,
        "wellbeing_category": "Low"
    },
    {
        "participant_id": "P004",
        "consent_given": True,
        "survey_complete": False,
        "wellbeing_category": "Medium"
    },
    {
        "participant_id": "P005",
        "consent_given": True,
        "survey_complete": True,
        "wellbeing_category": "High"
    }
]

def count_analysable_categories(participant_list):
    counts = {}

    for participant in participant_list:
        participant_is_analysable = (
            participant["consent_given"]
            and participant["survey_complete"]
        )

        if participant_is_analysable:
            category = participant["wellbeing_category"]
            counts[category] = counts.get(category, 0) + 1

    return counts

wellbeing_counts = count_analysable_categories(participants)

print("Wellbeing counts:", wellbeing_counts)


## NEW TOPIC: FILES

with open("survey_notes.txt", "r") as file:
    content = file.read()

print(content)


with open("survey_notes.txt", "r") as file:
    notes = file.readlines()

print(notes)
print("Number of notes:", len(notes))


with open("survey_notes.txt", "r") as file:
    notes = file.readlines()

for note_number, note in enumerate(notes, start=1):
    clean_note = note.strip()
    print(note_number, clean_note)


summary_lines = [
    "Analysis summary",
    "Three notes were reviewed.",
    "Further data cleaning is required."
]

with open("analysis_summary.txt", "w") as file:
    for line in summary_lines:
        file.write(line + "\n")


new_finding = "One note concerned missing responses."

with open("analysis_summary.txt", "a") as file:
    file.write(new_finding + "\n")

with open("analysis_summary.txt", "r") as file:
    updated_summary = file.read()

print(updated_summary)


try:
    with open("missing_file.txt", "r") as file:
        content = file.read()

    print(content)

except FileNotFoundError:
    print("The requested file could not be found.")


# WEEK 6 LESSON 13 - 23 SEP 2026

try:
    with open("survey_notes.txt", "r") as file:
        content = file.read()

    print(content)

except FileNotFoundError:
    print("The requested file could not be found.")


print("Starting program")

try:
    with open("missing_file.txt", "r") as file:
        content = file.read()

    print(content)

except FileNotFoundError:
    print("File not found")

print("Program Finished")


score_text = "Not recorded"

try:
    score = int(score_text)
    print("Score:", score)

except ValueError:
    print("The score could not be converted into a number.")

print("Data processing Finished.")


score_text = "8"

try:
    score = int(score_text)
    print("Score:", score)

except ValueError:
    print("The score could not be converted into a number.")

print("Data processing Finished.")


score_texts = ["7", "Not recorded", "5"]
valid_scores = []

for score_text in score_texts:
    try:
        score = int(score_text)
        valid_scores.append(score)

    except ValueError:
        print("Skipped invalid value:", score_text)

print("Valid scores:", valid_scores)


age_texts = ["16", "Missing", "15", "Unknown", "16"]
valid_ages = []
invalid_count = 0

for age_text in age_texts:
    try:
        age = int(age_text)
        valid_ages.append(age)

    except ValueError:
        invalid_count += 1

print("Valid ages:", valid_ages)
print("Invalid values:", invalid_count)


import csv

with open("survey_responses.csv", "r", newline="") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)


import csv

with open("survey_responses.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for participant in reader:
        print(participant)



import csv

total_score = 0
participant_count = 0

with open("survey_responses_2409.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for participant in reader:
        wellbeing_score = int(participant["wellbeing_score"])

        total_score += wellbeing_score

        participant_count += 1

mean_score = total_score / participant_count

print("Total score:", total_score)
print("Participant count:", participant_count)
print("Mean wellbeing score:", round(mean_score, 2))


# WEEK 6 LESSON 13 - 23 SEP 2026

import csv

total_score = 0
valid_score_count = 0
invalid_score_count = 0

with open("survey_responses.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for participant in reader:
        try:
            wellbeing_score = int(participant["wellbeing_score"])

            total_score += wellbeing_score
            valid_score_count += 1

        except ValueError:

            invalid_score_count += 1

mean_score = total_score / valid_score_count

print("Total valid score:", total_score)
print("Valid scores:", valid_score_count)
print("Invalid scores:", invalid_score_count)
print("Mean valid score:", round(mean_score, 2))


import csv

total_score = 0
valid_score_count = 0
invalid_score_count = 0
invalid_participants = []

with open("survey_responses.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for participant in reader:
        try:
            wellbeing_score = int(participant["wellbeing_score"])

            total_score += wellbeing_score
            valid_score_count += 1

        except ValueError:
            invalid_score_count += 1

            invalid_participants.append(participant["participant_id"])


print("Total valid score:", total_score)
print("Valid scores:", valid_score_count)
print("Invalid scores:", invalid_score_count)
print("Participants with invalid scores:", invalid_participants)

if valid_score_count > 0:
    mean_score = total_score / valid_score_count
    print("Mean valid score:", round(mean_score, 2))
else:
    print("A mean could not be calculated because there were no valid scores.")


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