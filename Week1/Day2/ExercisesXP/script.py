# Exercise 1
my_fav_numbers = {7, 14, 28}
my_fav_numbers.add(56)
my_fav_numbers.add(84)
print(my_fav_numbers)

my_fav_numbers.discard(84)
print(my_fav_numbers)

friend_fav_numbers = {5, 9, 78, 81}
our_fav_numbers = friend_fav_numbers
for number in my_fav_numbers:
  our_fav_numbers.add(number)
print(our_fav_numbers)

# Exercise 2
# Answer: A tuple is immutable, so it is not possible to add or remove anything.

# Exercise 3
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0, "Apples")
number_of_apple_trays = basket.count("Apples")
basket.clear()
print(basket)

# Exercise 4
# 1. A float is a number that contains decimals
# 2.
list_of_floats = []
for integer in range(3, 11):
  half_of_integer = integer / 2
  if half_of_integer == int(half_of_integer):
    half_of_integer = int(half_of_integer)
  list_of_floats.append(half_of_integer)
print(list_of_floats)

# 3.
list_of_floats_2 = []
number = 1
while number <= 4.5:
  number += 0.5
  if number == int(number):
    number = int(number)
  list_of_floats_2.append(number)
print(list_of_floats_2)

# Exercise 5
# 1.
for number in range(20):
  print(number + 1)

# 2.
for number in range(20):
  if (number + 1) % 2 == 0:
    print(number + 1)

# Exercise 6
my_name = "David"
username = "Whatever"
while username != my_name:
  username = input("Please enter your name starting with a capital letter: ")

# Exercise 7
favorite_fruits = input("Please enter your favorite fruits separated with a single space: ")
favorite_fruits = favorite_fruits.lower()
list_of_favorite_fruits = favorite_fruits.split(' ')
any_fruit = input("Please enter the name of any fruit: ")
if any_fruit.lower() in list_of_favorite_fruits:
  print("You chose one of your favorite fruits")
else:
  print("You chose a new fruit. I hope you enjoy.")

# Exercise 8
pizza_toppings = []
while True:
  pizza_topping = input("Please enter the pizza topping you wanna add or 'quit' to move on with your order: ")
  if pizza_topping == 'quit':
    break
  else:
    print(f"We'll add {pizza_topping} to your pizza.")
    pizza_toppings.append(pizza_topping)
total_price = 10 + 2.5 * len(pizza_toppings)
print(f"You'll get {pizza_toppings} for a total price of {total_price} euro.")

# Exercise 9
# 1. 2. 3.
family = []
total_cost = 0
while True:
  age = input("Please enter the age of the next person who wants to watch the movie or 'quit': ")
  if age == 'quit':
    break
  else:
    family.append(int(age))
for member in family:
  if 3 <= member < 12:
    total_cost += 10
  elif member >= 12:
    total_cost += 15
print(f'Your total cost is {total_cost} euro.')

# 4.
names = ["David", "Marija", "Manon"]
def age_checker(list_of_names):
  names_for_removal = []
  for person in list_of_names:
    age = input(f'Dear {person}, please enter your age: ')
    if int(age) < 21: # Assuming that if restricted for 16 to 21 it is also restricted for under 16
      names_for_removal.append(person)
  for person in names_for_removal:
    names.remove(person)
  print(list_of_names)

age_checker(names)

# Exercise 10
sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]

order_number = 0
while order_number < len(sandwich_orders):
  if "Pastrami" in sandwich_orders[order_number]:
    sandwich_orders.remove(sandwich_orders[order_number]) # after removing it is not necessary to add 1 to order_number
  else:
    order_number += 1
print(sandwich_orders)

finished_sandwiches = []
while len(sandwich_orders) > 0:
   sandwich_in_preparation = sandwich_orders.pop(0)
   finished_sandwich = sandwich_in_preparation.lower()
   finished_sandwiches.append(finished_sandwich)

for sandwich in finished_sandwiches:
  print(f'I made you a {sandwich}')