def reverse(num: int) -> int:
    n = num
    result = 0
    while n > 0:
        last_digit = n % 10
        result = (result * 10) + last_digit
        n = n//10
    return (num == result)

print(reverse(121))
print(reverse(327))
print(reverse(363))

# T(n) = O(LogN base 10)
# T(n) = O(1)
# the above is the optimal solution 