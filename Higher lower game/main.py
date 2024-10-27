import art
from game_data import data
import random
from replit import clear


#get random accounts from game data

def get_random_account():
  '''Get random account from data '''
  return random.choice(data)

# show the output it in readable format

def format_data(account):
  '''Formats the random account in readable format'''
  name = account["name"]
  description = account["description"]
  country = account["country"]
  return f"Name: {name} , Description: {description} Country: {country}"

# check who has more followers
def check_followers(guess, a_followers, b_followers):
  '''Checks who has more followers and returns true or false '''
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"
#Get two accounts and Display both accounts in console and get input from user
def game():
  print(art.logo)
  account_a = get_random_account()
  account_b = get_random_account()
  score = 0
  game_continue = True
  while game_continue:
    account_a = account_b
    account_b = get_random_account()
  
    while account_a == account_b:
      account_b = get_random_account()
    
    print(f"Compare A: {format_data(account_a)}.")
    print(art.vs)
    print(f"Against B: {format_data(account_b)}.")
    guess = input("Who has more followers? Type 'A' or 'B':") .lower()
    follower_count_a = account_a["follower_count"]
    follower_count_b = account_b["follower_count"]
    correct_guess = check_followers(guess, follower_count_a, follower_count_b )
    clear()
    print(art.logo)
  
  
    if correct_guess:
      score += 1
      print(f"You're right! Current score: {score}.")
    else:
      game_continue = False
      print(f"Sorry, that's wrong. Final score: {score}")


game()

# if user's guess is right, continue the game and keep the score count
#  else end the game displaying score





