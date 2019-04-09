
import math
c,h =  50, 30 
result =[]
d = input("eenter")
d = d.split()

for x in d :
    print(x)
    result1 =  [print(int(round(math.sqrt(((100/30)*(x)))))) for num in d ]
    result.append(result1)
print(result)
    

# d = input("enter :")
# items = [print(int(x)) for x in d]
# print(items)
# for val in items:
#     print(items[val])
# values = [ print("".join(str(round(math.sqrt(((100/30)*int(val))))))) for val in items]
