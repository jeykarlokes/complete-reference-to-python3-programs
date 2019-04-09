# a = 6A09E667F3BCC908
# e = 510E527FADE682D1 
# b = BB67AE8584CAA73B 
# f = 9B05688C2B3E6C1F 
# c = 3C6EF372FE94F82B 
# g = 1F83D9ABFB41BD6B 
# d = A54FF53A5F1D36F1 
# h = 5BE0CD19137E2179

print(0x3C6EF372FE94F82C)

# a =2,
# b= 3,
# c= 5,
# d =7,
# e = 11,
# f =13,
# g = 7,
# h =19
import math
import fractions
a = 2
# a = int(input("enter the number :"))
# sqrt_A= math.sqrt(a)
# print(f"we are printing the sqrt of {a}       ==>  ",end = "")
# print(sqrt_A)
sqrt_A = 1.7320508075688772935
fr  = fractions.Fraction(sqrt_A)
print(f"printing the fractions of {a}           ===> ",end="")
print(fr)
fr = str(fr).split("/")
fractions_num = []
fractions_num.append(fr[0])
fractions_dem = []
fractions_dem.append(fr[1])
f_num = fractions_num[0]
f_dem = fractions_dem[0]
def normal():
    print("Normal ")
    print("normal hex val :")
    fractions_num = hex(int(f_num))
    fractions_dem = hex(int(f_dem))
    print(f"printing the hexadecimal values of numerator :{fractions_num},demoniator : {fractions_dem}")
normal()
# big_endian()










# def big_endian():
#     f_nu  = f_num[::-1]
#     f_de = f_dem[::-1]
#     # fractions_dem_r = fractions_dem[::-1]
#     print(f"big endian formats :numerator:{fractions_num}={f_num} , denominator :{fractions_dem} = {f_dem}")
#     fractions_num = hex(int(f_nu))
#     fractions_dem = hex(int(f_de))
#     print(f"printing the big endian hexadecimal values of numerator :{fractions_num},demoniator : {fractions_dem}")
