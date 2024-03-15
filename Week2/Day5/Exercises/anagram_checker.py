from itertools import permutations

class AnagramChecker:

    def __init__(self, existing_words_file):
        with open(existing_words_file, 'r') as existing_words:
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
            sorted_character_list_1 = sorted(word_1)
            sorted_character_list_2 = sorted(word_2)
            if sorted_character_list_1 == sorted_character_list_2:
                return True
            else:
                return False

    def is_valid_word(self, word):
        return (word.lower() in self.existing_words)

    def get_anagrams(self, word):
        anagrams = [existing_word for existing_word in self.existing_words if len(existing_word) == len(word) and AnagramChecker.is_anagram(existing_word, word)]
        # My previous method with permutations (see below) took extremely long to get anagrams for words with length 8,
        # because it creates a list of 8*7*6*5*4*3*2*1 (= 40320) items to be created and checked.
        # potential_anagrams = ["".join(permutation) for permutation in permutations(word.lower())]
        # anagrams = [potential_anagram for potential_anagram in potential_anagrams if potential_anagram in self.existing_words and potential_anagram != word.lower()]
        return anagrams

