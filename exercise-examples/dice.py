import random

class Die:
    possible_values = {
    	1:

    ['+-------+',
    '|       |',
    '|   o   |',
    '|       |',
    '+-------+',],
    	2:

    ['+-------+',
    '| o     |',
    '|       |',
    '|     o |',
    '+-------+'],
    	3:

    ['+-------+',
    '| \\   / |',
    '| ^   ^ |',
    '| ----- |',
    '+-------+'],
    	4:
    [
    '+-------+',
    '| o   o |',
    '|       |',
    '| o   o |',
    '+-------+'],
    	5:
    [
    '+-------+',
    '| o   o |',
    '|   o   |',
    '| o   o |',
    '+-------+'
    ],
    	6:
[
    '+-------+',
    '| o   o |',
    '| o   o |',
    '| o   o |',
    '+-------+'
]
    }

    def __init__(self):
        self.value = 1
        self.held = False
        self.art = self.possible_values[self.value]


    def roll(self):
        if self.held == True:
            pass
        else:
            self.value = random.randint(1, 6)
            self.art = self.possible_values[self.value]
