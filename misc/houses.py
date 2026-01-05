# Define a list of dictionaries representing students with their names and houses
students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"},
] 

# Create a set to store unique houses
houses = set() 

# Iterate through the list of students and add their houses to the set
for student in students:
    houses.add(student["house"])

# Print the unique houses in alphabetical order
for house in sorted(houses):
    print(house)