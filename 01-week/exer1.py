"""
Get number form the user
and return if it even number or odd number
"""

num = int(input("Select number: "))
if num % 2 == 0:
    print(f"{num} is Even number")
else:
    print(f"{num} is Odd number")
