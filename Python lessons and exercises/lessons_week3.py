## WEEK 3 LESSON 7 - 1 SEP 2026

for participant_number in range(0, 11, 2):

  print("Participant", participant_number, "selected")


responses = ["Yes", "No", "Yes"]

for response_number, response in enumerate(responses, start=1):
  print("Response", response_number, ":", response)


responses = ["Yes", "", "No", "Yes"]

for response_number, response in enumerate(responses, start=1):
  if response == "":
    continue

  print("Response", response_number, ":", response)


## WEEK 3 LESSON 8 - 3 SEP 2026 (continues from previous lesson)

survey_scores = [6, -1, 8, 4, -1, 7]

valid_count = 0
valid_scores = []

for score in survey_scores:
    if score == -1:
        continue

    valid_count += 1
    valid_scores.append(score)

print("Number of valid scores:", valid_count)
print("Valid scores:", valid_scores)


wellbeing_scores = [7, 99, 5, 8, 3, 99, 6]

valid_count = 0
valid_scores = []

for score in wellbeing_scores:
   if score == 99:
      continue

   valid_count += 1
   valid_scores.append(score)

print("Number of valid scores:", valid_count)
print("Valid scores:", valid_scores)


remaining_surveys = 4

while remaining_surveys > 1:
   print("Surveys remaining:", remaining_surveys)
   remaining_surveys -=1

print("Loop finished")


survey_number = 1

while survey_number <= 6:
  if survey_number == 4:
     survey_number += 1
     continue 

  print("Processing survey", survey_number)
  survey_number += 1


record_number = 1

while record_number <= 7:
   if record_number == 5:
      record_number += 1
      continue
   print("Processing record", record_number)
   record_number += 1


def display_survey_heading():
    print("Adolescent Wellbeing Survey")
    print("---------------------------")

display_survey_heading()
display_survey_heading()


def show_status():
   print("Data checked")
   print("Analysis ready")

show_status()
show_status()


def display_score(score):
   print("Survey score:", score)

display_score(7)
display_score(4)


def classify_score(score):
   if score >= 7:
      print(score, "High")
   elif 4 <= score <= 6:
      print(score, "Medium")
   else:
      print(score, "Low")

classify_score(8)
classify_score(5)
classify_score(2)


def show_participant(participant_number):
   print("Processing participant", participant_number)

show_participant(3)
show_participant(8)

# Functions with multiple parameters

def show_participant(participant_number, score):
    print("Participant", participant_number, "score:", score)

show_participant(1, 7)
show_participant(2, 4)


def show_response(participant_number, response):
   print("Participant", participant_number, "response:", response)

responses = ["Yes", "No", "Yes"]

for participant_number, response in enumerate(responses, start=1):
   show_response(participant_number, response)
