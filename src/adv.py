from room import Room

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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

last_room = None

# Write a loop that:
while True:
# * Prints the current room name
    print(player.current_room.name)
# * Prints the current description (the textwrap module might be useful here).
    print(wrapper.fill(player.current_room.description))
# * Waits for user input and decides what to do.
    direction = input('Where shall you proceed next?')
    # Checking to see if user entered an allowed move.
    if direction.lower() in allowed_moves:
        # If the user enters "q", quit the game.
        if direction.lower() == 'q':
            print(f'Goodbye {player.name}')
            break
        else:
        # If the user enters a cardinal direction, attempt to move to the room there.
            selected_room = player.current_room.__getattribute__(f'{direction.lower()}_to')
            #If the direction is valid update the players current room
            if selected_room != None:
                # updating room
                player.current_room = selected_room
                print("-----------------------------------------------------------------------------------------------------")
            # Print an error message if there isn't a location in the direction specied
            elif selected_room == None:
                print(f"There isn't a thing in that direction, {player.name}")
                print("-----------------------------------------------------------------------------------------------------")
    # Print an error message if the movement isn't allowed.
    else:
        print("-----------------------------------------------------------------------------------------------------")
        print("Enter a valid direction or 'q' to quit")
