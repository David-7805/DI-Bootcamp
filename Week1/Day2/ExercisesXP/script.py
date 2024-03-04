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
for number in range(3, 11):
  half_of_number = number / 2
  if half_of_number == int(half_of_number):
    half_of_number = int(half_of_number)
  list_of_floats.append(half_of_number)
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

