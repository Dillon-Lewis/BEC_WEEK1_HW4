# Task1

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

print("Students who submitted on time:")

for student in attended:
    if student in submitted:
        print(student)


# Task2

print("Are the lists equal:")
print(submitted is attended)

# Task3

print("Those who didn't submit there assignments:")

attended.remove("Eve")
attended.remove("Frank")
print(attended)
