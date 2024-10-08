print(int(123.78))

#print(int(10 + 5j)) #not possible 

print(int(True))
print(int(False))

# print(int("sai")) #notpossible
# print(int("sai10")) # not posssible

print(int("212")) # possible 

# 1) We can convert from any type to int except complex type.

#2) If we want to convert str type to int type, compulsary str should contain only integral
#value and should be specified in base 10 integer format only.

# print(int("10.5")) # not possible

print(int("45"))

print(float(10))
# print(float(10 + 5j)) #not possible
print(float(True))
print(float(False))

# print(float("ten")) #not possible
print(float("10"))
print(float("10.5"))

# comlex() examples - 

print(complex("10"))
print(complex(10))
print(complex(True))
print(complex(False))
print(complex(True + False)) # 1 + 0j
print(complex(False + True)) # 1 + 0j
print(complex(False + False)) #0j
print(complex(True + True)) # 2 + 0j

# Form-2: complex(x,y)

# We can use this method to convert x and y into complex number such that x will be real
# part and y will be imaginary part.
print(complex(10, -2)) # 10-2j
print(complex(True, False)) # 1+0j
print(complex(False, True)) # 1j

print(bool()) # empty string false
print(bool('')) # empty string -- False
print(bool("")) # empty string -- False
print(bool(' ')) # -- True (non empty string)
print(bool(" ")) # -- True (non empty string)
print(bool('true')) # -- True
print(bool('False')) # -- True (non empty string)
print("===========================")
print(bool(1009090))
print(bool(1))
print("===========================")

# str()

print(str(10))
print(str(10.0))
print(str(10+5j))
print(str(True))
print(str(0b10111110))


