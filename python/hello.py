# print("hello the program is started")
# hi = 9.0
# mm = "hello"
# jk = 2
# print("type the phy mark")
# phy = int(input())
# print("type the maths  maark")
# mat = int(input())
# print("the total will be displayedd soon")
# total = (phy + mat)
# print("the total  is  equal to;",total)
# if total > 150 and total > 160:
#  print("you are passed in this in ths exam")
# elif total == 150:
#   print("ypur r on the average")
# else:
#  print("you are failed int his xam")
# j =9
# while j < 20:
#   print("ddd")
#   if (j == 12) :
# #    print("sep")
# #    break
# #   j += 1
# # class Hello:
# #  x = 12
# #  y = 33
# #  def calc():
# #    print("ddddddddd")
# # h1 = Hello()
# # h1.calc
# # class Hello:
# #   fg = 9
# #   def __init__(hell,bitch,moc,ll):
# #     hell.name = bitch
# #     hell.roll = moc
# #     hell.mm = ll
  
# #   def fum(bb):
# #     print("helolo"+bb.name)

# # he  = Hello("lokesh",2,"ss")
# # he.name = "michal"
# # del he.name
# # print(he.name)
# # he.fum()
# # print(he.roll)
# # print(he.fg)

# x= 11
# def calc():
#     if x==1:
#   
#       print("true") num = 0 
from operator import add
dates =12
oddfine= []
evenfine =[]
car_no = [11,12,23]
penalities = [111,22,133]
for pos in range(3):
    if dates%2==0 and car_no[pos]%2!=0:
        oddfine.append(penalities[pos])
    elif dates%2!=0 and car_no[pos]%2==0:
        evenfine.append(penalities[pos])
    else:
        print(",,,")    
sum1 =0 
for i in oddfine:
    sum1 +=i
print(sum1)


print(evenfine)

