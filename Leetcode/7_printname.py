# Print 1 to N  using recursion istead of using FOR loop


def func(i, n):
    if(i > n):
        return
    print(i)
    #print("sai")
    func(i+1, n)

func(1, 4)

print("=================================")

# Print n to 1 in reverse order using recursion

def func1(i, n):
    if(i < 1):
        return
    print(i)
    func1(i - 1, n)

func1(3, 5)