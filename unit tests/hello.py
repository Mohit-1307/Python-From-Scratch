# Main function to execute the code
def main():
    name = input("What's your name? ")
    print(hello(name))

# Function to print Hello message
def hello(to = "World"):
    return f"Hello, {to}"

# Call the main function to execute the code
if __name__ == "__main__":
    main()