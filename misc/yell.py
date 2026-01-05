# def main():
#     yell("This", "is", "CS50")

# This function takes an arbitrary number of arguments (words) and prints them in uppercase.
# def yell(*words):
    
    # Create an empty list to store the uppercased words.
    # uppercased = []
    
    # Iterate over each word and convert it to uppercase and append it to the list.
    # for word in words:
    #     uppercased.append(word.upper())
    
    # Print the uppercased words in a single line separated by spaces.
#     print(*(uppercased))

# if __name__ == "__main__":
#     main()

# ---------------------------------------------------------------------------------------------------------------------------------------->

# Improved version of the same function using the built-in map function.
# def main():
#     yell("This", "is", "CS50")

# This function takes an arbitrary number of arguments (words) and prints them in uppercase.
# def yell(*words):
    
    # Use the map function to convert each word to uppercase and print them in a single line separated by spaces.
#     uppercased = map(str.upper, words)
#     print(*(uppercased))

# if __name__ == "__main__":
#     main()

# ---------------------------------------------------------------------------------------------------------------------------------------->

# Improved version of the same function using list comprehension.
# def main():
#     yell("This", "is", "CS50")

# This function takes an arbitrary number of arguments (words) and prints them in uppercase.
# def yell(*words):
    
    # Use a list comprehension to convert each word to uppercase and print them in a single line separated by spaces.
    # uppercased = [word.upper() for word in words]
    # print(*(uppercased))

# if __name__ == "__main__":
#     main()