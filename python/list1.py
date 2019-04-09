

# python has a set of built-in methods that you can use on lists.
# Method
# Description
# append()-Adds an element at the end of the list
# clear()-Removes all the elements from the list
# copy()-Returns a copy of the list
# count()-Returns the number of elements with the specified value
# extend()-Add the elements of a list (or any iterable), to the end of the current list
# index()-Returns the index of the first element with the specified value
# insert()
# Adds an element at the specified position
# pop()-Removes the element at the specified position
# remove()
# Removes the item with the specified value
# reverse()
# Reverses the order of the list
# sort()
# Sorts the list



bikes = ["yamaha","rx100","r15"]
print(bikes)
bikes1 = [1,2,3,4]
print(bikes1)
bikes1.remove(1)
print(bikes1)
bikes1.extend("1")#extend will take one args and print it ass a each  char basedd list
print(bikes1)
numbers = ["lokesh","bowl","bowl","apple","xeroz"]# sort can numbers and strings also 
numbers.sort()
print(numbers)
# numbers.reverse()

numbers.insert(0,"bowl")
print(numbers)
