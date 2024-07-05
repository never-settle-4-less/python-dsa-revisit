def average(n1:int, n2:int, n3:int, n4:int) -> float:
    avg = (n1 + n2 + n3 + n4)/4
    return avg

x = average(10, 20, 34, 57)
print(x)

def add(num1: int, num2: int) -> float:
    sum = num1 + num2
    return sum

y = add(78.6, 42993.9)
print(y)

def sum(num1: int, num2: int) -> None:
    sum = num1 + num2
    print(sum)

sum(9, 1)

def concat(first_name: str, last_name: str) -> str:
    return first_name + last_name

ans = concat("abc", "123")
print(ans)

# print is an inbuilt function which returns None

