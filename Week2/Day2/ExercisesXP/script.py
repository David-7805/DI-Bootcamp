# Exercise 1 : Pets
class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around.'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

# 1.
class Siamese(Cat):
  def sing(self, sounds):
    return f'{sounds}'




# Exercise 2: Dogs
# 1. 2.
class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f'{self.name} is barking.'

    def run_speed(self):
        return self.weight / (self.age * 10)

    def fight(self, other_dog):
        if (self.run_speed() * self.weight) > (other_dog.run_speed() * other_dog.weight):
            return f'{self.name} won the fight.'
        elif (self.run_speed() * self.weight) < (other_dog.run_speed() * other_dog.weight):
            return f'{other_dog.name} won the fight.'
        else:
            return f'The fight between {self.name} and {other_dog.name} resulted in a draw.'

# Exercise 4: Family
class Family:
    def __init__(self, members, last_name):
        self.members = members
        self.last_name = last_name

    def born(self, **kwargs):
        self.members.append(kwargs)
        print(f'Congratulations with the birth of {kwargs['name']}!')

    def is_18(self, first_name):
        for family_member in self.members:
            if family_member['name'] == first_name:
                return family_member['age'] >= 18

    def family_presentation(self):
        print(f'Family {self.last_name}:\n')
        for family_member in self.members:
            for key, value in family_member.items():
                print(f'{key}: {value}')
            print()

# Exercise 5 : TheIncredibles Family
class TheIncredibles(Family):
    def __init__(self, members, last_name):
        super().__init__(members, last_name)

    def use_power(self, name):
        for member in self.members:
            if member['name'] == name:
                if member['age'] < 18:
                    raise Exception(f'{member['name']} is not over 18.')
                else:
                    print(member['power'])

    def incredible_presentation(self):
        print('**Here is our powerful family**')
        self.family_presentation()


if __name__=='__main__':
    # Exercise 1
    all_cats = [Siamese('Manon', 10), Bengal('Marija', 4), Chartreux('Estelle', 4)]
    sara_pets = Pets(all_cats)
    sara_pets.walk()

    # Exercise 2
    heavy_old_dog = Dog('Trump', 16, 60)
    heavy_middle_aged_dog = Dog('Frans', 7, 60)
    light_young_dog = Dog('Obama', 4, 30)

    print(heavy_old_dog.fight(heavy_middle_aged_dog))
    print(heavy_old_dog.fight(light_young_dog))
    print(heavy_middle_aged_dog.fight(light_young_dog))

    # Exercise 4

    list_of_family_members = [
        {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
        {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}
    ]

    family_palin = Family(list_of_family_members, 'Palin')
    family_palin.born(name='Jonathan', age=0, gender='Male', is_child=True)
    print(family_palin.is_18('Jonathan'))
    print(family_palin.is_18('Michael'))
    print(family_palin.is_18('Sarah'))
    family_palin.family_presentation()

    members_incredibles = [
        {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
        {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
    ]

    incredibles = TheIncredibles(members_incredibles, "Incredibles")
    incredibles.incredible_presentation()
    incredibles.born(name = "Baby Jack", age = 0, gender = 'Male', is_child = True, power = 'unknown power', incredible_name = 'Jack-Jack')
    incredibles.incredible_presentation()