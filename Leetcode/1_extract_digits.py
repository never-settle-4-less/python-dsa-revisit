# Given a number extract each digit of the number without converting it into string

def extract_digits(num: int) -> None:
    n = num
    while n > 0:
        last_digit = n % 10
        print(last_digit)
        n = n // 10
              

extract_digits(97373)

# T(n) = O(Logn to base 2)
# S(n) = O(1)