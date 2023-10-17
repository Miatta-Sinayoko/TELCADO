# Multiple Assignment
x, y = 5, 11

# Destructuring in for loops
student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}

for student, attendance in student_attendance.items():
    print(student, attendance)

# Another example
people = [("Bob", 42, "Mechanic"), ("James", 24, "Artist"), ("Harry", 32, "Lecturer")]

for name, age, profession in people:
    print(name, age, profession)

# Ignoring values with underscore
person = ("Bob", 42, "Mechanic")
name, _, profession = person

print(name, profession)  # Bob Mechanic

# Collecting values
head, *tail = [1, 2, 3, 4, 5]

print(head)  # 1
print(tail)  # [2, 3, 4, 5]

*head, tail = [1, 2, 3, 4, 5]

print(head)  # [1, 2, 3, 4]
print(tail)  # 5
# Multiple Assignment
# Assign the values 5 and 11 to the variables x and y
x, y = 5, 11

# Destructuring in for loops
# Iterate over the student_attendance dictionary and print the student name and attendance
student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}
for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")

# Another example
# Iterate over the people list and print the name, age, and profession of each person
people = [("Bob", 42, "Mechanic"), ("James", 24, "Artist"), ("Harry", 32, "Lecturer")]
for name, age, profession in people:
    print(f"{name}: {age}, {profession}")

# Ignoring values with underscore
# Assign the first and third values of the person tuple to the variables name and profession
person = ("Bob", 42, "Mechanic")
name, _, profession = person

# Print the name and profession
print(f"{name}: {profession}")  # Bob Mechanic

# Collecting values
# Assign the first value of the list to the variable head and the remaining values to the variable tail
head, *tail = [1, 2, 3, 4, 5]

# Print the head and tail
print(head)  # 1
print(tail)  # [2, 3, 4, 5]

# Assign the remaining values of the list to the variable head and the last value to the variable tail
*head, tail = [1, 2, 3, 4, 5]

# Print the head and tail
print(head)  # [1, 2, 3, 4]
print(tail)  # 5
