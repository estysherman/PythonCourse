"""
Print * in piramida
"""
num = int(input("Select number: "))
space = num - 1

for i in range(1, (num * 2), 2):
    for s in range(space):
        print(" ", end="")
    space -= 1

    j = 0
    while j < i:
        print("*", end="")
        j += 1

    print()


