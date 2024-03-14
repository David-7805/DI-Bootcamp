from itertools import permutations

class AnagramChecker:

    def __init__(self, existing_words_file):
        with open (existing_words_file, 'r') as existing_words:
            list_of_existing_words = existing_words.readlines()
            for index in range(len(list_of_existing_words)):
                list_of_existing_words[index] = list_of_existing_words[index].lower().strip('\n')
        self.existing_words = list_of_existing_words

    @staticmethod
    def is_anagram(word_1, word_2):
        word_1 = word_1.lower()
        word_2 = word_2.lower()
        if word_1 == word_2:
            return False
        else:
            character_list_1 = list(word_1)
            character_list_2 = list(word_2)
            character_list_1.sort()
            character_list_2.sort()
            if character_list_1 == character_list_2:
                return True
            else:
                return False

    def is_valid_word(self, word):
        return (word.lower() in self.existing_words)

    def get_anagrams(self, word):
        anagrams = [existing_word for existing_word in self.existing_words if len(existing_word) == len(word) and AnagramChecker.is_anagram(existing_word, word)]
        # potential_anagrams = ["".join(permutation) for permutation in permutations(word.lower())]
        # anagrams = [potential_anagram for potential_anagram in potential_anagrams if potential_anagram in self.existing_words and potential_anagram != word.lower()]
        return anagrams








# test_var = AnagramChecker(r'C:\Users\pasha\PycharmProjects\DI-Bootcamp\Week2\Day5\Exercises\english_word_list.txt')
# print(test_var.is_valid_word('META'))
# print(test_var.is_valid_word('meta'))
# print(AnagramChecker.is_anagram('MEAT', 'mate'))
# print(test_var.get_anagrams('Meta'))
