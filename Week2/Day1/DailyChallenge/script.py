class Farm:
    def __init__(self, name):
        self.name = name
        self.animals = {}

    def add_animal(self, animal, amount=1):
        if animal not in self.animals.keys():
            self.animals[animal] = amount
        else:
            self.animals[animal] += amount

    def get_info(self):
        print(f"{self.name}'s farm\n")
        for animal, amount in self.animals.items():
            print(f'{animal} : {amount}')
        print('\n    E-I-E-I-0!')
        return '' # Oddly enough it prints the return statement (or 'None') to the screen

    def get_animal_types(self):
        list_of_animal_types = list(self.animals.keys())
        list_of_animal_types.sort()
        return list_of_animal_types


    def get_short_info(self):
        print(f"{self.name}'s farm has ", end='')
        def how_to_display(animal):
            if self.animals[animal] > 1:
                return f'{animal}s'
            elif self.animals[animal] == 1:
                return f'a {animal}'

        for animal in self.get_animal_types()[0: -2]:
            print(f'{how_to_display(animal)}', end=', ')
        for animal in self.get_animal_types()[-2: -1]:
            print(f'{how_to_display(animal)}', end=' and ')
        for animal in self.get_animal_types()[-1:]:
            print(f'{how_to_display(animal)}', end='.\n')



macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())

print(macdonald.get_animal_types())
macdonald.get_short_info()


