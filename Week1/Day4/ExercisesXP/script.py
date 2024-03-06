# Exercise 1: What Are You Learning ?
def display_message(course_name):
    print(f'I am learning {course_name} in this course.')

display_message('Data Analytics')

# Exercise 2: What’s Your Favorite Book ?
def favorite_book(title):
  print(f'One of my favorite books is {title}.')

favorite_book('The Diary of a Young Girl')

# Exercise 3: Some Geography
def describe_city(city_name, country_name = 'India'):
  print(f'{city_name} is in {country_name}.')

describe_city('Tel Aviv', 'Israel')
describe_city('Mumbai')

# Exercise 4: Random
import random
def is_equal_to_random_number(number):
  if number not in list(range(1, 101)):
    print("You can only pass an integer from 1 to 100 to this function.")
  else:
    random_number = random.randint(1, 100) # The randint method includes both end points.
    if number == random_number:
      print(f"Congrats! You correctly predicted the random number {random_number}!")
    else:
      print(f"Unfortunately your number {number} is not the same as the random number {random_number}.")

is_equal_to_random_number('Python')
is_equal_to_random_number(0)
is_equal_to_random_number(101)
is_equal_to_random_number(28)

# Exercise 5: Let’s Create Some Personalized Shirts !
# 1. 2.
def make_shirt(size, message):
  print(f"The size of the shirt is '{size}' and the text is '{message}'.")

# 3.
make_shirt('L', 'Humanist')

# 4.
def make_shirt_2(size = 'L', message = 'I love Python'):
  print(f"The size of the shirt is '{size}' and the text is '{message}'.")

# 5.
make_shirt_2()

# 6.
make_shirt_2('M')

# 7.
make_shirt_2('S', 'Humanist')

# 8.
shirt_instructions = {'size': 'XL', 'message': 'Peace'}
make_shirt_2(**shirt_instructions)

# Exercise 6: Magicians …
magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magicians(list_of_magicians):
  for magician in list_of_magicians:
    print(magician)

def make_great(list_of_people):
  for member in range(len(list_of_people)):
    list_of_people[member] += " the Great"

make_great(magician_names)
show_magicians(magician_names)

# Exercise 7: Temperature Advice
# 1.1
def get_random_temp():
  random_temperature = random.randint(-10, 40)
  return random_temperature

# 1.2.
temperature_list = []
for i in range(1000):
  generated_temperature = get_random_temp()
  temperature_list.append(generated_temperature)
  temperature_list.sort()
print(temperature_list[0], temperature_list[-1]) # All 1000 generated temperatures are between -10 and 40

# 2.
def main():
  current_temperature = get_random_temp()
  print(f'The temperature right now is {current_temperature} degrees Celsius.')

# 3.
def main_2():
  current_temperature = get_random_temp()
  print(f'The temperature right now is {current_temperature} degrees celsius.')
  if current_temperature < 0:
    print('Brrr, that’s freezing! Wear some extra layers today!')
  elif current_temperature < 16:
    print('Quite chilly! Don’t forget your coat')
  elif current_temperature < 23:
    print("That's a pleasant temperature. Enjoy the weather!")
  elif current_temperature < 32:
    print("It's getting warm. Choose thin clothing today")
  elif current_temperature <= 40:
    print("It's very hot today. Choose thin clothing and make sure you drink enough.")

# 4.
def get_random_temp_2(season):
  if season.lower() == 'winter':
    random_temperature = random.randint(-10, 16)
  elif season.lower() == 'summer':
    random_temperature = random.randint(28, 40)
  elif season.lower() == 'autumn' or season.lower() == 'fall':
    random_temperature = random.randint(17, 27)
  else:
    return "Invalid season"
  return random_temperature

def main_3():
  season = input("Please enter the season: ")
  current_temperature = get_random_temp_2(season)
  while current_temperature == 'Invalid season':
    season = input("Season not recognised. Please enter the season: ")
    current_temperature = get_random_temp_2(season)
  print(f'The temperature right now is {current_temperature} degrees celsius.')
  if current_temperature < 0:
    print('Brrr, that’s freezing! Wear some extra layers today!')
  elif current_temperature < 16:
    print('Quite chilly! Don’t forget your coat')
  elif current_temperature < 23:
    print("That's a pleasant temperature. Enjoy the weather!")
  elif current_temperature < 32:
    print("It's getting warm. Choose thin clothing today")
  elif current_temperature <= 40:
    print("It's very hot today. Choose thin clothing and make sure you drink enough.")

main_3()
