"""
Print * in rows
"""
num = int(input("Select number: "))

for i in range(1, num + 1):
    j = 0
    while j < i:
        print("*", end="")
        j += 1
    print()
