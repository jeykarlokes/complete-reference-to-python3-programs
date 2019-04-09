 # a [2,4,7] replace 7 with 6 
# a = [2,4,7]
# def fun(a,i,n):
#  if i > 0 and i < 3:
#     # print("succeded")
#     a[i] = n
#     return(True)
#  else:
#     # print("failed")
#     return(False)
# result = fun(a,2,8)
# print(result)
# result1 = fun(a,3,4)
# print(result1)


#calculate gcd (4,6) 4 = 1,2,4 : 6 = 1,2,3: cf  = 1,2 : gcd = 2::
# d =[1,2,3] 12 = 1,2,3,4,6,12 : 24 = 2,1,3,4,6,12,24: cf = 1,2,3,4,6,12 gcd = 12
# print(max(d))


# (a,b) = int(input("enter no1 :")), int(input("enter no1 :"))
# cf = []
# def gcd(a,b):
#     for i in range(1,max(a,b)+1):
#         if a%i== 0 and b%i == 0: 
#          cf =[i]
#     print(max(cf))
# gcd(a,b)

char = []
char = input("enter stirng")
char= char[1::-1]
print(char)



