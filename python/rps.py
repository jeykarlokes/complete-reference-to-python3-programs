print("....................................")
print("!!!hello,, welcome to rock paper scisoors game !!!!")
print("let's start the game ")
for i in range(1,10):
    player1 = input("PLAYER 1 : please enter the input : ")
    print("no cheating \n" * 138)
    player2 = input("PLAYER 2 : please enter the input :")
    if player1 and player2 :
        if player1 == "rock" and player2 == "paper":
         print("player2 wins!!")
        elif  player1=="rock" and player2 == "scissors":
         print("player1 wins!!")
        elif player1 == player2:
         print("the match is tie ")
        elif player1 == "paper" and player2 =="rock":
         print("player1 wins!")
        elif player1 == "paper" and player2 == "scissors":
         print("player2 wins!")
        elif player1 == "scissors" and player2 == "rock":
         print("player2 wins!")
        elif player1 =="scissors" and player2 == "paper":
         print("player1 wins!")
        else:
         print("player1 or player2 entered a wrong  input")
    else:
     print("please type something")
    