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
  def __init__ (self, bank, correct_answers, wrong_answers, questions, list_of_questions):
    bank = self.bank
    correct_answers = self.correct_answers
    wrong_answers = self.wrong_answers
    questions = self.questions
    list_of_questions = self.list_of_questions
  def bank_value():
    bank = 0 
    return bank
  def quiz(bank, correct_answers, wrong_answers):
    def question_1():
      question_1 = input("Which animal features in the logo for Lamborghini?").lower()
      if question_1 == "bull" or question_1 == "a bull":
        correct_answers += 1
        bank += random.randint(10, 75)
        response = "CORRECT.\n You now have " + str(bank) + " in your bank"
      else:
        wrong_answers += 1
        response = "CORRECT.\n You now have " + str(bank) + " in your bank"
      return bank and correct_answers and wrong_answers
    def question_1():
      question_1 = input("Which animal features in the logo for Lamborghini?").lower()
      if question_1 == "bull" or question_1 == "a bull":
        correct_answers += 1
        bank += random.randint(10, 75)
        response = "CORRECT.\n You now have " + str(bank) + " in your bank"
      else:
        wrong_answers += 1
        response = "CORRECT.\n You now have " + str(bank) + " in your bank"
      return bank and correct_answers and wrong_answers
  def questions_randomizer(questions):

    pass


"""
#Title welocme to the game
print("Welcome to the car quiz!!!\n ")
#asking if they want to play
playing = input("Do you want to play? ").lower()
#
if playing == "yes" or playing == "y" or playing == "yea" or playing == "yeah":
  print("The goal of the game is to get over 500 points. \nQuestions are worth between 10 and 75 points. \nThier values are randomly assigned\n \nLETS GO")
  bank = 0
  while bank <= 500:
    #quiz(bank)
    bank = int(input("BANK: "))

else:
  quit()
"""