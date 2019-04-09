# ------------------------------------#
# Question 5
# Level 1

# Question:
# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

# Hints:
# Use __init__ method to construct some parameters

class Goat():
    def __init__(self,str1):
        self.str1 = str1
    def getString(self,lok):
        self.str1 = input("enter the string:")
        self.lok = lok
    def printString(self):
        print(self.str1)
        print(self.lok)
g = Goat("lokesh")
g.getString("rakesh")
g.printString()
