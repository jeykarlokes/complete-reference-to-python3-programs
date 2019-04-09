#tuples is immutable (can't change )  faster than list
colleges = ("srm","vit","bits","iit")
print(colleges)
nums = tuple((1,2,1,2,34))

print(nums.count(1))
print(colleges.index("bits"))
college =  len(colleges) -1

while college > 0:
    print(colleges[college])
    college -= 1



#sets is unorderd and donot accept dupliicates
fruits = {"orange","mango","grapes"}
print(fruits)
fruits1 = {"orange","mango","grapes","grapes"}
print(fruits)
for fruit  in fruits:
    print(fruit)
vegetables = {"onion","tomato","mango","cabbage","brinjal"}
print(fruits | vegetables)
 # unions the  two sets but doesn't produce duplicates
print(fruits & vegetables) # and operation is done 

#set methods
fruits.add("banana") #add operation
print(fruits)
fruits.remove("orange")
print(fruits)

fruits.discard("cabbage")
print(fruits)

new_fruits = fruits.copy()
print(new_fruits)

#set comprehension
string = "sequioa"
print(len({(char)  for char in string if char in "aeiou"})==5 )

print({num+=1 for num in range(1,10)})