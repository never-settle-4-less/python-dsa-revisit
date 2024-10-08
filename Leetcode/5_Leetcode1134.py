def check_armstrong(num: int) -> bool:
    n = num
    nod = len(str(n))
    result = 0

    while n:
        last_digit = n % 10
        result = result + (last_digit ** nod)
        n = n//10
    return(num == result)

x = 9474

if check_armstrong(x) == True: 
      print("Yes Armstrong number") 
else:
     print("NO, NOT an Armstrong number")

# T(n) = O(LogN to base 10)
# S(n) = O(1)
      

