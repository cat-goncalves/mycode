#!/usr/bin/env python3

zodiacSigns = [
    "Monkey, you are sharp, smart, curious, and mischievious",
    "Rooster, you are hardworking, resourceful, courageous, and talented",
    "Dog, you are loyal, honest, cautious, and kind",
    "Pig, you are a symbol of wealth, honesty, and practicality",
    "Rat, you are artistic, sociable, industrious, charming, and intelligent",
    "Ox, you are strong, thorough, determined, loyal, and reliable",
    "Tiger, you are courageous, enthusiastic, confident, charismatic, and a leader",
    "Rabbit, you are vigilant, witty, quick-minded, and ingenious",
    "Dragon, you are talented, powerful, lucky, and successfull",
    "Snake, you are wise, like to work alone, and determined",
    "Horse, you are animated, active, and energetic",
    "Sheep, you are creative, resilient, gentle, mild-mannered, and shy"
]

def main():    
    usr_name = input("Please enter your name:\n>") 
              
    usr_name = usr_name.title()    
    usr_year = int(input("Please enter your birth year in YYYY format, e.g 2010:\n>"))
    
    index = usr_year % 12

    print(f"{usr_name} your zodiac is {zodiacSigns[index]}.")

if __name__ == "__main__":
    main()