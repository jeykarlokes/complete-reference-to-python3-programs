def cheese_and_crackers(cheese_count,boxes_of_crackers):
    print(f"you have {cheese_count} cheese !")
    print(f"you have {boxes_of_crackers} boxes_of_crackers!")
    print("Ma that's enought for a party!")
    print("Gte a blanket \n")
print("We can ust give the function numbers direstly")
cheese_and_crackers(20,30)
print("OR, we can use variables from our scripts ")
amount_of_cheese = 10
amount_of_crackers = 30
cheese_and_crackers(amount_of_cheese,amount_of_crackers)
print("We can even do math inside too ")
cheese_and_crackers(10+20,5+6)
print("And we combine the two variables and math")
cheese_and_crackers(amount_of_cheese +100,amount_of_crackers + 1000)
