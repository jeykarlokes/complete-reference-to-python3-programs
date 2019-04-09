# num = int(input("enter the number :"))
# num_str = str(num)

# cube_of_num = num **3
# print(cube_of_num)
# cube_str = str(cube_of_num)
# length = len(num_str)
# # print(length)
# if cube_str[-length:] == num_str:
#     print("trimorphic")
# else:
#     print("it is not trimorphic")

#microsoft problem
#array of penaliies p
# an array of car number c 
# d for date 
# find total fine to be collected on the given date 
# fine is collected for odd nummbered cars on even dates and vice versa

# t is no of testcase 
# each t contains three lines of input
# 1st line is two integers n and d 
# 2nd line n sppaces with c is the car no 
# 3rd line n sppaces with p is the penalities

no_of_spaces = []
penalities = []
car_no =  []
t = int(input("entr the number of testcase :"))
oddcarsfine = []
evencarsfine= []


for i in range(0,t):
    print("first line ")
    no_of_spaces = int(input("enter spaces :"))
    dates = int(input("enter the dates :"))
    car_numbers1 = input("enter the car no with n spaces :").split()
    car_no.extend(car_numbers1)
    penalities1 = input("enter the penaities with n spaces ;").split()
    penalities.extend(penalities1)
for i in range(1):
    car_no.append(int(car_no[i]))
    penalities.append(int(penalities[i]))
print(car_no)

print(penalities)

for pos in range(len(car_no)):
    if dates%2==0 and int(car_no[pos])%2!=0:
        oddcarsfine.append(int(penalities[pos]))
    elif dates%2!=0 and int(car_no[pos])%2==0:
        evencarsfine.append(int(penalities[pos]))


print(type(oddcarsfine[0]))
# print(type(evencarsfine[0]))



total_fine_odd_car = 0
for items in oddcarsfine:
    total_fine_odd_car+=int(items)
print(total_fine_odd_car)
















#if date is even  calculate odd no cars and their fines


# for pos in range(3):
#     if dates%2==0:
#         if int(car_no[pos])%2!=0: # IF CAR IS ODD
#             oddcarsfine.append(penalities[pos])
#         else:
#             evencarsfine.append(penalities[pos])
# for pos in range(3):
#     if dates%2!=0:
#         if int(car_no[pos])%2==0: # IF CAR IS ODD
#             evencarsfine.append(penalities[pos])
#         else:
#             oddcarsfine.append(penalities[pos])
# print(oddcarsfine)
# print(evencarsfine)
# total_fine_even_car = 0
# total_fine_odd_car = 0

# for items in oddcarsfine:
#     total_fine_odd_car+=int(items)
# print(total_fine_even_car)
# for items in evencarsfine:
#     total_fine_even_car+=int(items)
# print(total_fine_even_car)














