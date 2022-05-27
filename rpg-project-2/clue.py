#!/usr/bin/python3

import random
from game_info import rooms
from game_info import rooms_list
from game_info import item_options
from game_info import suspects
from game_info import weapons_list
from game_info import showInstructions
from pprint import pprint


def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
  #print the current inventory if there is one
  if len(inventory) > 0:
    print('Inventory : ' + str(inventory))
  else:
    print("Iventory is empty, you need to collect evidence!")
  print('You have  : ' + str(keys) + ' key(s).')

  # show previous guesses if there are any
  if len(guesses) > 0:
    print("Your previous guesses")
    pprint(guesses)

  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
  print("---------------------------")

  #tell the user their play options 
  print("You can 'go': ")
  for direction in rooms[currentRoom]:
    if direction != "item":
      print (direction)
  if rooms[currentRoom].get('item'): 
    print("\nor 'get " + rooms[currentRoom].get('item') + "'")
  if keys > 0 and len(inventory) > 0:
    print("\n... or 'accuse' to make a guess")

#an inventory, which is initially empty
inventory = []
guesses = []
keys = 0

#a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms

#start the player in the Hall
currentRoom = 'Hall'

def main():
  global answer
  global guesses
  global inventory
  global currentRoom
  global keys
  global rooms_list
  global item_options

  rooms_temp= rooms_list.copy()
  random.shuffle(rooms_temp)
  item_temp= item_options.copy()
  random.shuffle(item_temp)
  for x in rooms_temp:
      for y in item_temp:
          rooms[x]["item"] = y



  suspect_index = randint(0, len(suspects))
  weapon_index = randint(0, len(weapons_list))
  room_index = randint(0, len(rooms_list))

  answer = {
    "suspect" : suspects[suspect_index].values(),
    "room"    : rooms_list[room_index],
    "weapon"  : weapons_list[weapon_index]
  }

  play = input("Clue:\nType '?' to see directions and,'Q' to quit and 'p' to play:\n")

  if play == "?" :
    showInstructions()
  elif play.lower() == "q":
    exit()
  else:
    print("Let's Play!")

  #loop forever
  while True:

    showStatus()

    #get the player's next 'move'
    #.split() breaks it up into an list array
    #eg typing 'go east' would give the list:
    #['go','east']
    move = ''
    while move == '':
      move = input('>')

    # split allows an items to have a space on them
    # get golden key is returned ["get", "golden key"]
    if move == "?" :
      showInstructions()
    elif move.lower() == "q":
      exit()
    else:
        move = move.lower().split(" ", 1)

    #if they type 'go' first
    if move[0] == 'go':
      #check that they are allowed wherever they want to go
      if move[1] in rooms[currentRoom]:
        #set the current room to the new room
        currentRoom = rooms[currentRoom][move[1]]
      #there is no door (link) to the new room
      else:
          print('You can\'t go that way!')

    #if they type 'get' first
    if move[0] == 'get' :
      #if the room contains an item, and the item is the one they want to get
      if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
        if rooms[currentRoom]['item'].lower() == "key":
          keys += 1
          del rooms[currentRoom]['item']
          print("\nYou got a key!\n\n")
        else:
          #add the item to their inventory
          inventory += [move[1]]
          #display a helpful message
          print(move[1] + ' got!\n\n')
          #delete the item from the room
          del rooms[currentRoom]['item']
      #otherwise, if the item isn't there to get
      else:
        #tell them they can't get it
        print('Can\'t get ' + move[1] + '!\n\n')
    
      # logic to accuse/guess the game
      if move[0] == 'accuse':
        pprint(suspects)
        guess_suspect = input(f"Input color to  from suspects above to guess\n")
        guess_weapon = input(f"Input a collected weapon to guess\n{inventory}\n")
        guess_room = input(f"input room to guess\n{str(rooms_list)}\n")

        ## Define how a player can win
        if suspects[guess_suspect].lower() == {answer["suspect"].lower() } and guess_weapon.lower()  == {answer["weapon"].lower() } and guess_room.lower()  == {answer["room"].lower() }:
          print(f"CONGRATULATIONS! You found the murderer!\n\nIt was {guess_suspect} with the {guess_weapon} in the {guess_room}")
          break

        ## If a player enters a room with a monster
        elif rooms[currentRoom] == "Basement" and keys == 0:
          print('The Murderer has locked you in the basement. You are out of keys. \nGAME OVER')
          break

        elif keys == 0:
          print('Incorrect guess. Unfortunately, you are out of keys and the murderer is on to you. \nGAME OVER')
          break
        else:
          guesses += {
            "suspect": guess_suspect,
            "weapon": guess_weapon,
            "room": guess_room
          }
          print("Incorrect guess. Maybe next time")



if __name__ == "__main__":
    main()
