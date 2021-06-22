#Title welocme to the game
print("Welcome to the car quiz!!!\n ")
#asking if they want to play
playing = input("Do you want to play? ").lower()
#
if playing == "yes" or playing == "y" or playing == "yea" or playing == "yeah":
  print("The goal of the game is to get over 500 points. \nQuestions are worth between 10 and 75 points. \nThier values are randomly assigned\n \nLETS GO")
else:
  quit()