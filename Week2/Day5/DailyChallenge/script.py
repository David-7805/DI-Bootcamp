import random

# Part 1: Quizz:
# * What is a class? A class is a blueprint that defines which attributes and methods a future object of that class
#   will have.
# * What is an instance? An instance of a class is an object that was instantiated by using the name of the class and
#   if required also parameters that will be the values of the attributes of the object.
# * What is encapsulation? Encapsulation is the bundling of attributes and methods within a class. It is also the
#   possibility to have _protected and __private attributes and methods within a class. _protected attributes/methods
#   signal to the one who uses them that it is better not to change them, while __private attributes/methods are not
#   visible to the programmer and have a more complicated way to access them, like object_name._ClassName__attribute.
# * What is abstraction? Abstraction is the possibility to use class methods (and attributes) just by typing a period
#   after the object name without having to know how they are programmed.
# * What is inheritance? Inheritance is the idea that classes can have relations between them. With inheritance a class
#   can be a child of another class and inherit attributes and methods from that parent class, in case they are not
#   defined in the child class itself.
# * What is multiple inheritance? Multiple inheritance is the possibility that a class can inherit attributes and
#   methods from more than only one parent class. In that case the interpreter looks for attributes and methods in an
#   order that is named method resolution order or MRO, see the last question of the quiz.
# * What is polymorphism? Polymorphism is the fact that a function can be defined in which a method is used that two
#   different classes both have, even though these methods do different things dependent on the class the object
#   belongs to.
# * What is method resolution order or MRO? Method resolution order defines the order in which the interpreter will
#   look for methods and attributes of an object in case it belongs to a class that inherits from more than one parent
#   class and also from grandparent classes. The order is depth-first left-to-right, meaning that the interpreter first
#   looks in the class itself, than in its parents in the order in which they were written while creating the class,
#   and then in its grandparents.

# Part 2: Create A Deck Of Cards Class
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
