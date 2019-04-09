import random
print("rock paper scissors upgraded versionn 2.O")
print("............rock.....paper..........scissors...........")
print("............rock.....paper..........scissors...........")
print("............rock.....paper..........scissors...........")
random = random.randint(0,2)
winning_score = 2
user_wins = 0
computer_wins = 0
while user_wins < winning_score and computer_wins < winning_score:
  print(f"computer wins = {computer_wins} and user wins = {user_wins}" )
  user_inputs = input("enter the input :").lower()
  if user_inputs :
      if random == 0:
       computer_inputs = "rock"
       print("the  comuputer input was :",computer_inputs)
       if computer_inputs == "rock" and user_inputs == "paper":
          print("user wins!!")
          user_wins +=1
       elif  computer_inputs=="rock" and user_inputs == "scissors":
          print("computer wins!!")
          computer_wins +=1
       else:
          print("the match is tie ") 
      elif random == 1 :
        computer_inputs = "paper"
        print("the  comuputer input was :",computer_inputs)
        if computer_inputs == "paper" and user_inputs =="rock":
          print("computer wins!")
          computer_wins +=1
        elif computer_inputs == "paper" and user_inputs == "scissors":
          print("user  wins!")
          user_wins +=1
        else :
          print("the match is tie ") 
      else:
        computer_inputs = "scissors"
        print("the  comuputer input was :",computer_inputs)
        if computer_inputs == "scissors" and user_inputs == "rock":
          print("user wins!")
          user_wins +=1
        elif computer_inputs =="scissors" and user_inputs == "paper":
          print("computer wins!")
          computer_wins +=1
        else:
          print("the match is tie ") 
  elif user_inputs == "":
      print("user has not entered the input")
  else:
      print("user inputs out of bounds:")
print("computer wins:",computer_wins)
print("user wins:",user_wins)
