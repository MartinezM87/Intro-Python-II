from room import Room
from player import Player
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
room['outside'].e_to = None
room['outside'].s_to = None
room['outside'].w_to = None

room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['foyer'].s_to = room['outside']
room['foyer'].w_to = None

room['overlook'].n_to = None
room['overlook'].e_to = None
room['overlook'].s_to = None
room['overlook'].w_to = room['foyer']

room['narrow'].n_to = room['treasure']
room['narrow'].e_to = None
room['narrow'].s_to = None
room['narrow'].w_to = room['foyer']

room['treasure'].n_to = None
room['treasure'].e_to = None
room['treasure'].s_to = room['narrow']
room['treasure'].w_to = None

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player(room['outside'])

# Write a loop that:
while True:
    # * Prints the current room name
    print(player.location)
    
    # * Prints the current description (the textwrap module might be useful here).
    # * Waits for user input and decides what to do.
    
    # If the user enters a cardinal direction, attempt to move to the room there.
    # Print an error message if the movement isn't allowed.
    #
    # If the user enters "q", quit the game.
    command = input("> ").split(',')


    if command[0] == 'q':
        break
    elif command[0] == 'n':
        if player.location.n_to == None:
            print("--- Try again. --- \n")
            continue
        else:
            player = Player(player.location.n_to)
    elif command[0] == 's':
        if player.location.s_to == None:
            print("--- Try again. --- \n")
            continue
        else:
            player = Player(player.location.s_to)
    elif command[0] == 'e':
        if player.location.e_to == None:
            print("--- Try again. --- \n")
            continue
        else:
            player = Player(player.location.e_to)
    elif command[0] == 'w':
        if player.location.w_to == None:
            print("--- Try again. --- \n")
            continue
        else:
            player = Player(player.location.w_to)