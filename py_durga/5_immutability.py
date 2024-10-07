# concept of immutability in python
# in python generally everything is treated as an object

# All Fundamental Data types are immutable. i.e once we creates an object,we cannot
# perform any changes in that object. If we are trying to change then with those changes
# a new object will be created. This non-chageable behaviour is called immutability.

a = 10
b = 10
print(a is b)

print(id(a))
print(id(b)) # both a and b will point to same reference 

x = 10
print(id(x))
print("==================")
x = x + 1
print(id(x))

p = 9
q = p
print("-------------------------")
print(id(p))
print(id(q))

print("**************************")
q = q + 1
print(id(p))
print(id(q))

print("&&&&&&&&&&&&&&&&&&&&&&&&&")

x = 10
print(id(x))
x = float(x)
print(id(x))

