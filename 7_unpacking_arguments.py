# * unpacks multiple arguments into one tuple
def multiply(*args):
    print(args)
    total = 1
    for arg in args:
        total = total * arg
    return total


print(multiply(1, 3, 5))

# * unpacks list into numerous parameters
nums = [3, 5]
# print(*nums)


def add(x, y):
    return x + y


# print(add(*nums))

# ** can be use to unpack dict if key names are the same as the function arguments
# only works inside the function call
nums = {"x": 3, "y": 5}
# print(**nums) # error
# print(add(**nums))


# practice time
def apply(*args, operator):
    if operator == "*":
        # print(args)
        # return multiply(args)  # args: tuple (1, 3, 6, 7)
        return multiply(*args)  # *args unpacks args tuple to pass it to the function

    if operator == "+":
        return sum(args)
    else:
        return "No valid operator provided"


# print(apply(1, 3, 6, 7, operator="+"))

# repeat the end o the video for the other possibility
