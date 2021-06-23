"""
Using random to randomamly assign scores to questions as well as
random give questions
"""
import random
"""
importing sqlite 3 in order to keep scores in a database
"""
import sqlite3
#class for game
class quiz:
  def __init__ (self, bank, questions, list_of_questions)
def quiz(bank):
  question_1 = input

#Title welocme to the game
print("Welcome to the car quiz!!!\n ")
#asking if they want to play
playing = input("Do you want to play? ").lower()
#
if playing == "yes" or playing == "y" or playing == "yea" or playing == "yeah":
  print("The goal of the game is to get over 500 points. \nQuestions are worth between 10 and 75 points. \nThier values are randomly assigned\n \nLETS GO")
  bank = 0
  while bank <= 500:
    quiz(bank)
    #bank = int(input("BANK: "))

else:
  quit()