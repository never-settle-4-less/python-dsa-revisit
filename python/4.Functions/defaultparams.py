
# accept a default value that you  mention in the params list if nothing is assigned.
# but still the order of the params has to be maintained 


def marks(sci =0, math =0, eng =0, hindi =0, comp =0):
    
    print(sci, math, eng, hindi, comp)
    total = sci + math + eng + hindi + comp
    percentage = total/5
    print(f"total marks are {total}")
    print(f"your percentage is {percentage}")

marks(24, 45, 67, 21, 77655)

marks(39,58, 69) # hindi and comp default value 0 will  be taken 

marks(50, 38)

#required params 

def marks(sci, math , eng =0, hindi =0, comp =0):
    print(sci, math, eng, hindi, comp)
    total = sci + math + eng + hindi + comp
    percentage = total/5
    print(f"total marks are {total}")
    print(f"your percentage is {percentage}")
    

# all required params always on LHS, default params always on RHS, no mixing allowed

