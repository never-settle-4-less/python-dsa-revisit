def marks(sci, math, eng, hindi=0, comp=0):
    
    print(sci, math, eng, hindi, comp)
    total = sci + math + eng + hindi + comp
    percentage = total/5
    print(f"total marks are {total}")
    print(f"your percentage is {percentage}")


# keyword args are used to mess up with the order and pass in the same order as u want

marks(math=99, hindi=87, comp=34, sci= 89, eng= 88)

# some args order is maintained and some not, look below - 

marks(89, 45, comp= 77, eng= 44, hindi = 28)

print()