# parameters and arguments

def sum(n1, n2, n3): #parameters
    total = n1 + n2 + n3
    print(f"sum is {total}")

# sum() would throw error since no arguments are sent 

sum(10, 20, 30)
sum(49, 78, 88) #arguments

sum("sum", "hello", "python") #this will work string concat since we did not define any data type for n1,n2,n3

# use annotations 

def add(n1:int, n2:int, n3:int): #parameters
    total = n1 + n2 + n3
    print(f"sum is {total}")

add("hello", "python","sai")

#annotations are just clean coding practice and for our understanding only, still they will get string concatenated 

