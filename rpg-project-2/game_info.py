rooms = {
            'Library' : {
                'north' : 'Study',
                'east'  : 'Basement',
                'south' : 'Billiard Room'
            },
            'Study' : {
                'east'  : 'Hall',
                'south' : 'Library',
                'item'  : 'candlestick'
            },
            'Hall' : {
                'east'  : 'Lounge',
                'south' : 'Ballroom',
                'west'  : 'Study',
                'item'  : 'key'
                },
            'Lounge' : {
                'north' : 'RANDOM',
                'south' : 'Dining Room',
                'west'  : 'Hall'
            },
            'Dining Room' : {
                'north' : 'Lounge',
                'south' : 'Kitchen',
                'west'  : 'Billiard Room',
                'item'  : 'potion',
               },
            'Kitchen' : {
                'north' : 'Dining Room',
                'west'  : 'Ballroom',
                'item'  : 'monster',
                },
            'Ballroom' : {
                'north' : 'Hall',
                'east'  : 'Kitchen',
                'west'  : 'Conservatory'
            },
            'Conservatory' : {
                'north' : 'Billiard Room',
                'east'  : 'Conservatory',
                'south' : 'RANDOM'
               },
            'Billiard Room' : {
                'north' : 'Library',
                'east'  : 'Dining Room',
                'south' : 'Conservatory'
            },
            'Pantry' : {
                'south' : 'Dining Room',
                'item' : 'cookie',
            }
         }

rooms_list = ["Library", "Study", "Hall", "Lounge", "Dining Room", "Kitchen", "Ballroom", "Convservatory", "Billiard Room", "Pantry", "Basement"]

item_options = ["Rope", "Lead Pipe", "Knife", "Candlestick", "Revolver", "Key", "Key", "Key", "Key", "Key", "Key"]
weapons_list = ["Rope", "Lead Pipe", "Knife", "Candlestick", "Revolver"]
suspects = [
    {"yellow" : "Colonel Mustard"},
    {"red" : "Miss Scarlet"},
    {"purple" : "Mr. Plum"},
    {"green" : "Mr. Green"},
    {"white" : "Mrs. White"},
    {"blue" : "Mrs. Peacock"}
]

def showInstructions():
  #print a main menu and the commands
  print('''
Clue Game
========

You have been invited to dinner at a fancy/scary mansion. You were hoping caviar would be on the menu but, instead, find yourself in the middle of a murder mystery! During the cocktail hour, you hear a blood curdling scream frorm a distance. A guest has been murdered! Put your skills to the test and find the killer!

Directions:
1. Every turn you can decide to either :
  go [direction] - to move into another room
      - You may go north, south, east or west throughout the house

  get [item] - to pick up the item in that room
      - The Item in a room could be either a weapon or a key

2. Collecting Items:
Items are very important. Collect items es evidence of the crime. Collect keys to use when accusing a suspect or freeing yourself from the basement

3. Traveling Around the House:
Beware the trap doors! Landing on a trap door means you will be transported to a new room at random.
Stay out of the basement. If you land in the basement you will need a key to exit. If you do not have a key, you lose!

3. Accusing a Suspect
At the end of each turn you may accuse someone by guessing the suspect, weapon and location of the murder. But, be careful! You may only guess from weapons you have already collected. Every accusation uses a key, lose all your keys and the game is over.

4. Updates
  type 'D' at any time to see the directions
  type 'update' to see a list of your items, keys and previous guesses

Now, be safe and catch the murderer!
''')
