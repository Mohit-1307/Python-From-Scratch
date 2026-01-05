# pytest is a testing framework for Python
import pytest
# Importing square function from Calculator module
from calculator import square 

# Main function to print the result of test_square function
# def main():
#     test_square()

# Function to test square function
# def test_square():
#     if square(2) != 4:
#         print("2 squared was not 4")
#     if square(3) != 9:
#         print("3 squared was not 9")

# Call main function to execute the code
# if __name__ == "__main__":
#     main()

#------------------------------------------------------------------------------------->

# Main function to print the result of test_square function
# def main():
#     test_square()

# Function to test square function
# def test_square():
      # Using try-except block to handle any exceptions
#     try:
#         # Using assert for testing
#         assert square(2) == 4
#     except:
#         print("2 squared was not 4")
#     try:
#         assert square(3) == 9
#     except:
#         print("3 squared was not 9")
#     try:
#         assert square(-2) == 4
#     except:
#         print("-2 squared was not 4")
#     try:
#         assert square(-3) == 9
#     except:
#         print("-3 squared was not 9")
#     try:
#         assert square(0) == 0
#     except:
#         print("0 squared was not 0")

# Call main function to execute the code
# if __name__ == "__main__":
#     main()

#------------------------------------------------------------------------------------->

# Function to test square function
# def test_square():
#     assert square(2) == 4
#     assert square(3) == 9
#     assert square(-2) == 4
#     assert square(-3) == 9
#     assert square(0) == 0

#------------------------------------------------------------------------------------->

# Function to test square function
# def test_positive():
#     assert square(2) == 4
#     assert square(3) == 9

# def test_negative():
#     assert square(-2) == 4
#     assert square(-3) == 9

# def test_zero():
#     assert square(0) == 0

#------------------------------------------------------------------------------------->

# Function to test square function
# def test_positive():
#     assert square(2) == 4
#     assert square(3) == 9

# def test_negative():
#     assert square(-2) == 4
#     assert square(-3) == 9

# def test_zero():
#     assert square(0) == 0

# def test_str():
#     with pytest.raises(TypeError):
#         square("cat")