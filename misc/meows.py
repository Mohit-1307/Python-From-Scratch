# class Cat:
    
#     MEOWS = 3
    
#     def meow(self):
        
#         for _ in range(Cat.MEOWS):
#             print("meow")

# cat = Cat()
# cat.meow()

# ---------------------------------------------------------------------------------------------------------------------------------------->

# def meow(n: int):
    
#     for _ in range(n):
#         print("meow")

# number: int = int(input("Number: "))
# meow(number)

# ---------------------------------------------------------------------------------------------------------------------------------------->

# def meow(n: int) -> None:
    
#     for _ in range(n):
#         print("meow")

# number: int = int(input("Number: "))
# meows: str = meow(number)
# print(meows)

# ---------------------------------------------------------------------------------------------------------------------------------------->

# def meow(n: int) -> str:
    
#     """Meows n times."""
    
#     return "meow\n" * n

# number: int = int(input("Number: "))
# meows: str = meow(number)
# print(meows, end = "")

# ---------------------------------------------------------------------------------------------------------------------------------------->

# import sys

# If no arguments are provided, print "Meow" directly.
# if len(sys.argv) == 1:
#     print("Meow")

# If the "-n" flag and a number are provided, print "Meow" that many times.
# elif len(sys.argv) == 3 and sys.argv[1] == "-n":
    
#     n = int(sys.argv[2])
    
#     for _ in range(n):
        # print("Meow")

# If the arguments do not match the expected patterns, print a usage message.
# else:
#     print("usage: Meows.py")

# ---------------------------------------------------------------------------------------------------------------------------------------->

# import argparse for command-line argument parsing.
# import argparse

# # Create an ArgumentParser object to handle command-line arguments.
# parser = argparse.ArgumentParser(description = "Meows like a cat.")
# parser.add_argument("-n", default = 1, help = "Number of times to meow", type = int)
# args = parser.parse_args()

# # Print "Meow" the specified number of times.
# for _ in range(int(args.n)):
#     print("Meow")