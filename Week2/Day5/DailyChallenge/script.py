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
        self.cards_to_deal = complete_deck
        self.cards_dealt = []

    def shuffle(self):
        random.shuffle(self.cards_to_deal)

    def deal(self):
        index_card_to_deal = random.randint(0, len(self.cards_to_deal) - 1) # - 1 because randint is inclusive and I don't want to pop a card that is out of range
        self.cards_dealt.append(self.cards_to_deal.pop(index_card_to_deal))
        print(self.cards_dealt[-1])

    def new_game(self):
        self.cards_to_deal.extend(self.cards_dealt)
        self.cards_dealt = []

    def show_deck(self):
        print(f"{len(self.cards_to_deal)} cards not dealt yet:", end = ' ')
        for card in self.cards_to_deal:
            print(card, end = '; ')
        print(f"\n{len(self.cards_dealt)} cards already dealt:", end = ' ')
        for card in self.cards_dealt:
            print(card, end = '; ')
        print()


my_deck = Deck()
my_deck.show_deck()
print()
my_deck.shuffle()
my_deck.show_deck()
print()
my_deck.deal()
my_deck.deal()
my_deck.deal()
print()
my_deck.show_deck()
print()
my_deck.new_game()
my_deck.show_deck()
print()
print(len(set(my_deck.cards_to_deal))) # to check that I still have 52 unique cards after starting a new game
