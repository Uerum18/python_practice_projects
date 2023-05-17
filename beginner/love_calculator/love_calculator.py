def get_love_score(name1, name2):
    string_1 = 'true'
    string_2 = 'love'
    name_string = name1 + name2
    total, total_2 = 0, 0
    for l in string_1:
        total += name_string.count(l)
    for l in string_2:
        total_2 += name_string.count(l)
    score = int(str(total)+str(total_2))
    return score


print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
score = get_love_score(name1.lower(), name2.lower())
if 10 > score or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif 40 <= score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}, you don't really fit together.")
