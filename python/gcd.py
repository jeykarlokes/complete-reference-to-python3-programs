#gcd of two numbeers


# find factors of a and b
# simple logics of the gcd is common factors 
# max(a,b)+1 is upperlimit and the modulus is the 

a=int(input("enter the number a  :"))
b=int(input("enter the number b  :"))
factors_a_and_b = []

def divisors(lista,listb):
    for a_values in range(1,max(lista,listb)+1):
        if lista%a_values==0 and listb%a_values==0:
            factors_a_and_b.append(a_values)
(divisors(a,b))
print(f"the gcd of a and b is :{max(factors_a_and_b)}")



