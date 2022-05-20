#!/usr/bin/env python3

questions = [
    "Step 1 - Pick a cleanser:\n\n 1: Cerave Hydrating Facial Cleanser\n 2: Krave Beauty Matcha and Green Tea Cleanser\n 3: Tata Harper Softening Cleanser",
    "Step 2 - Pick a toner/essence:\n\n 1: Glycolic Acid 7% Exfoliating Toning Solution \n 2: isntree Green Tea Toner\n 3: SK-II Facial Treatment Essence",
    "Step 3 - Pick a serum:\n\n 1: Inkey List Niacinimide Serum \n 2: Beauty of Joseon Glow Serum\n 3: Skinceuticals Vitamin C E Ferulic Serum ",
    "Step 4 - Pick a moisturizer:\n\n 1: Cerave Moisturizing Cream \n 2: Purito Water Cream\n 3: La Mer Creme de La Mer",
    "Would you even trust a skincare quiz that skipped the most important step?!?\n\n Step 5 - Pick an SPF:\n\n 1: La Roche Posay Anthelios Sunscreen SPF 60\n 2: Beauty of Joseon Relief Sun SPF 50\n 3: Supegoop Unseen Sunscreen SPF 40"
    ]

results = {
    1: "creativity",
    2: "curiosity",
    3: "ambition"
}
choices = []


def avgChoices():
    sum = 0
    for elem in choices:
        sum += elem
    return round(sum / 5)

def main():
    step = 0

    print("Pick a skincare routine and we'll tell you your best personality trait\n\n ...enter 'Q' at any time to quit")

# TODO: validate user inputs so they are either a number 1-3 or q/Q

    while step < 5:
        print(questions[step])
        currentChoice = input().upper()
        if currentChoice == "Q":
            print("...goodbye!")
            break

        choices.insert(step, float(currentChoice))

        print(choices)
        step += 1

    if step == 5:
        print( {results[avgChoices()]} )

main()

# creativity, curiousity, determination/ambition
