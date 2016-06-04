def game():
    print("Welcome to the A-Maze-ing Maze! I dare you to escape!")
    current_room = room0()
    while current_room != exit:
        current_room = current_room()
    current_room()


def process_user_movement(description, doors):
    """This is the process_user_movement function that will
       handle a user's inpt.

    Args:
        doors: A description of the current room
        description: dictionary with door:location sets
    """
    print(description)
    temp = input('pause')
    return doors['south']


def room0():
    # description
    description = "This room is very small. You barely fit here. You're like \
    Alice in that crazy-tiny-room thing."
    # doors
    # where those doors Go
    doors = {"south": room1, 'east': room1}

    return process_user_movement(description, doors)


def room1():
    description = "room1"
    doors = {"south": room1}
    return process_user_movement(description, doors)

game()
