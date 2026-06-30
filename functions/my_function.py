import random

def fun_game(die_sides):
  """ This is a game to roll the user determined die 5 times """
  die_rolls = [random.randint(1,die_sides)for die in range(5)]
  return die_rolls
def number_game():
  """This function gets a random number between 1 and 10 and the user tries to guess"""
  secret_number = random.randint(1,10)
  guess = int(input('Guess a number between 1 and 10'))
  if guess == secret_number: 
    return f'You Won the number was {secret_number}' 
  else:
    return f'Loser - lol'
