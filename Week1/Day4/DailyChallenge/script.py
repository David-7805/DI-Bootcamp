test_string = '7iiTsxh%?i #sM $a #t%^r!'

def from_string_to_grid(string, grid_width):
  list_of_substrings = []
  number_of_substrings = (len(string) // grid_width) + 1 # If len(string) == 16 and grid_width == 5, I need 4 (3 + 1) substrings
  for iteration in range(number_of_substrings):
    substring = string[iteration * grid_width: (iteration + 1) * grid_width]
    if substring != '':
      list_of_substrings.append(substring)
  return list_of_substrings

def vertical_reader(grid, index):
  vertical_string = ''
  for substring in grid:
    vertical_string += substring[index]
  return vertical_string

def combiner_of_vertical_strings(grid):
  result = ''
  substring_length = len(grid[0])
  for position in range(substring_length):
    result += vertical_reader(grid, position)
  return result

def only_alpha_characters(string):
  new_string = ''
  for character in string:
    if 65 <= ord(character) <= 91 or 97 <= ord(character) <= 123:
      new_string += character
    else:
      new_string += ' '
  list_of_the_words = new_string.split()
  string_to_output = ' '.join(list_of_the_words)
  print(string_to_output)
  return string_to_output

grid = from_string_to_grid(test_string, 3)
possible_message = combiner_of_vertical_strings(grid)
only_alpha_characters(possible_message)
