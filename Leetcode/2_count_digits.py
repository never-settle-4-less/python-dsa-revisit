
def count_digits(num: int) -> int:
    n = num

    if(n == 0):
        return 1
    
    count = 0
    while n > 0:
        n = n//10
        count += 1
    return count


print(count_digits(279000181))

# T(n) = O(LogN base 10)
# S(n) = O(1)

# optimal solution - 

# return int(Log(given_number) to base10)

import math

def digit_count(num: int) -> int:
    return int(math.log10(num) + 1)

print(digit_count(1234))

# T(n) = O(1)
# S(n) = O(1)