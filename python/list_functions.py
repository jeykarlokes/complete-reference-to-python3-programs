# 1) append
ar = [1,4,2,3,4]
cr = [1,2,3,4]
strin = ["s","q","a","o"]
br =  [33,22,11,33,44,55,33,24]
ar.append(5)
print(ar)
print(".......1")
ar1 = [5,6]
ar.append(ar1)
print(ar)
print("......2.")


#2) extend
cr.extend(ar1)
print(cr)
print(".......3")

#3) sort
br.sort()

print(br)
print(".......4")

#4) join
new_ar = ','.join(strin)
print(new_ar)
print(".......5")

#5) reverse
br.reverse()
print(br)
print(".......6")

#6) remove
br.remove(33)
print(br)
print(".......7")

#7) count
coun  = ar.count(4)
print(coun)
print(".......8")

#8) pop
ar.pop(2)
print(ar)
print("......9.")

#9) index
print(ar.index(4,1))
print("...index 10....")

#clear
ar.clear()
print(ar)
print("......11.")
