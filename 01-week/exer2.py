"""
Get 3 numbers
and check if one of them is sum of the 2 others
"""
def sum_of_2(num1, num2):
    """
    This function return sum of 2 numbers
    :param num1:
    :param num2:
    :return: sum of num1 and num2
    """
    return num1 + num2

a = int(input("Select number 1: "))
b = int(input("Select number 2: "))
c = int(input("Select number 3: "))

if a == sum_of_2(b, c):
    print(f"{a} is sum of {b} and {c}")
elif b == sum_of_2(a, c):
    print(f"{b} is sum of {a} and {c}")
elif c == sum_of_2(a, b):
    print(f"{c} is sum of {a} and {b}")
else:
    print("no match numbers....")

