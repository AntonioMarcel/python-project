# number game app
# random_number = 7

# while True:
#     user_input = input("Press Y/n if you want to play: ").lower()

#     if user_input == "n":
#         break

#     number_input = int(input("Choose a number: "))
#     if number_input == random_number:
#         print("you're goddamn right")
#     elif abs(number_input - random_number) == 1:
#         print("you were off by one")
#     else:
#         print("you're wrong!")

# average grade
# use a for loop to modify the total variable and add to it each of the grades
grades = [35, 67, 98, 100, 100]
total = 0
amount = len(grades)  # length of grades list

for grade in grades:
    total += grade  # total = total + grade

average_grade = total / amount
print(average_grade)
