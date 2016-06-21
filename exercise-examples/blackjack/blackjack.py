import random


class Card:
    def __init__(self, suit, face, value):
        self.suit = suit
        self.face = face
        self.value = value

    def __repr__(self):
        return '{f} of {s}'.format(f=self.face, s=self.suit)


class Deck:
    def __init__(self, number_of_decks):
        self.cards = self.create_deck(number_of_decks)
        self.shuffle_deck()

    def shuffle_deck(self):
        random.shuffle(self.cards)

    def create_deck(self, number_of_decks):
        deck = []
        suit = ['Diamonds', 'Hearts', 'Clubs', 'Spades']
        face = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9',
                '10', 'Jack', 'Queen', 'King']
        value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        for z in range(number_of_decks):
            for s in suit:
                x = 0
                for f in face:
                    card = Card(s, f, value[x])
                    deck.append(card)
                    x += 1
        return deck


class BlackJack:
    def __init__(self, number_of_decks=6):
        self.deck = Deck(number_of_decks)
        self.players = []
        self.dealer = Hand('Dealer')
        self.create_players()

    def create_players(self):
        pl_num = int(input("How many players are there? "))
        for pl in range(1, pl_num + 1):
            player = Hand(input('Player {num}, what is your name? '.format(num=pl)))
            self.players.append(player)

    def deal(self):
        self.dealer.cards.append(self.deck.cards.pop())
        self.dealer.cards.append(self.deck.cards.pop())
        for pl in self.players:
            c1 = self.deck.cards.pop()
            c2 = self.deck.cards.pop()
            pl.cards.append(c1)
            pl.cards.append(c2)

    def hit(self):
        card = self.deck.cards.pop()
        return card

    def clear_round(self):
        for pl in players:
            pl.hand_lost = False

    def run_game(self):
        self.deal()
        print("Dealer is showing a {}".format(self.dealer.cards[0]))
        for pl in self.players:
            pl_turn = True
            while pl_turn:
                print("Dealer is showing a {}.".format(self.dealer.cards[0]))
                pl.display_hand()
                if pl.hand_value == 21:
                    print("BlackJack! You win this hand {}!".format(pl.name))
                    pl_turn = False
                    continue
                elif pl.hand_value > 21:
                    print('{} busts!'.format(pl.name))
                    pl_turn = False
                    continue
                cards_in_hand = [str(x) for x in pl.cards]
                print('{}, you hand consists of {} and {}'.format(pl.name, ', '.join(cards_in_hand[:-1]), cards_in_hand[-1]))
                choice = input('Do you wish to hit or stay: ').lower()
                if choice == 'hit':
                    pl.cards.append(self.hit())
                    pl.get_score()
                    print(pl.name)
                    print(pl.hand_value)
                elif choice == 'stay':
                    pl_turn = False
                    pl.get_score()
                    print(pl.name)
                    print(pl.hand_value)
                else:
                    print("I don't understand that...")
        else:
            self.dealer.get_score()
            dealer_turn = True
            while dealer_turn:
                self.dealer.get_score()
                print("Dealer shows {}. {} total points".format(self.dealer.cards, self.dealer.hand_value))
                if self.dealer.hand_value < 17:
                    self.dealer.cards.append(self.hit())
                else:
                    dealer_turn = False
            else:
                for pl in self.players:
                    if pl.hand_value > self.dealer.hand_value and not pl.hand_lost:
                        print("You win {}!".format(pl.name))
                    elif pl.hand_value == self.dealer.hand_value:
                        print("You push {}.".format(pl.name))
                    else:
                        print("You lose {}!".format(pl.name))


class Hand:
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.hand_value = 0
        self.hand_lost = False

    def display_hand(self):
        print()
        print("**********")
        self.get_score()
        print(self.name)
        print(self.hand_value)
        print("**********")
        print()

    def get_score(self):
        self.hand_value = 0
        number_of_aces = 0
        for card in self.cards:
            if card.face == 'Ace':
                number_of_aces += 1
            else:
                self.hand_value += card.value
        if number_of_aces > 0:
            for aces in range(number_of_aces):
                self.hand_value += 1
            else:
                if self.hand_value + 10 <= 21:
                    self.hand_value += 10

    def __repr__(self):
        return self.name


# game = BlackJack(6)
# game.run_game()
def create_players():
    players = []
    pl_num = int(input("How many players are there? "))
    for pl in range(1, pl_num + 1):
        player = Hand(input('Player {num}, what is your name? '.format(num=pl)))
        players.append(player)
    print(players)
create_players()
