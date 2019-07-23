"""
Bool Pgiaa Game
"""

import random


# Choose secret number
def get_secret_number():
    number = ""
    for i in range(0, 4):
        digit = str(random.randint(0, 9))
        while digit in number:
            digit = str(random.randint(0, 9))
        number += digit

    return number


# Check if the number contains unique digits
def is_unique_number(num):
    for i in range(0, 4):
        unique_list = [u for u in num if u != num[i]]
        if len(unique_list) != 3:
            return False

    return True


# Save to file
def save_to_file(line):
    with open(file_name, "a", encoding="UTF-8") as f:
        f.write(line+"\n")


# Check if the input is valid
def get_valid_input():
    valid = False
    while not valid:
        guess = input("Enter 4 unique digits: ")
        if len(guess) == 4 and guess.isdigit() and is_unique_number(guess):
            valid = True

    return guess


# Calc the bool pgiaa score
def calc_bool_pgiaa(num):
    result = ""
    for i in range(0, 4):
        digit = num[i]
        if num[i] in secret_number:
            index1 = num.find(digit)
            index2 = secret_number.find(digit)

            if index1 == index2:
                result += '*'
            else:
                result += '-'
        else:
            result += '0'

    return result


# The Game
file_name = "bool_pgiaa.txt"
win = False
secret_number = get_secret_number()
print(secret_number)

# read the game from file
with open(file_name, "r", encoding="UTF-8") as game:
    played_games = 0
    for line in game:
        print(line, end="")
        played_games += 1

    games_remaining = 20 - int(played_games / 3)


for i in range(0, games_remaining):
    guess = get_valid_input()
    save_to_file(guess)

    result = calc_bool_pgiaa(guess)

    bool_list = [b for b in result if b == '*']
    pgiaa_list = [p for p in result if p == '-']

    score = f"bool: {len(bool_list)},  pgiaa: {len(pgiaa_list)}\n"
    save_to_file(score)
    print(score)

    if len(bool_list) == 4:
        win = True
        break

if win:
    print("You are the Winner !!!")
else:
    print("You failed  :(")






