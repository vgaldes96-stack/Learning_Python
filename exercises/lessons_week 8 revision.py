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

