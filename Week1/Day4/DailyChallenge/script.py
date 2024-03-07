matrix_string = '7iiTsxh%?i #sM $a #t%^r!'

def from_string_to_grid(string, grid_width):
  list_of_substrings = []
  number_of_substrings = (len(string) // grid_width) + 1 # If len(string) == 16 and grid_width == 5, I need 4 (3 + 1) substrings
  for iteration in range(number_of_substrings):
    substring = string[iteration * grid_width: (iteration + 1) * grid_width]
    if substring != '':
      if len(substring) == grid_width:
        list_of_substrings.append(substring)
      else:
        substring += '_' * (grid_width - len(substring)) # I need to add characters to the latest substring if its length < grid_width to prevent an index error in the function vertical_reader
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
    vertical_string = vertical_reader(grid, position)
    if vertical_string[-1] == '_':
      result += vertical_string[:-1] # Here I remove the earlier added '_' characters. The problem that I haven't solved, involves cases when a naturally occurring '_' happens to be at this latest position of vertical_string.
    else:
      result += vertical_string
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

def secret_message_finder(string, grid_width):
  grid = from_string_to_grid(string, grid_width)
  possible_message = combiner_of_vertical_strings(grid)
  only_alpha_characters(possible_message)

secret_message_finder(matrix_string, 2)
secret_message_finder(matrix_string, 3) # Prints an understandable message
secret_message_finder(matrix_string, 4)
secret_message_finder(matrix_string, 5)
secret_message_finder(matrix_string, 6)
secret_message_finder(matrix_string, 7)
secret_message_finder(matrix_string, 8)
secret_message_finder(matrix_string, 9)
secret_message_finder(matrix_string, 10)
secret_message_finder(matrix_string, 11)
secret_message_finder(matrix_string, 12)
