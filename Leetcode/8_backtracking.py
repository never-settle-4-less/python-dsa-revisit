# print 1 to N numbers using back tracking 

def func(i, n):
    if(i < 1):
        return
    func(i - 1, n)
    print(i)

func(4,4)
print("===========================")


# print N to 1 using backtracking
def func1(i, n):
    if( i > n):
        return
    func1(i + 1, n)
    print(i)

func1(1, 4)