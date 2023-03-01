import random

def get_choices(): 
  player_choice = input("Input a choice (rock, paper, scissors): ")
  options = ["rock", "paper", "scissors"]
  computer_choice = random.choice(options)
  choices = {"player": player_choice, "computer" : computer_choice}
  
  return choices

def checkWin(player, computer):
  print(f"You chose: {player}, Computer chose: {computer}")
  if player == computer:
    return "TIE"
  elif player == "rock":
    if computer == "scissors":
      return "Rock beats scissors you win"
    else:
      return "Paper beats rock you lose"
  elif player == "paper":
    if computer == "scissors":
      return "Scissors beats paper you lose"
    else:
      return "Paper beats rock you win"
  elif player == "scissors":
    if computer == "rock":
      return "Rock beats scissors you lose"
    else:
      return "Scissors beats paper you win"

choices = get_choices()
result = checkWin(choices["player"], choices["computer"])
print (result)