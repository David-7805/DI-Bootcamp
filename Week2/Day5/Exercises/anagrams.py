from anagram_checker import AnagramChecker

def show_menu():
    print('\n    MENU')
    print('(c) Check a word for its anagrams')
    print('(x) Exit')

def input_menu():
    is_in_menu = True
    while is_in_menu:
        show_menu()
        user_input = input('\n>>>: ')
        if user_input == 'x':
            is_in_menu = False
            print("Goodbye!")
        elif user_input == 'c':
            word_to_be_validated = word_receiver()
            if word_to_be_validated != 'Input not allowed.':
                anagram_checking_obj = AnagramChecker(r'C:\Users\pasha\PycharmProjects\DI-Bootcamp\Week2\Day5\Exercises\english_word_list.txt')
                if not anagram_checking_obj.is_valid_word(word_to_be_validated):
                    print("The word you entered is not in our dictionary.")
                else:
                    anagrams = anagram_checking_obj.get_anagrams(word_to_be_validated)
                    print(f'The anagrams of {word_to_be_validated}: {anagrams}')
        else:
            print("That's not a valid input. Please press 'c' or 'x'.")

def word_receiver():
    word_to_check = input('Please enter a word you would like to know the anagrams of: ')
    word_to_check = word_to_check.strip(' ')
    if len(word_to_check.split(' ')) > 1:
        print('ERROR: you entered more than one word.')
        return 'Input not allowed.'
    elif not word_to_check.isalpha():
        print('ERROR: you entered (at least) one character that is not in the alphabet.')
        return 'Input not allowed.'
    else:
        return word_to_check

input_menu()
