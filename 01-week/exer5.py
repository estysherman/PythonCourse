import operator

def read_until_number(prompt):
    original = prompt
    while True:
        try:
            return int(input(prompt))
        except Exception:
            prompt = "Incorrect number. please " + original
            pass


def read_until_operation(prompt):
    original = prompt
    while True:
        operator = input(prompt)
        if operator in "+-*/^":
            return operator
        else:
            prompt = "Incorrect operator. please " + original


num1 = read_until_number("Select first number: ")
num2 = read_until_number("Select second number: ")
operation = read_until_operation("Select operation: ")

ops = {"+": operator.add,
       "-": operator.sub,
       "*": operator.mul,
       "/": operator.itruediv,
       "^": operator.pow}

print(f"{num1}{operation}{num2} = {ops[operation](num1, num2)}")
