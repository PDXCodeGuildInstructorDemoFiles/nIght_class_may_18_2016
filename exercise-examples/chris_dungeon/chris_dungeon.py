import random
from monsterinfo import m_names, r_desc, magic_w_names, sword_w_names
from monsterinfo import helm_a_name, chest_a_name, pants_a_name
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
        self.physical = 10
        self.magic = 10
        self.location = None
        self.weapon = None
        self.helm = None
        self.chest = None
        self.pants = None
        self.backback = {}

    def show_backpack(self):
        for key, item in self.backback.items():
            print(str(key) + ' - ' + item.name)

    def backpack_menu(self):
        while True:
            print('*' * 40)
            self.show_backpack()
            print('*' * 40)
            print("To equip")

    def move(self, room):
        self.location = room

    def user_interaction(self):
        # os.system('cls' if os.name == 'nt' else 'clear')
        print(self.location.description)
        if self.location.visited:
            print()
            print('This room looks familiar...')
        else:
            self.location.visited = True
        if self.location.monster.alive:
            self.combat(self.location.monster)
        print("You see doors to the " + ', '.join(self.location.doors.keys()), end='. ')
        choice = input('What direction would you like to go? ').lower()
        if choice in self.location.doors:
            self.move(self.location.doors[choice])
        elif choice == 'backpack':
            self.show_backpack()
        elif choice == 'exit':
            exit()
        else:
            print("I do not understand. Please try again.")

    def combat(self, mon):
        print("You are being attacked by {}".format(self.location.monster.name))
        while mon.hp > 0 and self.hp > 0:
            print()
            print("Your HP is {0}".format(self.hp))
            print('{0} HP is {1}'.format(mon.name, mon.hp))
            attack = input('Attack with: (S)imple, (P)hysical or (M)agic? ').lower()
            if attack == 's':
                player_attack = random.randint(3, 10)
                mon.hp -= player_attack
                print("You hit {0} for {1}".format(mon.name, player_attack))
                mon_attack = mon.weapon.dmg
                self.hp -= mon_attack
                print("{0} attacks you for {1}".format(mon.name, mon_attack))
            elif attack == 'p':
                player_attack = self.physical + random.randint(3, 10)
                mon.hp -= player_attack
                print("You hit {0} for {1}".format(mon.name, player_attack))
                mon_attack = mon.weapon.dmg
                self.hp -= mon_attack
                print("{0} attacks you for {1}".format(mon.name, mon_attack))
            elif attack == 'm':
                player_attack = self.magic + random.randint(3, 10)
                mon.hp -= player_attack
                print("You hit {0} for {1}".format(mon.name, player_attack))
                mon_attack = mon.weapon.dmg
                self.hp -= mon_attack
                print("{0} attacks you for {1}".format(mon.name, mon_attack))
            else:
                print("I do not understand that command")
        else:
            if self.hp <= 0:
                print("You have died. Such a shame.")
                exit()
            else:
                mon.alive = False
                print('You have defeated {0}. After digging around his body you find {1}'.format(mon.name, mon.loot))
                item_number = len(self.backback)
                self.backback[item_number] = mon.loot
                mon.loot = None

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Monster:
    def __init__(self, name, weapon, lt):
        self.name = name
        self.alive = True
        self.hp = random.randint(85, 110)
        self.loot = lt
        self.weapon = weapon

    def attack(self):
        apow = self.weapon.power

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Weapon:
    def __init__(self, dmg_type, dmg, name):
        self.dmg_type = dmg_type
        self.dmg = dmg
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Armor:
    def __init__(self, ar, tpe, name):
        self.armor_rating = ar
        self.tpe = tpe
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


def create_armor(tpe, name_list, number):
    lst = []
    for h in range(number):
        name = random.choice(name_list)
        name_list.remove(name)
        ar = random.randint(1, 5)
        crit = random.randint(1, 2)
        if crit == 2:
            ex_ar = random.choice([10, 10, 10, 10, 15, 15, 20])
            ar += ex_ar
            if ex_ar == 20:
                name += ' of Ultamate Power'
            else:
                name += ' of Power'
        item = Armor(ar, tpe, name)
        lst.append(item)
    return lst


# Create random weapons
weapons = []
for wp in range(20):
    wp_type = random.randint(1, 2)
    if wp_type == 1:
        name = random.choice(magic_w_names)
        magic_w_names.remove(name)
        dmg = random.randint(5, 10)
        crit = random.randint(1, 2)
        if crit == 2:
            ex_dmg = random.choice([10, 10, 10, 10, 15, 15, 20])
            dmg += ex_dmg
            if ex_dmg == 20:
                name += ' of Ultamate Power'
            else:
                name += ' of Power'
        weapon = Weapon('Magic', dmg, name)
        weapons.append(weapon)
    else:
        name = random.choice(sword_w_names)
        sword_w_names.remove(name)
        dmg = random.randint(5, 10)
        crit = random.randint(1, 2)
        if crit == 2:
            ex_dmg = random.choice([10, 10, 10, 10, 15, 15, 20])
            dmg += ex_dmg
            if ex_dmg == 20:
                name += ' of Ultamate Power'
            else:
                name += ' of Power'
        weapon = Weapon('Physical', dmg, name)
        weapons.append(weapon)


helms = create_armor('Helm', helm_a_name, 10)
chests = create_armor('Chest', chest_a_name, 10)
pants = create_armor('Pants', pants_a_name, 10)
loot = pants + chests + helms + weapons

# Create random monsters for each room using names from m_names
monsters = []
for mnstrs in range(10):
    name = random.choice(m_names)
    m_names.remove(name)
    wpn = random.choice(weapons)
    weapons.remove(wpn)
    lt = random.choice(loot)
    loot.remove(lt)
    mon = Monster(name, wpn, lt)
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



# Run the game
while True:
    player.user_interaction()
