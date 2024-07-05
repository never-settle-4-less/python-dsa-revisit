def product(n1, n2):
    ans = n1 * n2
    return ans

def even_odd(num):
    if num % 2 == 0:
        print('even')
    else:
        print('odd')

x = product(7, 8)
print(x)
even_odd(x)

## return is most useful for reusing chunks of code