    # WEEK 9 LESSON 16 - 28 OCT 2026

## Exercise 1

score_a = 2
score_b = 2
score_c = 2

total = score_a + score_b + score_c

mean_score = total / 3

print(mean_score)

print(mean_score >= 5)


# Exercise 2

score = 5

if score < 4:
    print("Low")

elif score < 7:
    print("Medium")

else:
    print("High")


## Exercise 3

scores = [6, 8, 4, 7, 5]

print(scores[0])

scores.append(9)

high_scores = []
total_high_scores = 0

for score in scores:
    if score >= 7:
        high_scores.append(score)
        total_high_scores += 1

print(high_scores)
print(total_high_scores)

# Exercise 4

def calculate_mean(total, count):
    mean_score = total / count
    return mean_score

result = calculate_mean(30, 5)
print(result)


## Exercise 5

participant = {
    "id": "P01",
    "group": "A",
    "score": 6
}

print(participant["score"])

participant["score"] = 8

participant["completed"] = True

print(participant.get("age", "Not recorded"))

## Follow-up exercise to practise return

def calculate_total(score_a, score_b):
    total = score_a + score_b
    return total

results = calculate_total(6, 8)
print(results)


## Another small exercise

def classify_score(score):
    if score < 4:
        return "Low"
    elif score < 7:
        return "Medium"
    else:
        return "High"

score_classification = classify_score(4)
print(score_classification)



# WEEK 10 LESSON 18 - 4 NOV 2026

scores = [6, 8, 4, 7, 5, 9]

def count_high_scores(scores):
    high_scores = 0

    for score in scores:
        if score >= 7:
            high_scores += 1
        
    return high_scores
    
result = count_high_scores(scores)
print(result)


## Exercise: Count completed dictionaries

participants = [
    {"id": "P01", "completed": False},
    {"id": "P02", "completed": True},
    {"id": "P03", "completed": True},
    {"id": "P04", "completed": False}
]

def count_completed(participants):
    total_completed = 0

    for participant in participants:
        if participant["completed"]:
            total_completed += 1

    return total_completed

result = count_completed(participants)
print(result)


## Exercise: Return the IDs of participants who completed the questionnaire

participants = [
    {"id": "P01", "completed": False},
    {"id": "P02", "completed": True},
    {"id": "P03", "completed": True},
    {"id": "P04", "completed": False}
]

def get_completed_ids(participants):
    completed_ids = []

    for participant in participants:
        if participant["completed"]:
            completed_ids.append(participant["id"])
    return completed_ids
        
result = get_completed_ids(participants)
print(result)


## Exercise: which participants completed the questionnaire and scored at least 7?

participants = [
    {"id": "P01", "completed": False, "score": 9},
    {"id": "P02", "completed": True,  "score": 7},
    {"id": "P03", "completed": True,  "score": 6},
    {"id": "P04", "completed": True,  "score": 8}
]

def get_eligible_ids(participants):
    eligible_ids = []

    for participant in participants:
        if participant["completed"] and participant["score"] >= 7:
            eligible_ids.append(participant["id"])
    return eligible_ids
        
result = get_eligible_ids(participants)
print(result)

## Exercise: calculate the mean score for participants who completed the questionnaire

participants = [
    {"id": "P01", "completed": False, "score": 9},
    {"id": "P02", "completed": True,  "score": 7},
    {"id": "P03", "completed": True,  "score": 6},
    {"id": "P04", "completed": True,  "score": 8}
]

def mean_completed_score(participants):
    completed_scores = []

    for participant in participants:
        if participant["completed"]:
            completed_scores.append(participant["score"])
    
    mean_score = sum(completed_scores) / len(completed_scores)
    return mean_score

mean_score = mean_completed_score(participants)
print(mean_score)


## Exercise: what if nobody completes the questionnaire?

participants = [
    {"id": "P01", "completed": False, "score": 9},
    {"id": "P02", "completed": True,  "score": 7},
    {"id": "P03", "completed": True,  "score": 6},
    {"id": "P04", "completed": True,  "score": 8}
]

def mean_completed_score(participants):
    completed_scores = []

    for participant in participants:
        if participant["completed"]:
            completed_scores.append(participant["score"])

    if not completed_scores:
        return None
    
    mean_score = sum(completed_scores) / len(completed_scores)
    return mean_score

mean_score = mean_completed_score(participants)
print(mean_score)
print(mean_completed_score([{"id": "P05", "completed": False, "score": 8}]))

## Exercise: read scores from a text file

from pathlib import Path
file_path = Path(__file__).with_name("scores.txt")
print(file_path)

scores = []

with open(file_path, "r") as file:
    for line in file:
        clean_line = line.strip()
        score = int(clean_line)
        scores.append(score)

print(scores)
