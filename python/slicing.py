num = [11,22,33,44,55,66,77,88]
print(num[1::])
print(num[1::2])#22,44,66,88
print(num[1::3])#22,55,88
print(num[1:5:])#22,33,44,55
print(num[1::-1])#22,11
print(num[3:-5:])#22,11,88,77,66,55
print(num[:4][::-1])

names = ["lokesh","kumar","jeykar"]
names[1],names[0] = names[0],names[1]
print(names)
