# Task 1

print("grades:")
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
print(grades)
print("grades in decending order:")
grades.sort(reverse=True)
print(grades)


# Task 2

print('Average grade in the class:')
total = sum(grades)
amount = len(grades)
Mean = total / amount
print(Mean)


# Task 3

print("The Unlucky few that Failed:")

Stud1 = grades.pop(7)
grades.insert(7, "Failed")

Stud2 = grades.pop(8)
grades.insert(8, "Failed")

Stud3 = grades.pop(9)
grades.insert(9, "Failed")
print(grades)


