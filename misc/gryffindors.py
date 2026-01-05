# students = [
#     {"name": "Hermione", "house": "Gryffindor"},
#     {"name": "Harry", "house": "Gryffindor"},
#     {"name": "Ron", "house": "Gryffindor"},
#     {"name": "Draco", "house": "Slytherin"},
# ]

# # Print all the names of the Gryffindors in alphabetical order using list comprehension
# gryffindors = [
#     student["name"] for student in students if student["house"] == "Gryffindor"
# ]

# for gryffindor in sorted(gryffindors):
#     print(gryffindor)

# ---------------------------------------------------------------------------------------------------------------------------------------->

# students = [
#     {"name": "Hermione", "house": "Gryffindor"},
#     {"name": "Harry", "house": "Gryffindor"},
#     {"name": "Ron", "house": "Gryffindor"},
#     {"name": "Draco", "house": "Slytherin"},
# ]

# # Filter the list of students to include only those in Gryffindor using filter and a lambda function
# gryffindors = filter(lambda s: s["house"] == "Gryffindor", students)

# # Sort the names in alphabetical order and print each name
# for gryffindor in sorted(gryffindors, key = lambda student: student["name"]):
#     print(gryffindor["name"])

# ---------------------------------------------------------------------------------------------------------------------------------------->

# students = ["Hermione", "Harry", "Ron"]

# Use list comprehension to create a new list of dictionaries, each representing a Gryffindor student
# gryffindors = [{"name": student, "house": "Gryffindor"} for student in students]

# print(gryffindors)

# ---------------------------------------------------------------------------------------------------------------------------------------->

# students = ["Hermione", "Harry", "Ron"]

# Use a dictionary comprehension to create a new dictionary, where the keys are the students and the values are their houses
# gryffindors = {student: "Gryffindor" for student in students}

# print(gryffindors)

# ---------------------------------------------------------------------------------------------------------------------------------------->

# students = ["Hermione", "Harry", "Ron"]

# for i in range(len(students)):
#     print(i+1, students[i])

# ---------------------------------------------------------------------------------------------------------------------------------------->

# students = ["Hermione", "Harry", "Ron"]

# for i, student in enumerate(students, start = 1):
#     print(i, student)