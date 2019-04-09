# Question 2
# Level 1

# Question:
# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
# 3 = 3*2*1 
# a =int(input("enter the number :"))
# fact =1 
# if a > 0:
#     for i in range(1,a+1):
#         fact = fact * i
#     print(f"the factorial of {a} is ",fact)
# else:
#     print("can't process the value ")    

num = int(input("enter the number "))

def fact(n):
    if n == 1:
     return n
    else :
     return n + fact(n-1) 
    # 4 + fact(3) + fact(2) == 4 + 
if (num == 0):
    print(f"the factorial of {num} is : 1")
elif (num < 0):
    print("can't proced to -ve numbers")
else:
    print(f"the factorial of {num} is ",fact(num))