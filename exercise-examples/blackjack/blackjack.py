import random


class Card:
    def __init__(self, suit, face, value):
        self.suit = suit
        self.face = face
        self.value = value

    def __str__(self):
        return '{f} of {s}'.format(f=self.face, s=self.suit)

    def __repr__(self):
        return '{f} of {s}'.format(f=self.face, s=self.suit)


class Deck:
    def __init__(self):
        self.cards = self.create_deck()
        self.shuffle_deck()

    def shuffle_deck(self):
        random.shuffle(self.cards)

    def create_deck(self):
        deck = []
        suit = ['Diamonds', 'Hearts', 'Clubs', 'Spades']
        face = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9',
                '10', 'Jack', 'Queen', 'King']
        value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        for s in suit:
            x = 0
            for f in face:
                card = Card(s, f, value[x])
                deck.append(card)
                x += 1
        return deck

class BlackJack:
    def __init__(self):
        self.deck = Deck()
        self.players = []
        self.create_players()

    def create_players(self):
        pl_num = int(input("How many players are there? "))
        for pl in range(1, pl_num + 1):
            player = Hand(input('Player {num}, what is your name? '.format(num=pl)))
            self.players.append(player)

class Hand:
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.hand_value = 0

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


game = BlackJack()
print(game.players)

# for card in hand:
#     number_of_aces = 0
#     if card.face == 'Ace':
#         number_of_aces += 1
#     else:
#         value += card.value
#     if number_of_aces > 0:
#         for aces in range(number_of_aces):
#             if value + 11 < 21:
#                 value += 11
#             else:
#                 value += 1
