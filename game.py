#!/usr/bin/env python3

#Player Object
class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []

    def grabItems(self, item):
        self.inventory.append(item)

    def fight(self):
        self.health -= 50

    def winRiddle(self):
        answer = int(input("What's 2 +2?"))
        if answer == 4:
            self.health += 50
            print("Health increased by 50")
        else:
            print("wrong answer")

#Monster Object
class Monster:
    def __init__(self):
        self.health = 50


def showInstructions():
    # print a main menu and the commands
    print('''
RPG Game
========
Commands:
  go [direction]
  get [item]
  teleport [room]
''')


def showStatus():
    # print the player's current status
    print('---------------------------')
    print('Teleport code: 0->Hall 1->Kitchen 2->Dinning Room 3->Living Room 4->Garden 5->Pantry 6->Attic')
    print('You are in the ' + currentRoom)
    # print the current inventory
    print('Inventory : ', p.inventory)
    # print an item if there is one
    if "item" in rooms[currentRoom]:
        print('You see a ', rooms[currentRoom]['item'])
        print((rooms[currentRoom]['Description']))
    print("---------------------------")


rooms = {

    'Hall': {
        'south': 'Kitchen',
        'west': 'Dining Room',
        'east': 'Attic',
        'north': 'Living room',  # new room
        'item': {'key': 'Keys to all of the rooms', 'map': 'Map of the house'},
        'Description': 'Hall connects to Kitchen(south), Dining room(east), Living room(north), Kitchen(south), '
                       'Attic(east)',
    },

    'Kitchen': {
        'north': 'Hall',
        'item': {'monster': 'You\'ve been caught by the monster'},
        'Description': 'Kitchen connects to Hall(north)',
    },
    'Dining Room': {
        'east': 'Hall',
        'south': 'Garden',
        'item': {'potion': 'you\'re safe', 'Pizza': 'enjoy your pizza'},
        'north': 'Pantry',
        'Description': 'Dining room connects to Hall(west), Garden(south), Pantry(north)',
    },
    'Living Room': {
        'south': 'Hall',
        'item': {'couch': 'Please sit on this couch', 'tv': 'Watch your favorite movie', 'lamp': 'Turn on the lamp'},
        'Description': 'Living room connects to Hall(south)',
    },
    'Garden': {
        'north': 'Dining Room',
        'item': {'Baby dragon': 'You\'re in flames', 'chest box':'Solve riddles'},
        'Description': 'Garden connects to Dining room(north)',
    },
    'Pantry': {
        'south': 'Dining Room',
        'item': {'cookie': 'yum', 'soda': 'refreshing'},
        'Description': 'Pantry connects to dinning room(south)'
    },
    'Attic': {
        'Description': 'You\'e trapped'
    }
}

# Teleport codes
codes = list(rooms.keys())

currentRoom = 'Hall'

showInstructions()
name = input("please enter player name: ")
p = Player(name)

while True:

    showStatus()

    # get the player's next 'move'
    # .split() breaks it up into an list array
    # eg typing 'go east' would give the list:
    # ['go','east']
    move = ''
    while move == '':
        move = input('>')

    # split allows an items to have a space on them
    # get golden key is returned ["get", "golden key"]
    move = move.split(" ", 1)

    # if they type 'go' first
    if move[0] == 'go':
        # check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            # set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        # there is no door (link) to the new room
        else:
            print('You can\'t go that way!')

    # if they type 'get' first
    if move[0] == 'get':
        # if the room contains an item, and the item is the one they want to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            # add the item to their inventory
            p.grabItems(move[1])
            # display a helpful message
            print(move[1] + ' got!')
            # delete the item from the room
            del rooms[currentRoom]['item']
        # otherwise, if the item isn't there to get
        else:
            # tell them they can't get it
            print('Can\'t get ' + move[1] + '!')

    # teleport command
    if move[0] == 'teleport':
        # allows the player to move to any room
        if codes[int(move[1])] in rooms:
            # set the current room to the new room
            currentRoom = codes[int(move[1])]
            # there is no door (link) to the new room
        else:
            print('You can\'t go that way!')

    # Define how a player can win
    if currentRoom == 'Garden' and 'key' in p.inventory and 'potion' in p.inventory:
        print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
        break

    if currentRoom == 'Garden':
        answer = input("There's a chest box in room, would you like to open it?(y or n)")
        if answer == 'y':
            p.winRiddle()
        else:
            print('You missed out')

    # If a player enters a room with a monster
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        m = Monster()
        print('Oh Noo MONSTER...')
        plea = input("beg for your life( y or n): ")
        if plea.lower() == 'y':
            print("Monster has let you live")
        elif plea.lower() == 'n':
            p.fight()
            m.health -= 50
            if m.health <= 0 and p.health > 0:
                print("You killed the monster")
            elif p.health <= 0:
                print("You didn't have a sword. A monster has got you...Game Over!!!")
            else:
                print('Both of you are dead')
        else:
            print('A monster has got you...Game Over!!!')
            break

