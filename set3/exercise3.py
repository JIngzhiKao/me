"""Set 3, Exercise 3.

Steps on the way to making your own guessing game.
"""

import random


def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    merge it with code from excercise 1.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """

    
    # the tests are looking for the exact string "You got it!". Don't modify that!
    print('welcome to the guessing game')
    print(' a number between _ and _?')
    
    
    while True:
      try:
        lowerbound = int(input("Enter a lower bound:"))
        upperbound = int(input("Enter an upper bound:"))
      except ValueError as e:
        print("Hey mate, a pure digital number is better for me to understand ")

        continue
      if lowerbound > upperbound:
        print("Hey mate, {low} is bigger than {high}".format(low = lowerbound,high = upperbound))
      else:
        print("OK then, a number between{low} and {high} ?".format(low=lowerbound,high=upperbound))

      lowerbound = int(lowerbound)
      upperbound = int(upperbound)
      actural_number = random.randint(lowerbound, upperbound)
      while True:
        try:
          guess = int(input("Let's try it: "))
        except ValueError as e:
          print("Hey mate, please give me a pure digital number:")
          continue
        if guess < int(lowerbound):
          print (" Hey mat, too small:")
        if guess > int(upperbound):
          print("Hey mate, you got too wild:")
        if guess > actural_number:
          print("too big,try again: ")
        elif guess < actural_number:
          print("too small,try again:")
        else:
          break
        return "you got it"

    
    


       if __name__ == "__main__":
        print(advancedGuessingGame())
