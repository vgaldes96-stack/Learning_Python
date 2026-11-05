## WEEK 4 LESSON 9 - 9 SEP 2026

def show_response(participant_number, response):
    print("Participant", participant_number, "response:", response)

responses = ["Yes", "No", "Yes"]

for participant_number, response in enumerate(responses, start=1):
    show_response(participant_number, response)


survey_scores = [3, 8, 6, 9, 4]

def classify_score(score):
    if score >= 7:
        return "High"
    elif 4 <= score <= 6:
        return "Medium"
    else:
        return "Low"

for participant_number, score in enumerate(survey_scores, start=1):
    classification = classify_score(score)
    print("Participant number", participant_number, ":", classification)


def count_high_scores(scores):
    high_count = 0

    for score in survey_scores:
        if score >= 7:
            high_count += 1
    return high_count

survey_scores = [3, 8, 6, 9, 4]

high_count = count_high_scores(survey_scores)
print("Number of high scores:", high_count)


def count_valid_scores(scores):
    valid_count = 0

    for score in scores:
        if score != 99:
            valid_count += 1

    return valid_count

wellbeing_scores = [7, 99, 5, 8, 99,6]

number_valid = count_valid_scores(wellbeing_scores)

print("Number of valid scores:", number_valid)


def get_valid_scores(scores):
    valid_scores = []

    for score in scores:
        if score != 99:
            valid_scores.append(score)

    return valid_scores

stress_scores = [4, 99, 7, 6, 99, 8]

clean_scores = get_valid_scores(stress_scores)

print("valid stress scores:", clean_scores)


def calculate_valid_mean(scores):
    valid_scores = []

    for score in scores:
        if score != 99:
            valid_scores.append(score)

    mean_valid_score = sum(valid_scores) / len(valid_scores)

    return mean_valid_score

wellbeing_scores = [7, 99, 5, 8, 99, 6]

mean_score = calculate_valid_mean(wellbeing_scores)
print("Mean valid score:", mean_score)


def calculate_completion_rate(statuses):
    complete_count = 0

    for status in statuses:
        if status == "Complete":
            complete_count += 1

    percentage_completion_rate = complete_count / len(statuses) * 100

    return percentage_completion_rate

survey_statuses = ["Complete", "Incomplete", "Complete", "Complete", "Incomplete"]

completion_rate = calculate_completion_rate(survey_statuses)

print("Completion rate:", completion_rate, "%")


def find_busy_days(visitor_counts):
    busy_days = []

    for day_number, visitors in enumerate(visitor_counts, start=1):
        if visitors >= 100:
            busy_days.append(day_number)

    return busy_days

daily_visitors = [85, 120, 76, 143, 98]

busy_day_numbers = find_busy_days(daily_visitors)
print("Busy days:", busy_day_numbers)