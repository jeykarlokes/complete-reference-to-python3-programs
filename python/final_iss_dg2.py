#sqrt of a numbr 
#decimal part should be multiplied by 16 and the integer shoould be made as o 
# a = 6A09E667F3BC C908 ---2
# b = BB67AE8584CA A73B ---3
# c = 3C6EF372FE9   4F82B ---5
# d = A54FF53A5F1D3 6F1 ---7
# e = 510E527FADE68 2D1 ---11
#  
# f = 9B05688C2B3E 6C1F ---13
# g = 1F83D9ABFB41 BD6B ---17
# h = 5BE0CD19137E 2179---19

import math
decimal  = []
a = int(input())
b = math.sqrt(a)
def add_hexa(b):
        for i in range(16):
            b = str(b).split(".")
            print(b)
            z = str(b[1])    
            c = "0."+z
            b.pop(0)
            c = float(c)
            val1 = c * 16
            val1 = str(val1).split(".")
            decimal.append(val1[0])
            val1 = val1[1]
            b = "0."+str(val1)
            print(c)
            # print(hexad)
            if i == 15:
                print(decimal)

final_hexadecimal = []
hexadeimal = []
def convert_hexadecimal(decimal):
    items = [int(v) for v in decimal]
    items = [hex(v) for v in items]
    print(items,len(items))
    for i in range(15):
        # for j in range(3):
        xr = items[i]
        xr = xr[-1]
        xr = str(xr).upper()
        final_hexadecimal.append(xr)
    print("".join(final_hexadecimal))
add_hexa(b)
convert_hexadecimal(decimal)

