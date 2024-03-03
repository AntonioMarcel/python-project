# # ** can be used to collect keyword arguments and to unpack them into a dictionary
# def named(**kwargs):
#     print(kwargs)


# named(name="Bob", age=25)


# # ** can also be used to unpack dictionary to multiple arguments in a function call
# def named(name, age):
#     print(name, age)


# details = {"name": "Bob", "age": 25}

# named(**details)


# # ** challenge 1
# def named(**kwargs):  # unpacks into dictionary
#     print(kwargs)


# details = {"name": "Bob", "age": 25}

# named(**details)  # unpacks into multiple arguments


# ** challenge 2
# def named(**kwargs):  # unpacks arguments into dict kwargs
#     print(kwargs)  # prints kwargs dict


# def print_nicely(**kwargs):  # unpacks arguments into dictionary kwargs
#     named(**kwargs)  # unpacks kwargs dict into multiple arguments
#     for arg, value in kwargs.items():
#         print(f"{arg}: {value}")


# print_nicely(name="Bob", age=25)

"""
* and ** are normally used to show that a function accepts an unlimited number of 
arguments
"""


# def both(*args, **kwargs):
#     print(args)  # tuple
#     print(kwargs)  # dict


# both(1, 3, 5, name="Bob", age=25)


# final example: ** can only be used with a mapping
def myfunction(**kwargs):
    print(kwargs)


details = {"name": "Bob", "age": 25}

myfunction(**details)  # success
myfunction(**"Bob")  # error
myfunction(**None)  # error
