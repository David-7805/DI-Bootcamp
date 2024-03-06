test_string = '7iiTsxh%?i #sM $a #t%^r!'

def from_string_to_grid(string, grid_width):
  list_of_substrings = []
  number_of_substrings = (len(string) // grid_width) + 1 # If len(string) == 16 and grid_width == 5, I need 4 (3 + 1) substrings
  for iteration in range(number_of_substrings):
    substring = string[iteration * grid_width: (iteration + 1) * grid_width]
    if substring != '':
      list_of_substrings.append(substring)
  print(list_of_substrings)

from_string_to_grid(test_string, 3)

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
  print(result)

combiner_of_vertical_strings(['7ii', 'Tsx', 'h%?', 'i #', 'sM ', '$a ', '#t%', '^r!'])
# vertical_reader(['7ii', 'Tsx', 'h%?', 'i #', 'sM ', '$a ', '#t%', '^r!'], 0)

