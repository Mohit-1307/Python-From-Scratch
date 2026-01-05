# def main():

#     n = int(input("What's n? "))

#     for i in range(n):
#         print("👌" * i)

# if __name__ == "__main__":
#     main()

# -------------------------------------------------------------------------------->

# def main():

#     n = int(input("What's n? "))

#     for i in range(n):
#         print(emoji(i+1))

# def emoji(n):
#     return "👌" * n

# if __name__ == "__main__":
#     main()

# -------------------------------------------------------------------------------->

# def main():

#     n = int(input("What's n? "))

#     for e in emoji(n):
#         print(e)

# def emoji(n):

#     flock = []

#     for i in range(n):
#         flock.append("👌" * (i + 1))

#     return flock

# if __name__ == "__main__":
#     main()

# -------------------------------------------------------------------------------->

# def main():

#     n = int(input("What's n? "))

#     for e in emoji(n):
#         print(e)

# def emoji(n):

#     for i in range(n):
#         yield "👌" * i

# if __name__ == "__main__":
#     main()