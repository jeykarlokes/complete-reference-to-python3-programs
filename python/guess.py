import random
guess = None
random_no = random.randint(1,10)
while True:
    guess = int(input("enter the  number from 1 to 10 :"))
    if guess > random_no:
        print("you'r too high !!")
    elif guess < random_no:
        print("yuu are to low !!")
    else:
        print("you won !!")
        playagain = input("do you want to play again : (y/n)")
        if playagain == "y":
            guess = int(input("enter the  number from 1 to 10 :"))
        else:
            print("thanks for playing:")
            break 
