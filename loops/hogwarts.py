# Define a list of students
# students = ["Hermione", "Harry", "Ron"]

# Print the list of students
# print(students)
# Print each student in the list individually
# print(students[0])
# print(students[1])
# print(students[2])

# ------------------------------------------------------------------------>

# Loop through each student in the list and print their name
# for student in students:
#     print(student)

# ------------------------------------------------------------------------>

# Loop through each student in the list and print their name
# for i in range(len(students)):
#     print(i+1, students[i])

# ------------------------------------------------------------------------>

# Define a dictionary of students and their houses
# students = {
#     "Hermione": "Gryffindor",
#     "Harry": "Gryffindor",
#     "Ron": "Gryffindor",
#     "Draco": "Slytherin",
# }

# print the dictionary of students and their houses
# print(students)
# # Print the house of Hermione
# print(students["Hermione"])
# print(students["Harry"])
# print(students["Ron"])
# print(students["Draco"])

# ------------------------------------------------------------------------>

# Loop through each student in the dictionary and print their name
# for student in students:
#     print(student)

# ------------------------------------------------------------------------>

# Loop through each student in the dictionary and print their name and house
# for student in students:
#     print(student, students[student], sep = ", ")

# ------------------------------------------------------------------------>

# Define a list of students with additional information
# students = [
#     {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
#     {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
#     {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
#     {"name": "Draco", "house": "Slytherin", "patronus": None},
# ]

# Loop through each student in the list and print their name, house, and patronus if available
# for student in students:
#     print(student["name"], student["house"], student["patronus"], sep = ", ")