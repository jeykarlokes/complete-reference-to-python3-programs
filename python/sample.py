# # list comprehension
# bikes = ["honda","tvs"]
# print([bike[0].upper() for bike in bikes])

# year = int(input("year :"))
# if year%4==0:
#     if year%100==0:
#         if year%400:
#             print(True) 
#         else:
#             print(False)
#     else:
#         print(True)
#         # break
# else:
#     print(False)
#     # break


# map
num  = [1,2,3,4,5,6]
double = list(map(lambda x : x/2,num))
# print(list(do?uble))
print(double)

scse = [{"student":"lokesh","rollno":"15mis1051"},
{"student":"kumar","rollno":"15mis1101"}]
print(scse)
hello = {"student":"lokesh","rollno":"15mis1051"}
mm = {"student":"kumar","rollno":"15mis1101"}
name = ["lokesh","kumar","love","like"]
name_with_l = list(filter(lambda x : x[0]=="l",name))
print(name_with_l)

length= list(filter(lambda x : len(x)<5,name))
prints = list(map(lambda x : f"hello {x}",length))
print(prints)

sentence = [{"sent1":"hello he is a good boy","sent2":"he is very quiet "},
{"sent1":"he is very lonely","sent2":"he is calmm"},
{"sent1":"heisa badboy","sent2":"he is worst"}]

filered = list(filter(lambda x : len(x["sent1"]) < 14,sentence))
print(filered)
for x in filered:
       if x == "sent1":
           print(x.upper())