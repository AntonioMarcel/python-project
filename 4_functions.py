# Create a function, user_name(), that returns the name of a person: "Rolf"
def user_name():
    return "Rolf"


# Create another function, greeting(), that
def greeting(name):
    return f"Hello, {name}, how are you?"


# takes a name as an argument and returns a greeting phrase:
# "Hello, NAME, how are you?"
greetings_rolf = greeting(user_name())
print(greetings_rolf)
