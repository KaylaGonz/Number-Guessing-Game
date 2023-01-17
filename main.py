#Number Guessing Game:
import random
from art import logo

def difficulty(mode):
  """Selects difficulty of game by deciding number of attempts"""
  if mode == "easy":
    return 10
  elif mode == "hard":
    return 5

def check_number(computer_number, user_number):
  """Checks if user's number is the right guess"""
  if user_number > computer_number:
    print("Too high.")
    print("Guess again.\n")
    return 
  elif user_number < computer_number:
    print("Too low.")
    print("Guess again.\n")
  elif user_number == computer_number:
    return print(f"You got it! The answer was {user_number}.")
 

def game():
  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I am thinking of a number between 1 and 100.")
  
  answer = random.randint(1,100)
  print(f"Psssst....The correct answer is: {answer}")
  game_mode = input("Choose a difficulty. Type 'easy' or 'hard': ")
  guess_amount = difficulty(game_mode)
  
  while guess_amount != 0:
    print(f"You have {guess_amount} attempts remaining to guess the number.")
    guess_amount -= 1
    user_guess = int(input("Make a guess: "))
    check_number(answer, user_guess)
    if answer == user_guess:
      return

  return print("You've run out of guesses, you lose.")

    
game()
