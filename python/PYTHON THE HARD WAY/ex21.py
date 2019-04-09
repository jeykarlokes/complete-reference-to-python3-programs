def add(a,b):
    print(f"adding {a} + {b}")
    return a + b

def subtract(a,b):
    print(f"subtracting {a} - {b}")
    return a - b

def Multiply(a,b):
    print(f"Multiply {a} * {b}")
    return a * b

def divide(a,b):
    print(f"dividing {a} / {b}")
    return a / b
print("Lets do some math functions ")
age =  add(21,23)
height  = subtract(74,2)
weight  = Multiply(2,5)
iq = divide(100,2)
print(f"Age : {age},height = {height} weight = {weight} , iq = {iq}")
print("here is a puzzle ")
what = add(age,subtract(height,Multiply(weight,divide(iq,2))))
print("That becomes: ",what,"can you do it by hand")
