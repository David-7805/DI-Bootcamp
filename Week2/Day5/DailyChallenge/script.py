import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f'Card object: {self.suit} {self.value}'

class Deck:
    def __init__(self):
        complete_deck = []
        for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades']:
            for value in ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']:
                complete_deck.append(Card(suit, value))
        self.cards_in_game = complete_deck
        self.cards_no_longer_in_game = []

    def shuffle(self):
        random.shuffle(self.cards_in_game)

    def deal(self):
        index_card_to_deal = random.randint(0, len(self.cards_in_game) - 1) # - 1 because randint is inclusive and I don't want to pop a card that is out of range
        self.cards_no_longer_in_game.append(self.cards_in_game.pop(index_card_to_deal))
        print(self.cards_no_longer_in_game[-1])

    def new_game(self):
        self.cards_in_game.extend(self.cards_no_longer_in_game)
        self.cards_no_longer_in_game = []


my_deck = Deck()
print(len(my_deck.cards_in_game))
for card in my_deck.cards_in_game:
    print(card, end = '; ')
print()
my_deck.shuffle()
for card in my_deck.cards_in_game:
    print(card, end = '; ')
print()
my_deck.deal()
print(len(my_deck.cards_in_game))
print(len(my_deck.cards_no_longer_in_game))
my_deck.deal()
my_deck.deal()
print(len(my_deck.cards_in_game))
print(len(my_deck.cards_no_longer_in_game))
my_deck.new_game()
print(len(my_deck.cards_in_game))
print(len(my_deck.cards_no_longer_in_game))
