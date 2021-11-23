from random import randint

#get both users to guess a number
playerOneGuess = int(input("I'm thinking of a number between 1 and 100, enter a guess player 1: "))

playerTwoGuess = int(input("Now player 2 guess: "))

#randomly generate a number between 1 and 100
answer = randint(1, 100)

#get the distance each user was from the answer
playerOneDistance = answer - playerOneGuess
playerTwoDistance = answer - playerTwoGuess

#make both values positive since it doesn't matter if too high or too low, only who is closer
if playerOneDistance < 0:
  playerOneDistance = playerOneDistance * (-1)

if playerTwoDistance < 0:
  playerTwoDistance = playerTwoDistance * (-1)

if playerOneDistance < playerTwoDistance:
  print("Player 1 was closer, the answer was " + str(answer))
elif playerTwoDistance < playerOneDistance:
  print("Player 2 was closer, the answer was " + str(answer))
else:
  print("It's a draw, the answer was " + str(answer))