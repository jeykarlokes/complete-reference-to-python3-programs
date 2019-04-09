num = int(input("enter number ::"))
si_of_n = int(input("enter si of n"))
def find_modulus():
    for exponent in range(1,si_of_n):
        # exponent_result = 0
        exponent_result = (num**exponent)%si_of_n
        # print(exponent_result)
        if exponent_result == 1:
            print(exponent_result,exponent)
            break
print(find_modulus())