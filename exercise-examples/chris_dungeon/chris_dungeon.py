import random
from monsterinfo import m_names, r_desc
import os


class Room:
    def __init__(self, name, description, doors, monster):
        self.name = name
        self.description = description
        self.monster = monster
        self.doors = doors
        self.visited = False

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100

        self.location = None
        self.weapon = None
        self.helm = None
        self.chest = None
        self.pants = None
        self.backback = []

    def move(self, room):
        self.location = room

    def user_interaction(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(self.location.description)
        if self.location.visited:
            print()
            print('This room looks familiar...')
        else:
            self.location.visited = True
        if self.location.monster.alive:
            self.combat()
        print("You see doors to the " + ', '.join(self.location.doors.keys()), end='. ')
        choice = input('What direction would you like to go? ').lower()
        if choice in self.location.doors:
            self.move(self.location.doors[choice])
        elif choice == 'exit':
            exit()
        else:
            print("I do not understand. Please try again.")

    def combat(self):
        print("You are being attacked by {}".format(self.location.monster.name))
        attack = input('Attack with: Physical or Magic ')

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Monster:
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.hp = random.randint(85, 110)
        self.loot = None

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

# Create random monsters for each room using names from m_names
monsters = []
for mnstrs in range(10):
    name = random.choice(m_names)
    m_names.remove(name)
    mon = Monster(name)
    monsters.append(mon)

# Create Rooms
# name: Name of room
# description: Random Room description from r_desc
# doors: doors to other rooms
# monster: random monster
room01 = Room('room01', 'You awake in a strange empty rooom.', {}, monsters.pop(random.randrange(len(monsters))))
room02 = Room('room02', r_desc.pop(random.randrange(len(r_desc))), {}, monsters.pop(random.randrange(len(monsters))))
room03 = Room('room03', r_desc.pop(random.randrange(len(r_desc))), {}, monsters.pop(random.randrange(len(monsters))))
room04 = Room('room04', r_desc.pop(random.randrange(len(r_desc))), {}, monsters.pop(random.randrange(len(monsters))))
room05 = Room('room05', r_desc.pop(random.randrange(len(r_desc))), {}, monsters.pop(random.randrange(len(monsters))))
room06 = Room('room06', r_desc.pop(random.randrange(len(r_desc))), {}, monsters.pop(random.randrange(len(monsters))))
room07 = Room('room07', r_desc.pop(random.randrange(len(r_desc))), {}, monsters.pop(random.randrange(len(monsters))))
room08 = Room('room08', r_desc.pop(random.randrange(len(r_desc))), {}, monsters.pop(random.randrange(len(monsters))))
room09 = Room('room09', r_desc.pop(random.randrange(len(r_desc))), {}, monsters.pop(random.randrange(len(monsters))))
room10 = Room('room10', r_desc.pop(random.randrange(len(r_desc))), {}, monsters.pop(random.randrange(len(monsters))))

# Make room connections
room01.doors = {'south': room02}
room02.doors = {'south': room06}
room03.doors = {'north': room01, 'south': room07}
room04.doors = {'south': room08}
room05.doors = {'east': room06}
room06.doors = {'north': room02, 'east': room07, 'west': room05}
room07.doors = {'north': room03, 'east': room08, 'west': room06}
room08.doors = {'north': room04, 'south': room09, 'west': room07}
room09.doors = {'north': room08, 'east': room10}
room10.doors = {"west": room09}

# Instanciate player and place them in room01
player = Player(input("What is your name hero? "))
player.move(room01)

print(monsters)

# Run the game
while True:
    player.user_interaction()
