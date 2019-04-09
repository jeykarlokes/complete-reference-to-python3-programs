fruits = ["apple","bannana","orange","grapes"]
new_fruits = [fruit.upper() + " is good for health " for fruit in fruits]
name =  "lokesh"
print([x.upper() for x  in name])

nums = [1,2,3,4,5,6,12,44,76,33,1121]
nums1 = [num *2 + 10  for num in nums ]
print(nums1)
print(new_fruits)
bool_values = ["",[],0]
new_bool = [bool(bool_value)  for bool_value in bool_values]
print(new_bool)

#conditional logics
#if
if_num = [num for num in nums if num%2 == 0]
print(if_num)
#else 
else_num = [num*2 if num%2==0 else num/2  for num in nums]
print(else_num)

#join
hello = "hOw aRe you ?"
hello = hello.lower()
# hello_join = "".join(hello)
# print(hello_join)

hello_join1 = [char for char in hello if char not in "aeiou"]
hello_join1 = "".join(hello_join1)
print(hello_join1)

#list _join
fruits = "".join(fruits)
print(fruits)


# learned list comprehesnion

nums = str([1,2,3,4,5,6,7,8])
print(" ,".join(nums))
double_num = [num/2 for num in nums]
print(double_num)

# list comprehesnion with if 
if_num = [num if num%2==0 else num*2 for num in nums]
print(if_num)

words = "lokesh is bad boy"
new_words = "..".join([char for char in words if char not in "aeiou"])
print(new_words)
some = [1,2,3]
nestedlist = ",".join([[val*2 if val%2!=0 else val for val in range(1,4)] 
for num in range(3)])
print(nestedlist)



s = [num,input() if num <=9 for num in range(3
)]
# for _ in range(3):
#     s.append(list(map(int, input().rstrip().split())))
# result = formingMagicSquare(s)

