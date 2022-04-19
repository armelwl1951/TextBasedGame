# User instructions
def show_instructions():
    # main menu commands
    print('MYSTERY SCIENCE THEATRE 3000 TEXT ADVENTURE GAME')
    print("You are trapt on the Satellite of Love in space by the mad scientist Dr. Forrester ")
    print("and his henchman TV's Frank.")
    print('They make you watch Z-grade movies waiting for you to go insane.')
    print('Movie Sign is on and the ship will self-destruct if you are not in the theatre to watch the bad movie')
    print('You need to gather the 6 items needed to escape this nightmare and finally make it back to earth.')
    print('MOVE COMMANDS: go South, go North, go East, go West')
    print("Pick up item: get 'item name'\n")


# main function
def main():
    # display instructions
    show_instructions()

    # A dictionary linking a room to other rooms and carrying items
    rooms = {
        'Main Deck': {'South': 'Storage Bay', 'North': 'Research Deck',
                      'West': 'Rocket #9', 'East': 'Security Hallway', 'item': None},
        'Rocket #9': {'East': 'Main Deck', 'item': 'Crow T. Robot'},  # Crow T. Robot
        'Storage Bay': {'North': 'Main Deck', 'East': 'Kitchen', 'item': 'Repair Kit'},  # Repair Kit
        'Kitchen': {'West': 'Storage Bay', 'item': 'Popcorn'},  # Popcorn
        'Research Deck': {'East': 'Library', 'South': 'Main Deck', 'item': 'Nanobots'},  # Nanobots
        'Library': {'West': 'Research Deck', 'item': 'Tom Servo'},  # Tom Servo
        'Security Hallway': {'West': 'Main Deck', 'North': 'Theatre',
                             'item': 'Star-Trek Replica Transporter'},  # Star-Trek Replica Transporter
        'Theatre': {'South': 'Security Hallway', 'item': 'Self Destruct'}  # Self Destruct
    }

    # starting room
    current_room = 'Main Deck'
    inventory = []

    # Loop to move between rooms
    while True:
        # If current_room is Main Deck then break loop
        if current_room == 'Theatre':
            print('\nYou are in the', current_room)
            print('The movie is ready to play!')
            if len(inventory) == 6:
                print('\nYou used the Nanobots to fix the screen')
                print('You ate the Popcorn to get energy')
                print('You used the Repair Kit to fix Tom Servos hover skirt')
                print('You gathered your robot friends')
                print('You use the Star-Trek Replica Transporter to switch places with')
                print('the evil scientist and his henchman and now are back on earth!')
            else:
                print('\nOh no! You have no items to fix the screen and the movie screen.')
                print('You have no popcorn for energy.')
                print("You're friends can't help you.")
                print("The movie can't play and the Satellite of Love explodes. BOOM!")
            break

        # Printing current_room
        print('\nYou are in the', current_room)

        # Taking user input to pick up items
        if rooms[current_room]['item'] is not None:
            print('You see a', rooms[current_room]['item'])
            opinion = input('Get ' + rooms[current_room]['item'] + '?(Y/N): ').upper()
            # Validating user input
            while opinion not in ['Y', 'N']:
                print('Invalid input. Try again ')
                opinion = input('Get ' + rooms[current_room]['item'])
            if opinion == 'Y':
                inventory.append(rooms[current_room]['item'])
                rooms[current_room]['item'] = None
        else:
            print('Already collected item or nothing is in this room')

        # print inventory
        print('Inventory:', inventory)

        # Taking user input to move
        direction = input('Where do you want to go? ').title()
        directions = list(rooms[current_room].keys())
        directions.remove('item')
        # validate direction
        while direction not in directions:
            print('Invalid direction. Try again')
            direction = input('Where do you want to go? ').title()

        # Next room setup
        next_room = rooms[current_room][direction]
        print('You are now in', next_room)
        print('--------------------------------------')

        # Update next room
        current_room = next_room

    # Print ending message
    print('\nThanks for playing the game. Hope you enjoyed it.')

    # Call main room
main()
