"""
Get the winner - x o game
"""
import re

regex = [
    r"(x|o)\1\1.{3}.{3}",
    r".{3}(x|o)\1\1.{3}",
    r".{3}.{3}(x|o)\1\1",
    r"(x|o).{2}\1.{2}\1.{2}",
    r".{2}(x|o).{2}\1.{2}\1",
    r".(x|o).{2}\1.{2}\1.",
    r"(x|o).{3}\1.{3}\1",
    r".{2}(x|o).\1.\1.{2}",
]


def getTheWinner(game):
    for reg in regex:
        res = re.search(reg, game)
        if res is not None:
            res = res.group(1)
            break

    if res is not None:
        print("The winner is " + res)
    else:
        print("There is no winner :( ")


print("Enter 1 to exit")
while True:
    gameBoard = input("Enter your board game: ")
    if gameBoard == '1':
        break
    getTheWinner(gameBoard)

