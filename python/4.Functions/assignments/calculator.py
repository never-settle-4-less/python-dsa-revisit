def simple_calculator(n1: int, n2: int, operation: str):
    if(operation == "+"):
        print(n1 + n2)
    elif(operation == '-'):
        print(n1 - n2)

n1 = int(input())
n2 = int(input())
operation = str(input())

simple_calculator(n1, n2, operation)