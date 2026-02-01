#Magic8Ball.py
#Name: Nathan Heavican
#Date: 1/31/26
#Assignment: Lab 2
#Purpose: Create a program that asks the user to enter a question, selects a random response, and displays the response

#We will need random for this program, import to use this package.
import random

def main():
  #Create a list of your responses.
  print("Magic 8 Ball")
  answers = ["yes", "no", "maybe", "possibly", "definitly not", "ask again later", "certainly"]
  #Prompt the user for their question.
  question = input("Enter a yes or no question: ")
  #Answer question randomly with one of the options from your earlier list.
  response = random.choice(answers)
  print(response)
if __name__ == '__main__':
  main()
