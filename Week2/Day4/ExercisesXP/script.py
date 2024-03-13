from random import choices
import json

# Exercise 1 – Random Sentence Generator
def get_words_from_file(filename):
    with open(filename, 'r') as words:
        list_of_words = words.readlines()
        for index in range(len(list_of_words)):
            list_of_words[index] = list_of_words[index].strip('\n')
        tuple_of_words = tuple(list_of_words)
        return tuple_of_words


def get_random_sentence(length):
    tuple_of_words = get_words_from_file(r'C:\Users\pasha\PycharmProjects\DI-Bootcamp\Week2\Day4\ExercisesXP\word_list.txt')
    random_words = choices(tuple_of_words, k = length)
    for index in range(len(random_words)):
        random_words[index] = random_words[index].lower()
    random_sentence = ' '.join(random_words)
    print(random_sentence)

def main():
    print("This program makes random sentences of between 2 to 20 words and you can choose how many exactly.")
    number_of_words = input('Please choose amount of words (between 2 and 20): ')
    try:
        sentence_length = int(number_of_words)
        if sentence_length < 2 or sentence_length > 20:
            raise Exception('Number of words should have been between 2 and 20!')
        else:
            get_random_sentence(sentence_length)
    except ValueError:
        print("Error: you didn't enter an integer!")

main()

# Exercise 2: Working With JSON
sampleJson = """{
   "company":{
      "employee":{
         "name":"emma",
         "payable":{
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

my_company = json.loads(sampleJson)
print(my_company['company']['employee']['payable']['salary'])
my_company['company']['employee']['birth_date'] = '1978-05-14'

json_file = 'my_company.json'
with open(json_file, 'w') as file_object:
    json.dump(my_company, file_object, indent = 2, sort_keys = True)