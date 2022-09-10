import time
import random
from WORDS import list_of_words

name = input("Tell me your name? ")#Get the user's name
name = name.upper()

print("Hello, " + name, "Welcome to the WORD BENDER!")
time.sleep(1)



def Word_Bender():
    words = random.choice(list_of_words)  # Sellecting random word for the player to guess letters
    words = words.lower()
    RLetter = random.choice(words)  # selecting random letter to show
    print("******************************************")
    print("" + name,"be ready to play the game!!!")
    print("Start guessing... Go..! ")
    print("You have 10 tries")
    time.sleep(0.5)
    guessedletters = RLetter + " _" * (len(words) - 1)
    tries = 10

    # Create a while loop to repeat the code
    while tries > 0:
        F = 0  # count how many times user will fail
        for letter in words:
            # print the correct guesses
            if letter in guessedletters:
                print(letter, end=" ")

            else:
                print("_", end=" ")
                F += 1
        print()
        if F == 0:  # When there isn't any failuer user will win
            print("Congratulations.!!! " + name, "You won the game!")
            print()
            time.sleep(1.0)
            break
        print()

        guessedletter = input("Guess a letter:")  # Giving chance to guess a letter
        guessedletter = guessedletter.lower()
        if guessedletter == "":  # Check if user input a letter or not
            print("Please input a letter!")
            print("You have", +tries, "tries left")
        else:
            guessedletter = guessedletter[0]  # Consider only the fist letter, if user input multiple letters at one try

            if guessedletter in guessedletters:  # Check whether user input a letter that he/she entered in previous tries
                print("You have entered this letter before. Please enter a new letter!")
                print("You have", +tries, "tries left")
                print()

            else:
                guessedletters += guessedletter
                if guessedletter in words:  # Check whether the guess is correct
                    tries == tries  # If it is a correct guess number of tries will remain same
                    print("Correct Guess")
                    print("You have", +tries, "tries left")
                    print()

                else:  # check whether the guess is wrong
                    tries -= 1  # If it is a wrong guess number of tries will deduct by 1
                    print("Wrong Guess")
                    print("You have", + tries, 'tries left')
                    print()

                    if tries == 0:  # When the number of tries = 0 player will loss the game
                        print("Oops," + name, "You Lost!")
                        print("The word was:" + words)
                        time.sleep(1.0)
Word_Bender()
