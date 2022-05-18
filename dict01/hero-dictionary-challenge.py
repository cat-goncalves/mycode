#!/usr/bin/env python3

from pprint import pprint

ScarletWitch={'Real Name':'Wanda Maximoff','First Appearance':'The X-Men (Vol. 1) #4 (March, 1964)','Team Affiliations':['Avengers Unity Squad','Brotherhood of Evil Mutants','Avengers','Lady Liberators','West Coast Avengers','Defenders','Secret Defenders','Force Works'],'Aliases':['Wanda Frank','Ana Maximoff','Wanda Magnus'],'Base of Operations':'New York City','Powers':['Probability manipulation','reality alteration','Chaos Magic (later revealed not to exist, according to Doctor Strange)'],'Skills and Abilities':'Knowledge of Magic'}

pprint(ScarletWitch)

# adding a new value into the dictionary
ScarletWitch['Creators'] = ['Stan Lee', 'Jack Kirby']

print( ScarletWitch.keys() )

# Ask for input form te uder to type in one of those keys displayed in that list. Save it as the variable choice
choice = input("Input a key to display the dictionary values: ")

# Use the variable choice to accress your dictionaried and return the appropriate value
if ScarletWitch.get(choice) == None:
    print("Sorry, invalid key")
else:
    print(f"Scarlet Witch's {choice} is/are: {ScarletWitch[choice]}")
