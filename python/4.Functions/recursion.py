"""def greet():
    print("greetings")
    greet()
    print("Done")


greet()"""

# recursion depth exceeded error will come 

# program to find out recursion milit error in python 
"""count = 1
def func():
    global count
    print(count)
    count += 1
    func()

func()"""

count = 1
def func1():
    global count
    if count == 7:
        return
    
    print(count)
    count += 1
    func1()

func1()

# outp put will be 1,2,3,4,5,6