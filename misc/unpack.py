# def total(galleons, sickles, knuts):
#     return (galleons * 17 + sickles) * 29 + knuts

# coins = [100, 50, 25]

# Calculate the total number of knuts by passing the list to the total function as unpacking the list.
# print(total(*coins), "knuts")

# ---------------------------------------------------------------------------------------------------------------------------------------->

# def total(galleons, sickles, knuts):
#     return (galleons * 17 + sickles) * 29 + knuts

# coins = {"galleons": 100, "sickles": 50, "knuts": 25}

# Calculate the total number of knuts by passing the list to the total function as unpacking the list.
# print(total(**coins), "knuts")

# ---------------------------------------------------------------------------------------------------------------------------------------->

# def f(*args, **kwargs):
    
#     print("Positional arguments:", args)

# f(100, 50, 25, 5)


# def f(*args, **kwargs):
    
#     print("Named:", kwargs)

# f(galleons = 100, sickles = 50, knuts = 25)