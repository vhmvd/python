import random

# Genrates random integer number in the range 1-20
random_number = random.randint(1,20)

number_of_guesses = 10
guesses_made = 0
max_score = 100
number_guessed = False

# This loop runs until the number is not guessed
while(not number_guessed):
  guess = input("\nEnter guess: ")

  # Increments the guesses after input
  guesses_made = guesses_made + 1

  # Coverts the string input into integer
  guess = int(guess)

  # Checks if the number is correct
  if(guess == random_number):

    # Outputs the details
    print("\nCorrect guess!!")
    print("Score:", max_score)
    print("Number of guesses made:", guesses_made)

    # Sets number_guessed to True so the loop breaks
    number_guessed = True

  else:
    # Decrements the number of available guesses
    number_of_guesses = number_of_guesses - 1

    # Reduces the score by 5 after an incorrect guess
    max_score = max_score - 5
    print("\nIncorrect guess")

    # Loop tho check if the number is divisible in range 3-10
    # If the number is a prime number 11, 13, 17, 19 the loop will not output
    for itr in range(3,11):
      if (random_number%itr == 0):
        print("The number is divisible by", itr)
        break

    # Checks if the number is greater or smaller than 10
    if random_number > 10:
      print("Number is greater than 10")
    else:
      print("Number is smaller than 10")

    print("Number of guesses left", number_of_guesses)

    # If max number of guesses is reached, closes the loop
    if(guesses_made == 10):
      print("\nYou have no guesses left")
      print("The number was", random_number)
      break
