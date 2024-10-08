
def count_digits(num):
    n = num

    if(n == 0):
        return 1
    
    count = 0
    while n > 0:
        n = n//10
        count += 1
    return count


print(count_digits(279000181))