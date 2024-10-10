
# 10 - [1, 2, 5, 10]
# 25 - [1, 5, 25]
# 7 - [1, 7]
# 19 - [1, 19]

def factors(num: int) -> list[int]:

    n = num
    result = []
    for i in range(1, n + 1):
        if (n % i) == 0:
            result.append(i)
    return result

print(factors(10))
print(factors(20))

# T(n) - O(n)
# S(n) - O(k) where is total number of factors 

# optimal solution -- 

def reduceTime_by_half(num: int) -> list:

    n = num
    result = []
    for i in range(1, n//2):
        if (n % i) == 0:
            result.append(i)
    result.append(n)
    return result

print(reduceTime_by_half(30))
print(reduceTime_by_half(70))



# more optimal solution, if n is the num , search till sq.root of num

from math import sqrt

def sqrootmethod(num: int):
    result = []
    n = num
    for i in range(1, int(sqrt(n))):
        if(n % i) == 0:
            result.append(i)
            if(n//i) != i:
                result.append(n//i)
    result.sort()
    return result

print(sqrootmethod(90))



