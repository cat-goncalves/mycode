rooms = {
            'Library' : {
                'north' : 'Study',
                'east'  : 'Basement',
                'south' : 'Billiard Room'
            },
            'Study' : {
                'east'  : 'Hall',
                'south' : 'Library'
            },
            'Hall' : {
                'east'  : 'Lounge',
                'south' : 'Ballroom',
                'west'  : 'Study',
                'east'  : 'Dining Room',
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

suspects = [
    {"yellow" : "Colonel Mustard"},
    {"red" : "Miss Scarlet"},
    {"purple" : "Mr. Plum"},
    {"green" : "Mr. Green"},
    {"white" : "Mrs. White"},
    {"blue" : "Mrs. Peacock"}
]