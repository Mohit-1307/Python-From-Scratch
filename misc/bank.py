# balance = 0 

# def main():
    
#     print("Balance:", balance)
#     deposit(100)
#     withdraw(50)
#     print("Balance:", balance)

# def deposit(amount):
    
#     global balance
#     balance += amount

# def withdraw(amount):
    
#     global balance
#     balance -= amount

# if __name__ == "__main__":
#     main()

# -------------------------------------------------------------------------------->

# Demonstrating the use of a class to implement a bank account
# class Account:
    
#     # Initialize the balance to 0 in the constructor method.
#     def __init__(self):
#         self._balance = 0
    
#     # Getter method for the balance.
#     # The @property decorator allows us to access the balance attribute directly.
#     @property
#     def balance(self):
#         return self._balance
    
#     def deposit(self, amount):
#         self._balance += amount

#     def withdraw(self, amount):
#         self._balance -= amount

# def main():
#     account = Account()
#     print("Balance:", account.balance)
#     account.deposit(100)
#     account.withdraw(50)
#     print("Balance:", account.balance)

# if __name__ == "__main__":
#     main()