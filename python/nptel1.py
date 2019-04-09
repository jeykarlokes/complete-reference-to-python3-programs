age = input("enter the age ")
if age and (age >= 18 and age <=21):
    print("you are ok ") 
elif age and age < 18 :
    print("you are not eligible")
else :
    print ("nooooooooo")
# else:
#     print("enter the  input please ")


# rock paper scissors
print(".....................")

print("welcome to rock paper scissors game ")
print(".....................")
print(".....................")

print(".....................")

choice1 = input("enter the choice of the player 1 ;"))
choice2 = input("enter the choice of the player 1 ;"))
ch1 ,ch2,ch3= "rock","paper","scissors"
#rock paper  paper wins
#paper scissors  scisro wins
#rock scissors rock wins 
if (choice1 == choice2):
    print("player2 give different input ")
elif choce1 == ch1 and choice2 == ch2 :
    print("player2 wins")
elif choce1 == ch2 and choice2 == ch1 :
     print("player1 wins")
elif choice1 == ch2 and choice2 == ch3:
    print("player2 wins")
elif choice1 == ch3 and choice2 == ch2:
    print("player1 wins")
elif choice1 == ch3 and choice2 == ch1:
    print("player2 wins")
elif choice1 == ch and choice2 == ch3:
    print("player2 wins")
elif choice1 == ch2 and choice2 == ch3:
    print("player2 wins")
