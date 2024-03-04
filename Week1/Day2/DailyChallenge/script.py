# Challenge 1
inputted_number = int(input('Please give a number: '))
length = int(input('Please give a length: '))

list_of_multiples = []
for number in range(length):
  list_of_multiples.append(inputted_number * (number + 1))
print(list_of_multiples)

# Challenge 2
inputted_string = input("Please enter a word: ")

new_string = inputted_string[0]
for position in range(len(inputted_string)):
  if position == 0:
    continue
  elif inputted_string[position] != new_string[-1]:
    new_string += inputted_string[position]
print(new_string)