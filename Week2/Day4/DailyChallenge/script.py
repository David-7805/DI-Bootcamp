import string

class Text:
    def __init__(self, string):
        self.original_text = string
        self.dict_of_frequencies = self.frequencies()

    def frequencies(self):
        words_list_to_process = self.original_text.lower().split(' ')
        punctuation_marks = string.punctuation
        dict_of_frequencies = {}
        for index in range(len(words_list_to_process)):
            words_list_to_process[index] = words_list_to_process[index].strip(punctuation_marks).strip('\n')
        for word in words_list_to_process:
            dict_of_frequencies[word] = words_list_to_process.count(word)
        return dict_of_frequencies

    def word_frequency(self, word):
        if word in self.dict_of_frequencies:
            return self.dict_of_frequencies[word]
        else:
            return f'The word {word} does not occur in the text'

    def most_common_word(self):
        highest_frequency = 0
        most_frequent_word = []
        for word, frequency in self.dict_of_frequencies.items():
            if frequency == highest_frequency:
                most_frequent_word.append(word)
            elif frequency > highest_frequency:
                most_frequent_word = [word]
                highest_frequency = frequency
        return most_frequent_word

    def unique_words(self):
        unique_words = []
        for word, frequency in self.dict_of_frequencies.items():
            if frequency == 1:
                unique_words.append(word)
        return unique_words

    @classmethod
    def from_file(cls, filename):
        with open(filename) as text:
            string_of_text = text.read()
            return Text(string_of_text)


the_stranger = Text.from_file(r'C:\Users\pasha\PycharmProjects\DI-Bootcamp\Week2\Day4\DailyChallenge\the_stranger.txt')

print(the_stranger.word_frequency('stranger'))
print(the_stranger.most_common_word())
print(the_stranger.unique_words())