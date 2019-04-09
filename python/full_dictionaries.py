names = {"father":"jai","mother":"jayanthi","son":"lokesh","daughter":"akshaya"}
age = dict(f="50",m = "42",s = "22",d ="18")
print(age)
print(names)
print(age["f"])
num  = "son"
print(names[num])

for key in names.values():
    print(key)
for key in names.keys():
    print(key)
for key,values in names.items():
    print(key,values)

if names["father"]:
    print("father key is present")
else:
    print("no father key is present")

print("jai" in names.values())
print("daughter" in names.keys())

# fromkeys
newuser = dict.fromkeys(["name","phone","email","address","age"],"unknown")
print(newuser)

newuser = newuser.fromkeys(range(1,10),"mm")
print(newuser)

#get
names = {"father":"jai","mother":"jayanthi","son":"lokesh","daughter":"akshaya"}
print(names["son"])
print(names.get("son"))
# print(names["son1"]) # it will throw the error 
print(names.get("son1")) # but it will return none valule 

# #pop
print(names.pop("father"))
print(names)

#popitem
print(names.popitem())
print(names)

#update
names = {"father":"jai","mother":"jayanthi","son":"lokesh","daughter":"akshaya"}
second = {"city ": "chennai  "}
third = {}
third["city "] = "ambur"
names.update(second)
print(names)
names.update(third)
print(names)

# data modelling 
playlist = {
    "tiltle ": "travel",
    "author": "lokesh_jeykar",
    "songs":[
        {"songname ":"nenjae","artists":"arr rahman","music":"arr","duration":6.0},
        {"songname ":"inkem inkem ","artists":"sid ","music":"gopi sundar","duration":4.0},
        {"songname ":"high on love ","artists":"sid sriram","music":"u1","duration":6.0}
        ]}
total = 0
for song in playlist["songs"]:
    total += song["duration"]
print(total)
    

#dictionary comprehension
names = {"father":"jai","mother":"jayanthi","son":"lokesh","daughter":"AKshaya"}
update_names = {k.upper() : v.lower()  for k,v in names.items()}
print(update_names)
new_names = { k:(k.upper() if k is "son" else k)  for k,v in names.items()}
print(new_names)
num = dict(one = 1,two = 2,three = 3)
num = {k + " hello" :v**2 for k,v in num.items()}
print(num)
number = {k:("even" if k%2==0 else "odd" ) for k in range(1,100)}
print(number)
new_names = {(k.upper() if k is "son" else k ):(v.lower() if v is "AKshaya" else v) for k,v in names.items()}
print(new_names)


