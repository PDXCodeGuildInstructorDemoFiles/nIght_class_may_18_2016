import random
from dice import Die

class Player:
    def __init__(self, name):
        self.name = name
        self.round = 1
        self.die1 = Die()
        self.die2 = Die()

    def roll_round(self):
        self.die1.roll()
        self.die2.roll()
        self.display_dice()
        query = input('Would you like to hold die A or B or press Enter to continue? ')
        if query.upper() == 'A':
            if self.die1.held == True:
                self.die1.held = False
            else:
                if self.die1.value != 6:
                    self.die1.held = True
                else:
                    print('You can not hold a 6.')
        elif query.upper() == 'B':
            if self.die2.held:
                self.die2.held = False
            else:
                if self.die2.value != 6:
                    self.die2.held = True
                else:
                    print('You can not hold a 6.')

    def display_dice(self):
        separator = ' | '
        spaces = ' ' * int(len(self.die1.art[0]) / 2)
        print(spaces + "A" + spaces + separator + spaces + "B")
        print(self.die1.art[0] + separator + self.die2.art[0])
        print(self.die1.art[1] + separator + self.die2.art[1])
        print(self.die1.art[2] + separator + self.die2.art[2])
        print(self.die1.art[3] + separator + self.die2.art[3])
        print(self.die1.art[4] + separator + self.die2.art[4])
        if self.die1.held:
            print("  HELD   " + separator + spaces + " ")
        elif self.die2.held:
            print("         " + separator + "  HELD   ")

    def check_win(self):
        if self.die1.value  == 3 and self.die2.value == 3:
            print("Why so angry? Go back to round One")
            self.round = 1
            self.die1.held = False
            self.die2.held = False

        elif self.round == 1:
            if self.die1.value + self.die2.value == 3:
                print("Welcome to round 2, {}".format(self.name))
                self.round = 2
                self.die1.held = False
                self.die2.held = False

        elif self.round == 2:
            if self.die1.value == 3 and self.die2.value == 4 or self.die1.value == 4 and self.die2.value == 3:
                print("Welcome to round 3, {}".format(self.name))
                self.round = 3
                self.die1.held = False
                self.die2.held = False

        elif self.round == 3:
            if self.die1.value + self.die2.value == 11:
                print("You win, {}!".format(self.name))
                quit()

players = []
plcount = input('How many players are there? ')
for pl in range(int(plcount)):
    player = Player(input("What is your name? "))
    players.append(player)

while True:
    for pl in players:
        print('{pl}, you are in round {r}'.format(pl=pl.name, r=pl.round))
        pl.roll_round()
