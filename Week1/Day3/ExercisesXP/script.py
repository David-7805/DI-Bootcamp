# Exercise 1: Convert Lists Into Dictionaries
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
dict = {key: value for key, value in zip(keys, values)}
print(dict)

# Exercise 2: Cinemax
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

total_cost = 0
for name in family.keys():
  if family[name] < 3:
    cost = 0
  elif 3 <= family[name] < 12:
    cost = 10
  else:
    cost = 15
  print(f'{name.capitalize()} has to pay {cost} euro.')
  total_cost += cost
print(f'The total cost for the group is {total_cost}')

# Exercise 3: Zara
# 2.
brand = {
    'name': 'Zara',
    'creation_date': 1975,
    'creator_name': 'Amancio Ortega Gaona',
    'type_of_clothes': ['men', 'women', 'children', 'home'],
    'international_competitors': ['Gap', 'H&M', 'Benetton'],
    'number_stores': 7000,
    'major_color': {
        'France': 'blue',
        'Spain': 'red',
        'US': ('pink', 'green')
    }
}

# 3.
brand['number_stores'] = 2

# 4.
print(f"Zara's clients are people in search of {brand['type_of_clothes'][0]}, {brand['type_of_clothes'][1]}, {brand['type_of_clothes'][2]} or {brand['type_of_clothes'][3]} clothes.")

# 5.
brand['country_creation'] = "Spain"

# 6.
if 'international_competitors' in brand.keys():
  brand['international_competitors'].append('Desigual')

# 7.
brand.pop('creation_date')

# 8.
print(brand['international_competitors'][-1])

# 9.
print(brand['major_color']['US'])

# 10.
print(len(brand))

# 11.
for key in brand.keys():
  print(key)

# 12.
more_on_zara = {
    'creation_date': 1975,
    'number_stores': 10000
}

# 13.
brand.update(more_on_zara)

# 14.
print(brand['number_stores']) # The value belonging to the key 'number_stores', which was earlier set to 2, was updated with the new value of 10000

# Exercise 4: Disney Characters
users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

# 1.
disney_users_A = {key: value for value, key in enumerate(users)}
print(disney_users_A)

# 2.
disney_users_B = {key: value for key, value in enumerate(users)}
print(disney_users_B)

# 3.
users_alphabetical = users.copy()
users_alphabetical.sort()
disney_users_C = {key: value for value, key in enumerate(users_alphabetical)}
print(disney_users_C)

# 4.1.
disney_users_D = {key: value for value, key in enumerate(users) if 'i' in key or 'I' in key}
print(disney_users_D)

# 4.2.
users_names_capitalized = [] # I want it to work also if the names are not capitalized
for name in users:
  name = name.capitalize()
  users_names_capitalized.append(name)

disney_users_E = {key: value for value, key in enumerate(users) if key[0] == 'm'.upper() or key[0] == 'p'.upper()}
print(disney_users_E)