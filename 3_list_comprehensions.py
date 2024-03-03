my_list = [0, 1, 2, 3]
mult_list = [x * 2 for x in my_list]

friends = ["Claudin", "Clauclau", "Claudineia", "Marcelino", "PC"]
friends_c = [friend for friend in friends if friend.startswith("C")]

new_friends_c = ["Claudin", "Clauclau", "Claudineia"]

# same content but different lists (different memory allocation)
print(friends_c == new_friends_c)  # true (only checks content)
print(friends_c is new_friends_c)  # false (checks memory allocation as well)
print(f"first list: {id(friends_c)}\nsecond list: {id(new_friends_c)} ")
