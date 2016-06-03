import random

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def roll(self):
        r1 = random.randint(1,6)
        r2 = random.randint(1,6)

        if r1 == 3 and r2 == 3 or r1 == 6 and r2 == 6:
            self.score = 0
            print('You rolled a {0} and {1}'.format(r1, r2))
            print('You loose all your points!')
        else:
            print('You rolled a {0} and {1}'.format(r1, r2))
            self.score += r1 + r2


player1 = Player(input('What is player 1\'s name? '))
player2 = Player(input('What is player 2\'s name? '))


while player1.score <= 20 and player2.score <= 20:
    print('{p1}, go!'.format(p1=player1.name))
    player1.roll()
    print('{p1}, your score is {s}'.format(p1=player1.name, s=player1.score))
    input('Press enter for next player.')
    print('{p2}, your turn!'.format(p2=player2.name))
    player2.roll()
    print('{p2}, your score is {s}'.format(p2=player2.name, s=player2.score))
    input('Press enter for next round.')
