a = 10
print(type(a))

b = 0b1111 #binary num
print(type(b))
print(b)

c = 0B10101 #binary num
print(type(c))
print(c)


h = 0b111
print(h)
print(type(h))

print(c + h)

octal1 = 0o2373
print(octal1)
print(type(octal1))

octal2 = 0O342432
print(octal2)
print(type(octal2))

print(octal1 + octal2)

#hexadecimal -- 

hex1 = 0x38927face
print(hex1)
hex2 = 0Xabce12
print(hex2)

hex3 = print(hex1 + hex2)


num1 = 10
num2 = 0B10
num3 = 0o10
num4 = 0X10

print(num1, num2, num3, num4)

print(num1 + num2 + num3 + num4)

##base conversions from decimal to other formats 

print(bin(18))
print(bin(0o11))
print(bin(0X10))
print("============================")

print(oct(10))
print(oct(0B1111))
print(oct(0X123))
print("============================")

print(hex(100))
print(hex(0B111111))
print(hex(0o12345))
print("===================================")

#int data type meant for integer values 

#float data type 
f = 1.234
print(type(f))

#We can also represent floating point values by using exponential form
#(Scientific Notation)
print("===========================")
x = 1.2e3
print(x)

#We can represent int values in decimal, binary, octal and hexa decimal forms. But we
#can represent float values only by using decimal form.


# next complex data type -- 

#  In the real part if we use int value then we can specify that either by decimal, octal,
#binary or hexa decimal form.

# But imaginary part should be specified only by using decimal form.

a = 0B11 + 5j
print(a)
print("======================")

# we can perform operations on complex data type - 

a = 10 + 8j
b = 20 + 2.5j

print(type(a))
print(type(b))
print(a + b)

# Note: Complex data type has some inbuilt attributes to retrieve the real part and
#imaginary part

c = 10.5+3.6j

print(c.real)
print("=============")
print(c.imag)
print("=============")

#bool data type 

#  Internally Python represents True as 1 and False as 0

a = True
print(type(a))

b = False
print(type(b))
print('============================')
print(a + b)

c = True
print( a + a + c)

# string data type 

# A String is a sequence of characters enclosed within single quotes or double
#quotes.

s1 = "sai"
s2 = "abhi"

print(s1[0])
print("=====================")
print(s1[1])
print("=================")
print(s1[2])

#print(s1[20])
print("=================")
print(s1[:40])
print(s1[1:])
print(s1[:])

print(len(s1))
print(len(s2))
print("=================")
print(s1 * 4)

print(type(s1))
print(type(s2))

print("=================")

s = 'akhilesh'
print(s[0].upper() + s[1:])

print(s[:-1] + s[-1].upper())
print("=================")
print(s[0:len(s) - 1] + s[-1].upper())
print("=================")
print(s[0].upper() + s[1: len(s) - 1] + s[-1].upper())

print(s + '10')

# int * str - allowed
# str * int - allowed
# str * str - error 
# str + int - error 
# int + str - error 
# str + str - allowed

print(2 * 'ab' * 3)
print('5' * 5)
