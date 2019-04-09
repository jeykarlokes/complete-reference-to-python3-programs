# # numArray = list(map(int,input().split(",")))
# # print(numArray)
# # sum=0
# # def addition(*num):
# #     for nums in num :
# #         global sum
# #         sum = sum + nums
# #     return sum
# # print(addition(*numArray))

# # Complete the compareTriplets function below
# #obj 3,21,11
# #  4,12,33
# # ans(1,2)

# # ass = 0
# # bss = 0
# # result = []
# # def func(a,b):
# #     global ass 
# #     global bss
# #     for i in range(0,3):
# #         if a[i] > b[i]:
# #             ass +=1
# #         elif a[i] < b[i]:
# #             bss+=1
# #         else:
# #             ass = ass
# #             bss =bss
        
# # a = list(map(int,input().split(",")))
# # b = list(map(int,input().split(",")))
# # func(a,b)
# # result.append(ass)
# # result.append(bss)

# # print(result)


# #3rd problem
# # n = int(input("length"))
# # num = list(map(int,input()))


# # sum =0
# # for i in num:
# #     i = i*i
# #     sum+=i
# # print(sum)


# # #PROBLEM
# # input string : abc
# # output:
# # abc
# # acb
# # bac 
# # bca
# # cba
# # cab 

# def is_repeated(word):
#     unique = []
#     for char in word:
#         if char not in unique:
#             unique.append(char)
#         else:
#             return True
#     return False

# unique = []
# result  =[]
# input_string = (input())
# for val in range(6):
#     for j in range(3):
#         for z in range(3):
#             # result.append(input_string[val] + input_string[j] + input_string[z])
#             result_word = input_string[val] + input_string[j] + input_string[z]
#             if(is_repeated(result_word) == False):
#                 result.append(result_word)
#             # .append(string[val] + string[j] +string[z])
#     print(result)
# # def is_repeated():
# #     for var in result:
# #         for char in var:
# #             if char not in unique:
# #                 unique.append(var)
# #             else:
# #                 print("print already exists")
# #     return unique   
 




# L as int input

# N= summation of 1 to L
# q = largest prime no b/w 1 and  N
# formula = (q*r)%N == 1


# i should get L as input 
# N should be summation 1- L

# aim it find r


#find N
L = int(input("enter the L as input :"))
N  = 0
for val in range(1,L+1):
    N += val
print(N)

#find q ?
#  prime concept is if it is divide by 1 and by it itself
# find prime numbers from 1 to N store in list
# sort it and find the last index of that
# which is the largest prime no

#harish
# prime_no = []
# for numerator in range(1,N+1):
#     counter = 0
#     for denominator in range(1,numerator+1):
#         if numerator % denominator == 0:
#             counter += 1
#     if counter == 2:
#         prime_no.append(numerator)


less_limit = N//2 
prime_no = []
for val in range(less_limit,N+1):# 1
    count =0
    for each in range(1,val+1):
        if val % each ==0:
            count +=1
    if count==2:
        prime_no.append(each)

print(prime_no)            

prime_no.sort()
q  = prime_no[-1]
print(f"largest prime number is {q}")

# formula = (q*r)%N == 1

for r in range(1,N):
    if ((q*r)%N==1):
        print(r)




