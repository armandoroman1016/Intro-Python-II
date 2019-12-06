from room import Room
from item import Item

# Declare Items

sword = Item('Sword', 'A valiant knights sword')
oil = Item('Oil Can', 'Useful for various things')
log = Item('Log', 'Useful for cooking and warmth')
slingshot = Item('Slingshot', 'Can be used to shoot targets from a distance')
mirror = Item('Old Mirror', 'You Can Peek around corners where you dont want to be seen')
pick = Item('Lock Pick', 'Is there treasure!?')

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [mirror]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [oil_can, slingshot]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [lock_pick]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""" , [sword]),
}







# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

from player import Player
import textwrap 

# Make a new player object that is currently in the 'outside' room.
print("-----------------------------------------------------------------------------------------------------")
playerName = input('Welcome to Dark Island, to get started enter your name => ')
player = Player(playerName, room['outside'])

# Player instructions
print("-----------------------------------------------------------------------------------------------------")
print("To navigate around the island enter 'n', 's', 'e', 'w', to look for the treasure or enter 'q' to quit.")
print("-----------------------------------------------------------------------------------------------------")


wrapper = textwrap.TextWrapper(width=100)

allowed_moves = ['n', 's', 'e', 'w', 'q']
verbs = ['get', 'take', 'drop']

# Write a loop that:
while True:
# * Prints the current room name
    print(player.current_room.name)
# * Prints the current description (the textwrap module might be useful here).
    print(wrapper.fill(player.current_room.description))
    player.current_room.print_items()
# * Waits for user input and decides what to do.
    cmd = input('What shall you do?')
    # Checking to see if user entered an allowed move.
    nextMove = cmd.split(' ')
    verb = nextMove[0]
    if verb in verbs and len(nextMove) > 1:
        item = nextMove[1]
        if verb == 'get' or verb == 'take' \
        and item in player.current_room.items:
            player.add_to_inventory(item)
            player.current_room.remove_item(item)
        else:
            print("Sorry that item isn't in this room")
    elif verb.lower() == 'drop':
        if item not in player.inventory:
            print(f'{item} is not in your inventory')
        elif item in player.inventory:
            player.remove_from_inventory(item) 
            player.current_room.add_to_inventory(item)
            item.on_drop()
    elif cmd.lower() in allowed_moves:
        # If the user enters "q", quit the game.
        if cmd.lower() == 'q':
            print(f'Goodbye {player.name}')
            break
        else:
        # If the user enters a cardinal cmd, attempt to move to the room there.
            selected_room = player.current_room.__getattribute__(f'{cmd.lower()}_to')
            #If the cmd is valid update the players current room
            if selected_room != None:
                # updating room
                player.current_room = selected_room
                print("-----------------------------------------------------------------------------------------------------")
            # Print an error message if there isn't a location in the cmd specied
            elif selected_room == None:
                print("-----------------------------------------------------------------------------------------------------")
                print(f"There isn't a thing in that direction, {player.name}")
    # Print an error message if the movement isn't allowed.
    else:
        print("-----------------------------------------------------------------------------------------------------")
        print("Enter a valid command or 'q' to quit")
