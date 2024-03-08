# Challenge 1: Sorting
def string_sorter(unsorted_string, delimiter):
  help_list = unsorted_string.split(delimiter)
  help_list.sort()
  sorted_string = delimiter.join(help_list)
  return sorted_string

input_string = 'without,hello,bag,world'
print(string_sorter(input_string, ','))

# Challenge 2: Longest Word
def longest_word_finder(sentence):
  help_list = sentence.split(' ')
  longest_word = ''
  for word in help_list:
    if len(word) > len(longest_word):
      longest_word = word
  return longest_word

print(longest_word_finder("Margaret's toy is a pretty doll."))
print(longest_word_finder("A thing of beauty is a joy forever."))
print(longest_word_finder("Forgetfulness is by all means powerless!"))