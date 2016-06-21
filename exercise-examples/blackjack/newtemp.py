class Card:
    def __init__(self, suit, face, value):
        self.suit = suit
        self.face = face
        self.value = value

    def __repr__(self):
        return '{f} of {s}'.format(f=self.face, s=self.suit)

card1 = Card('Hearts', 'Ace', 1)
card2 = Card('Diamonds', 'Ace', 1)

print(card1)
print(card2)
print([card1, card2])
