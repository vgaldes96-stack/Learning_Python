### Week 2 Lesson 5

ages = [15, 16, 14, 15, 16]

ages[2] = 16

print(ages)

### Week2 Lesson 6

survey_scores=[3, 8, 6, 9, 4]

for score in survey_scores:
    if score >= 7:
        print(score, "High")
    elif 4 <= score <= 6:
        print(score, "Medium")
    else:
        print(score, "Low")


survey_scores = [3, 8, 6, 9, 4, 7, 2]

medium_count = 0
medium_scores = []
for score in survey_scores:
    if 4 <= score <= 6:
        medium_count += 1
        medium_scores.append(score)
print("Medium count:", medium_count)
print("Medium scores:", medium_scores)