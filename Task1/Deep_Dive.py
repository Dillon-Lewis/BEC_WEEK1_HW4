students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]

# Task 1

for g in range(len(grades)):
    if grades[g] < 80:
        print("Students that need extra help:", students[g], grades[g], activities[g])


# Task 2
print("Students who did good:")

approved = []
approved.append(students[0])
approved.append(students[1])
approved.append(students[3])


# Task 3

print(approved)