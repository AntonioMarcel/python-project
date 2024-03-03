users = [
    (0, "Clauclau", "rei deles"),
    (1, "Marcelino", "goy sentador"),
    (2, "Marek", "baleia azul"),
]

users_mapping = {user[1]: user for user in users}

print(users_mapping["Marek"])

# same but more complicated
for user in users:
    if user[1] == "Marek":
        print(user)

# log in example
name_input = input("Enter your name: ")
password_input = input("Enter your password: ")

_, name, password = users_mapping[name_input]

if password_input == password:
    print("Welcome!")
else:
    print("You're not welcome!")
