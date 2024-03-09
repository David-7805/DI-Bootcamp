# Challenge 1: Sorting
def string_sorter(original_string, delimiter):
  list_original = original_string.split(delimiter)
  list_lowercase = [word.lower() for word in list_original] # I want words containing capital letters to be sorted appropriately
  lowercase_and_original_zipped = zip(list_lowercase, list_original) # But I don't want to lose the original words
  dictionary_lowercase_to_original = {lowercase: original for lowercase, original in lowercase_and_original_zipped}
  list_lowercase.sort()
  list_original_sorted = [dictionary_lowercase_to_original[lowercase_word] for lowercase_word in list_lowercase]
  sorted_string = delimiter.join(list_original_sorted)
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
