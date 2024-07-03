def info():
    pass

print("start")
info()
print("end")


def add():
    # local vars exist only within function
    num1 = 100
    num2 = 399
    total = num1 + num2
    print(total)
    #greet()

def greet():
    # name is the local variable here
    name = 'akhilesh'
    print(f"Hello {name}")
    add()

# =================

#add()
print("================================")
greet()
#info()