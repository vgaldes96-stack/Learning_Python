## WEEK 5 LESSON 8 - 15 SEP 2026

def count_large_purchases(amounts, minimum_amount):
    large_count = 0

    for amount in amounts:
        if amount >= minimum_amount:
            large_count += 1
    return large_count

purchase_amounts = [12, 45, 8, 60, 25, 38]

number_large = count_large_purchases(purchase_amounts, 30)
print("Number of purchases worth at least €30:", number_large)


def calculate_delivery_cost(order_total, free_delivery_threshold=50):

    if order_total >= free_delivery_threshold:
        return 0
    else:
        return 5

standard_cost = calculate_delivery_cost(40)
special_cost = calculate_delivery_cost(40, 30)

print("Standard delivery cost:", standard_cost)
print("Special delivery cost:", special_cost)


def calculate_late_fee(days_late, daily_fee=2):
    late_fee = days_late * daily_fee
    return late_fee

standard_fee = calculate_late_fee(4)
higher_fee = calculate_late_fee(
    4,
    daily_fee=3
)

print("Standard late fee:", standard_fee)
print("Higher late fee:", higher_fee)


def find_long_movies(durations, minimum_duration=120):
    long_movies = []

    for duration in durations:
        if duration >= minimum_duration:
            long_movies.append(duration)
    return long_movies

movie_durations = [95, 130, 110, 145, 85]

default_long_movies = find_long_movies(movie_durations)
custom_long_movies = find_long_movies(
    movie_durations,
    minimum_duration=100
)

print("Movies lasting at least 120 minutes:", default_long_movies)
print("Movies lasting at least 100 minutes:", custom_long_movies)


book = {
    "title": "Python Basics",
    "pages": 250,
    "available": True,
    "category": "Education"
}

print(book["title"])
# THE BELOW PRINT IS THE SAME AS THE ABOVE,
# BUT THE ABOVE PRODUCES A KeyError
#  AND THE BELOW RETURNS none INSTEAD OF CAUSING AN ERROR
print(book.get("author"))
book["pages"] = 275
book["category"] = "Education"
print(book)

print(book.get("pages"))
print(book.get("author", "Not provided"))
print("category" in book)
print(book.get("pages"))
print(book.get("author", "Not provided"))
print("category" in book)
print("Education" in book)


## WEEK 5 LESSON 8 - 15 SEP 2026

participant = {
    "participant_id": 1001,
    "age": 16,
    "survey_complete": True,
    "wellbeing_score": 7
}

print(participant.keys())
print(participant.values())

for key, value in participant.items():
    print(key, ":", value)


## Exercise: identify high-scoring wellbeing domains

domain_scores = {
    "emotional": 7,
    "school": 5,
    "family": 8,
    "peers": 4,
}

def find_high_scoring_domains(scores, threshold=7):
    high_domains = []

    for domain, score in scores.items():
        if score >= threshold:
            high_domains.append(domain)
    return high_domains

high_scoring_domains = find_high_scoring_domains(domain_scores)

print("High-scoring domains:", high_scoring_domains)


## NEW EXERCISE


participants = {
    "P001": {
        "age": 16,
        "survey_complete": True,
        "wellbeing_score": 7,
    },
    "P002": {
        "age": 15,
        "survey_complete": False,
        "wellbeing_score": 5
    }
}

print(participants["P002"]["age"])

participants["P001"]["wellbeing_score"] = 8

participants["P003"] = {
    "age": 16,
    "survey_complete": True,
    "wellbeing_score": 6,
    }

for participant_id, details in participants.items():
    print(participant_id, "score:", details["wellbeing_score"])


## Exercise using the participants dictionary above: 
## find completed participants

def find_completed_participants(participant_data):
    completed_ids = []

    for participant_id, details in participant_data.items():
        if details["survey_complete"]:
            completed_ids.append(participant_id)
    return completed_ids

completed_participants = find_completed_participants(participants)

print("Completed participants:", completed_participants)


## Exercise - list of dictionaries

participants = [
    {
        "participant_id": "P001",
        "age": 16,
        "survey_complete": True,
        "wellbeing_score": 8
    },
    {
        "participant_id": "P002",
        "age": 15,
        "survey_complete": False,
        "wellbeing_score": 5
    },
    {
        "participant_id": "P003",
        "age": 16,
        "survey_complete": True,
        "wellbeing_score": 6
    }
]

print(participants[1]["wellbeing_score"])

participants.append({
    "participant_id": "P004",
    "age": 15,
    "survey_complete": True,
    "wellbeing_score": 7 
})
 
for participant in participants:
    print(participant["participant_id"], "age:", participant["age"])


## Combined exercise: identify analysable records

survey_records = [
    {
        "participant_id": "P001",
        "survey_complete": True,
        "wellbeing_score": 8
    },
    {
        "participant_id": "P002",
        "survey_complete": False,
        "wellbeing_score": 7
    },
    {
        "participant_id": "P003",
        "survey_complete": True,
        "wellbeing_score": 4
    },
    {
        "participant_id": "P004",
        "survey_complete": True,
        "wellbeing_score": 99
    },
    {
        "participant_id": "P005",
        "survey_complete": True,
        "wellbeing_score": 6
    }
]

def find_analysable_participants(records, minimum_score=5):
    analysable_ids = []

    for participant in records:
        if (
            participant["survey_complete"]
            and participant["wellbeing_score"] != 99
            and participant["wellbeing_score"] >= minimum_score
        ):
            analysable_ids.append(participant["participant_id"])

    return analysable_ids

analysable_participants = find_analysable_participants(survey_records)

print("Analysable participants:", analysable_participants)


## WEEK 5 LESSON 11 - 17 SEP 2026

study_records = [
    {
        "participant_id": "S001",
        "consent_given": True,
        "survey_complete": True,
        "age": 16
    },
    {
        "participant_id": "S002",
        "consent_given": False,
        "survey_complete": True,
        "age": 16
    },
    {
        "participant_id": "S003",
        "consent_given": True,
        "survey_complete": False,
        "age": 16
    },
    {
        "participant_id": "S004",
        "consent_given": True,
        "survey_complete": True,
        "age": 14
    },
    {
        "participant_id": "S005",
        "consent_given": True,
        "survey_complete": True,
        "age": 15
    }
]

def find_eligible_participants(records, minimum_age=15):
    eligible_ids = []

    for participant in records:
        has_consent = participant["consent_given"]
        survey_is_complete = participant["survey_complete"]
        meets_minimum_age = participant["age"] >= minimum_age

        if has_consent and survey_is_complete and meets_minimum_age:
            eligible_ids.append(participant["participant_id"])

##      this logic can be written directly as:
##      if(
##          participant["consent_given"]
##          and participant["survey_complete"]
##          and participant["age"] >= minimum_age
##      ):
##          eligible_ids.append(participant["participant_id"])

    return eligible_ids

eligible_participants = find_eligible_participants(study_records)

print("Eligible participants:", eligible_participants)


participant = {
    "participant_id": "P001",
    "age": 16,
    "temporary_note": "Check later",
    "wellbeing_score": 7
}

print(len(participant))

removed_note = participant.pop("temporary_note")

print(removed_note)

del participant["age"]

print(participant)

print(len(participant))



participant = {
    "participant_id": "P002",
    "age": 15,
    "temporary_note": "Confirm consent",
    "wellbeing_score": 6
}

removed_note = participant.pop("temporary_note", "No note found")

print(removed_note)

removed_note = participant.pop("temporary_note", "No note found")

print(removed_note)

print(participant)


participant = {
    "participant_id": "P003",
    "age": 15,
    "wellbeing_score": 6,
}

participant.update({
    "age": 16,
    "wellbeing_score": 7,
    "survey_complete": True
})

print(participant)


wellbeing_categories = [
    "High",
    "Medium",
    "High",
    "Low",
    "Medium",
    "High",
    "Low"
]

category_counts = {}

for category in wellbeing_categories:
    if category in category_counts:
        category_counts[category] += 1
    else:
        category_counts[category] = 1

print(category_counts)

# Exercise: create a counting function

responses = [
    "Agree",
    "Disagree",
    "Agree",
    "Neutral",
    "Agree",
    "Neutral"   
]

def count_responses(response_list):
    counts = {}

    for response in response_list:
        counts[response] = counts.get(response, 0) + 1

    return counts

response_counts = count_responses(responses)

print("Response counts:", response_counts)

second_responses = ["Yes", "No", "Yes"]

print(count_responses(second_responses))