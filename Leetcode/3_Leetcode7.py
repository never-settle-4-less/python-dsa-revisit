# given a number return the reverse of it - 

def reverse(num: int) -> int:

   # MAX = 2147483647
   # MIN = -2147483648

    n = num
    result = 0
    while n > 0:

        last_digit = n % 10
        n = n //10

        #if(result > MAX // 10 or result == MAX//10 and last_digit >= MAX % 10):
          #  return 0
        
        #if(result < MIN // 10 or result == MIN//10 and last_digit <= MIN % 10):
          #  return 0

        #last_digit = n % 10
        result = (result * 10) + last_digit
        #n = n //10
    return result

# T(n) = O(LogN to base 10)
# S(n) = O(1)

print(reverse(2345)) # passed
print(reverse(890)) # passed
print(reverse(-5643)) # NOT passed