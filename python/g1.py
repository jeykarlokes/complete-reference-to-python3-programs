
# #----------------------------------------#
# Question 1
# Level 1

# Question:
# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.
7,14,21,
# Hints: 
# Consider use range(#begin, #end) method

print("the numbers divisible by 7")
for i in range(2,50):
    if(i%7==0) and (i%5!=0):
     
     print(i)



