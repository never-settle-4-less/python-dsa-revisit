"""
make a function named marks, it should take 5 integeres as parameters and print the total and print the percentage
"""

def marks(sci:int, math:int, eng:int, hindi:int, comp:int):
    total = sci + math + eng + hindi + comp
    percentage = total/5
    print(f"total marks are {total}")
    print(f"your percentage is {percentage}")

marks(24, 45, 67, 21, 77655)

# parameterizing is better than taking input from user

