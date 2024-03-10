# Exercise 1: Cats

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age


# 1.
black_cat = Cat('Sara', 5)
orange_cat = Cat('Vera', 7)
grey_cat = Cat('Diana', 6)


# 2
def oldest_cat_finder(list_of_cats):
    max_age = 0
    for cat in list_of_cats:
        if cat.age > max_age:
            oldest_cat = cat
            max_age = cat.age
    return oldest_cat


# 3.
list_of_cats = [black_cat, orange_cat, grey_cat]
oldest_cat = oldest_cat_finder(list_of_cats)
print(f'The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.')

# Exercise 2: Dogs
# 1. 2. 3. 4.
class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f'{self.name} goes woof!')

    def jump(self):
        print(f'{self.name} jumps {self.height * 2} cm high!')


# 5. 6.
davids_dog = Dog("Rex", 50)
print(f'Name: {davids_dog.name}\nHeight: {davids_dog.height} cm.')
davids_dog.bark()
davids_dog.jump()

# 7. 8.
sarahs_dog = Dog('Teacup', 20)
print(f'Name: {sarahs_dog.name}\nHeight: {sarahs_dog.height} cm.')
sarahs_dog.bark()
sarahs_dog.jump()

# 9.
if davids_dog.height > sarahs_dog.height:
    print(davids_dog.name)
elif davids_dog.height < sarahs_dog.height:
    print(sarahs_dog.name)
else:
    print(f'{davids_dog.name} and {sarahs_dog.name} have equal height.')

# Exercise 3 : Who’s The Song Producer?
# 1. 2.
class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


# 3.
stairway = stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])

# 4.
stairway.sing_me_a_song()

# Exercise 4: Afternoon At The Zoo
# 1. 2. 3. 4. 5. 6. 7.
class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

    def add_animals(self, *new_animals):
        if new_animals not in self.animals:
            self.animals.extend(new_animals)

    def get_animals(self):
        for animal in self.animals:
            print(animal)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals(self):
        dict_of_animals = {}
        self.animals.sort()
        number_key = 1
        for animal in self.animals:
            if dict_of_animals == {}:
                dict_of_animals[number_key] = animal
            elif animal[0] == dict_of_animals[number_key][0]:
                dict_of_animals[number_key] = [dict_of_animals[number_key], animal]
            elif animal[0] == dict_of_animals[number_key][0][0]:
                dict_of_animals[number_key].append(animal)
            else:
                number_key += 1
                dict_of_animals[number_key] = animal
        return dict_of_animals

    def get_groups(self):
        print(self.sort_animals())


# 8.
ramat_gan_safari = Zoo('Ramat Gan Safari')
ramat_gan_safari.add_animals("Ape", "Chimpanzee", "Baboon", "Bear", 'Cat', 'Cougar', 'Eel', 'Emu', "Gorilla", "Orangutan")
ramat_gan_safari.get_animals()
ramat_gan_safari.sell_animal('Eel')
print(ramat_gan_safari.animals)
ramat_gan_safari.sort_animals()
ramat_gan_safari.get_groups()
