#!/usr/bin/env python3

tries = 0
guess = ""
while tries < 4:
    tries += 1
    guess = input("Finish the movie title, 'Monty Python's The Life of ...'")

    if guess.lower() == "shrubbery": 
        print("You gave the super secret answer!")
        break
    else:
        if guess.lower() == "brian":
            print("Correct!")
        elif guess.lower() != "brian" and tries == 3:
            print("Sorry, the answer was Brian.")
            break
        else:
            print("Sorry, try again!")


# "Correct!", "Sorry, try again!", and "Sorry, the answer was Brian."