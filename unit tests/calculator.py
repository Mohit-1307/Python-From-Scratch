# This function takes user input for x and prints its square.
def main(): 
    x = int(input("What's x? "))
    print("x squared is", square(x))


# This function takes an integer as an argument and returns its square.
def square(n):
    return n + n

# Call the main function to execute the code.
if __name__ == "__main__":
    main()