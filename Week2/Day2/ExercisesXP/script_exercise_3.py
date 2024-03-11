from script import Dog
from random import choice

class PetDog(Dog):
    def __init__(self, name, age, weight, trained=False):
        super().__init__(name, age, weight)
        self.trained = trained

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *dogs):
        print(f'{self.name}, ', end = '')
        for dog in dogs[0: -2]:
            print(f'{dog.name}, ', end = '')
        for dog in dogs[-2: -1]:
            print(f'{dog.name} and ', end = '')
        for dog in dogs[-1: ]:
            print(f'{dog.name} all play together.')

    def do_a_trick(self):
        tricks = ['does a barrel roll!', 'stands on his back legs!', 'shakes your hand!', 'plays dead!']
        print(f'{self.name} {choice(tricks)}')

frenkie = PetDog('Frenkie', 5, 50)
johnny = Dog('Johhny', 8, 40)
david = Dog('David', 9, 45)
jochie = Dog('Jochie', 7, 35)
daniel = Dog('Daniel', 9, 43)

frenkie.train()
print(frenkie.trained)
frenkie.play(johnny, david, jochie, daniel)
frenkie.do_a_trick()



