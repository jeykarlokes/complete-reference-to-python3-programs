print(0xFB) #- hexa
print(0b1010)#-binary
print(0o15)#-octal
x = 1.1
y = 2.2
z  = x+y
print(z) #output  = 3.300000000000000003
#to overcome this issue use decimal modules
from decimal import Decimal as D
print(D('1.1') + D('2.2')) # o/p = 3.3
print(D('1.0') * D('2.0')) #o/p = 2.00
# to convert decimal to fractions module fractions
import fractions
print(fractions.Fraction(1.5))#o/p = 3/2 
print(fractions.Fraction(2.5)) #o/p = 5/2
# we can expllicitly  convert into fractions
print(fractions.Fraction(2,9))#o/p = 2/9
from fractions import Fraction as V
print(V(2,8) + V(1,8)) #o/p = 3/8
#in python built in functions ar there 
# factorial is a built in function we can calcualte factorial of a number 
import math
print(math.factorial(4)) #o/p = 24

#Random module 
import random
print(random.randrange(1,10)) #prints random integer in range
print(random.randint(1,10)) #prints random integer in range
x = ["a,","x","aa","q"]
print(random.choice(x)) #prints random in the aray 
random.shuffle(x) # prints shuffled aarray 
print(x)
print(random.random()) #prints randomly

