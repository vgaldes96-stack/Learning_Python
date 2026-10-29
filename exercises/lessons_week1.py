print("Hello, world!")
print("I am learning Python")
print(10)
print(5 + 3)
print("5 + 3")
print(10 + 5)
print("10" + "5")
#print("10" + 5)
age = 29
print(age)
name = "Alex"
age = 29
height = 1.70
print(name)
print(age)
print(height)
print(type(name))
print(type(age))
print(type(height))
gaming_monday = 2
gaming_tuesday = 4
total_gaming = gaming_monday + gaming_tuesday
print(total_gaming)
average_gaming = total_gaming / 2
print(average_gaming)
print(type(average_gaming))
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(3 ** 2)
print(3 % 2)
print(10 + 3 * 2)
print((10 + 3) * 2)
participants = 120
service_users = 45
percentage_users = (service_users / participants) * 100
print(percentage_users)
print(type(percentage_users))
completed_surveys = 75
age = 29
print(age > 18)
print(age < 18)
print(type(age > 18))
participant_age=16
if participant_age >= 18:
    print("Adult")
else:
    print("Under 18")

score = 5

if score >= 7:
    risk_level = "High"
elif score >= 4:
    risk_level = "Medium"
else:
    risk_level = "Low"
    print(risk_level)

    score = 5
if score >= 7:
    risk_level = "High"
elif score >= 4:
    risk_level = "Medium"
else:
    risk_level = "Low"
print(risk_level)

participant_age = 16

if participant_age >= 15 and participant_age <= 16:
    print("Eligible")
else:
    print("Not eligible")

    participant_age = 16

if 15 <= participant_age <= 16:
    print("Eligible")
else:
    print("Not eligible")

consent_given = False
if not consent_given:
    print("Cannot include participant")
else:
    print("Participant can be included")

participant_age=16
consent_given=True
if 15<=participant_age<=16 and consent_given:
    print("Include participant")
else:
    print("Do not inclued participant")

participant_age=16
consent_given=False
if 15<=participant_age<=16 and consent_given:
    print("Include participant")
else:
    print("Do not inclued participant")

participant_age=16
consent_given=False
if participant_age<15 or participant_age>16:
    print("Outside age range")
elif consent_given:
    print("Eligible")
else:
    print("No consent")

participant_age = 15
survey_complete = True
consent_given = True

if participant_age > 16 or participant_age < 15:
    print("Outside age range")
elif not survey_complete:
    print("Incomplete survey")
elif not consent_given:
    print("No consent")
else:
    print("Include participant")

score = 5
survey_complete = True

if not survey_complete:
    classification = "Cannot classify"
elif score >= 7:
    classification = "High"
elif 4 <= score <= 6:
    classification = "Medium"
else:
    classification = "Low"

print(classification)

score = 5
survey_complete = True

if not survey_complete:
    classification = "Cannot classify"
elif score >= 7:
    classification = "High"
elif 4 <= score <= 6:
    classification = "Medium"
else:
    classification = "Low"

print("Classification:", classification)

### Week 1 Lesson 4

ages = [15, 16, 14, 15, 16]

ages[2] = 16

print(ages)