# #functions
# def printoddoreven(num):
#     for n in num:
#         if n%2!=0:
#             return True
#         return False
# print(printoddoreven([12]))

# # default paarameters
# # (A,B) IS THE paarameters
# # (11,12) IS THE ARGUMENT

# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def common(a,b,func = add):
#     return(func(a,b))

# print(common(11,12,sub))


# # KEYWORD argument --> we are explicity passing the arguments with = asignment
# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def common(a,b,func = add):
#     return(func(a,b))

# print(common(b=11,a=121,func=sub))

# # scope
# total =0
# def mm():
#     print(total)
#     total = 1 + 2
#     return total
# print(mm())
# # global
# total =0
# def mm():
#     global total
#     total +=1
#     return total
# print(mm())
# #nonlocal
# def mm():
#     """hello this is simple nonlocal variable it is used to access the variables which are local and within function of function itself-------"""
#     total =0
#     total +=1
#     print(total)
#     def mn():
#         nonlocal total
#         total +=2
#         print(total)
# print(mm())
# print(mm.__doc__)



# #args in function collects and returns as a tuple
# def sum(*args):
#     total =0
#     for num in args:
#         total+=num
#     return total
# print(sum(1,2,3,4,5))

# def identify_words(*words):
#     if "lokesh" in words and "jeykar" in words:
#         return "lokesh jeykar is present in the words"
#     return "no lokesh jeykar is present"

# print(identify_words("lokesh","hello","jeykar"))#present
# print(identify_words("lokesh","hello","jeykar "))#not present


# # kwargs collects and returns as a dictionary 

# def colours(**colors):
#     print(colors)
#     if "lokesh" in colors and colors["lokesh"] == "white":
#         return "lokesh likes white colour"
#     elif "lokesh" in colors:
#         print("lokesh is there but not white ")
#     return "nothing is there"

# print(colours(lokesh = "white",akshaya = "green"))
# print(colours(lokesh = "red"))
# print(colours(aks = "redd"))


# #parameter ordering  *args takes arguments until it reaches the keyword argument
# # 1. parameter
# # 2. *args 
# # 3. default parameter
# # 4. **kwargs

# def parameter_ordering(a,b,*args,ball = "pen",**kwargs):
#     return [a,b,args,ball,kwargs]


# print(parameter_ordering(1,2,33,44,55,566,"kumar" , first_name= "lokesh",last_name="jeykar"))

# #list and tuple unpacking
# #means that it takes that entire list  or tuple and pass it as argument (every number in the list or tuple is passed as each)
# def numbers(*nums):
#     print(nums)
#     intial =  0
#     for numb in nums:
#         intial += numb
#     return intial
# number  = [1,2,3,4,5,6,7,8,9,11]
# number1  = (1,2,3,4,5,6,7,8,9,11)

# print(numbers(*number1))

# print(numbers(*number))

# #dictionary unpacking 
# print("dictionary unpacking!!")
# def addition(a,b,c,**kwargs):
#     print(kwargs)
#     print(a,b,c)
#     return a+b+c
# add_num = dict(a=1,b=2,c=33, aa = 11 ,dog = "barks") 
# print(addition(**add_num))


# #lambdas  similar to a function it is a online expression 

# def add(a,v):return a + v
# print(add(1,22))

# # the above in lambdas
# addition = lambda a,b : a+b-2*12
# print(addition(11,14))


# #map which accepts two args one is function and other is iterable thing (list,string,dict,tuple )
# num = [1,2,3,4,5]
# double = map(lambda x:x*2,num)
# print(list(double))
# # print(double)

# names  = [dict(one ="harish ",two ="vikash",three="motta",four= "maddu")]
# caps_names = list(map(lambda name : name["one"] ,names))
# print(str(caps_names))

#filter it is similar to map it checks the condition  within the lamda
chats = [{"username":"lokesh","status":["i'm okk"]},
{"username":"vel","status":[]},
{"username":"yeshwant","status":["ya good"]},
{"username":"kumar","status":[]},
]


print("extract not active users using filters")
filter_chats = list(filter(lambda c  : c["status"]==[],chats))
print((filter_chats))

s = list(map(filter(lambda x : if x <=9 ,for x in range(3)))

# #map and filter 
# chats = [{"username":"lokesh","status":["i'm okk"]},
# {"username":"vel","status":[]},
# {"username":"yeshwant","status":["ya good"]},
# {"username":"kumar","status":[]},
# ]
# print("extract non active users and upper it with map and filter")
# filter_chats = list(filter(lambda c  : c["status"]==[],chats))

maps = list(map(lambda user:user["username"].upper(),filter_chats))
print(maps)

# print("more simpleer ways,,,,,,,,,,,")
# filter_maps = list(map(lambda user:user["username"].upper(),filter(lambda u :u["status"]==[],chats)))

# print(filter_maps)

# #same example  extracting inactive users using list comprehension  
# print("extracting inactive users using list comprehension")

# inactive_users = [user["username"].upper() + " is inactive " for user in chats if not user["status"]]
# print(inactive_users)
# print("##########")


# new_names = ["tvs_star_city","bajaj_pulsar","honda_shine"]
# new_names1 = (list(map(lambda name :name.upper(),filter(lambda x : len(x)<15 ,new_names))))
# print(new_names1)


# #all checks all the args are truthy or false
# nums = [1,2,4,6,8,10]
# alls  = all([print(num) for num in nums if num%2==0])
# print(alls)
# names = ["Tvs","Tata","Techmahindra","Twoys"]

# print(all([name[0]=="T" for name in names ]))
# print("all in dict ")
# family = dict(father ="jai",mother = "jayanthi",son="lokesh",daughter = "akshaya")
# print(all({fam["father"] + "is there" for fam in family if fam["father"]=="j"}))
# # #any if any of the values is truthy it returns true 
# # print("any")
# # nums = [1,2,3,4,11]
# # print(any([num for num in nums if num%3==2]))










