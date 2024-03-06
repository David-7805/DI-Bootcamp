# Challenge 1
def place_in_word_of_letters(word):
  character_occurrences = {}
  for position in range(len(word)):
    if word[position] not in character_occurrences.keys():
      character_occurrences[word[position]] = [position]
    else:
      character_occurrences[word[position]].append(position)
  print(character_occurrences)

place_in_word_of_letters("dodo")
place_in_word_of_letters("froggy")
place_in_word_of_letters("grapes")

# Challenge 2
def string_to_number(price_string):
  price = ''
  for char in price_string:
    if char == '$' or char == ',':
      continue
    else:
      price += char
  amount = int(price)
  return amount

def shop_calculator(product_range, budget):
  budget = string_to_number(budget)
  chosen_items = []
  for product in list(product_range.items()):
    if string_to_number(product[1]) < budget:
      chosen_items.append(product[0])
      budget -= string_to_number(product[1])
  chosen_items.sort()
  print(chosen_items) if len(chosen_items) > 0 else print('Nothing')


shop_calculator({
  "Water": "$1",
  "Bread": "$3",
  "TV": "$1,000",
  "Fertilizer": "$20"
}, "$300")

shop_calculator({
  "Apple": "$4",
  "Honey": "$3",
  "Fan": "$14",
  "Bananas": "$4",
  "Pan": "$100",
  "Spoon": "$2"
}, "$100")

shop_calculator({
  "Phone": "$999",
  "Speakers": "$300",
  "Laptop": "$5,000",
  "PC": "$1200"
}, "$1")
