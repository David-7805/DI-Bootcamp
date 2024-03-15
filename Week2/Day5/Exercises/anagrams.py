from anagram_checker import AnagramChecker

def show_menu():
    print('\n    MENU')
    print('(c) Check a word for its anagrams')
    print('(x) Exit')

def anagram_finder():
    program_is_running = True
    while program_is_running:
        show_menu()
        user_input = input('\n>>>: ')
        if user_input == 'x':
            program_is_running = False
            print("Goodbye!")
        elif user_input == 'c':
            word_to_be_checked = user_word()
            if word_to_be_checked != 'Input not allowed.':
                anagram_checker = AnagramChecker(r'C:\Users\pasha\PycharmProjects\DI-Bootcamp\Week2\Day5\Exercises\english_word_list.txt')
                if not anagram_checker.is_valid_word(word_to_be_checked):
                    print("The word you entered is not in our dictionary.")
                else:
                    anagrams = anagram_checker.get_anagrams(word_to_be_checked)
                    print_result(word_to_be_checked, anagrams)
        else:
            print("That's not a valid input. Please press 'c' or 'x'.")

def user_word():
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

def print_result(word, anagram_list):
    print(f'\nYOUR WORD: "{word.upper()}"')
    print('This is a valid English word.')
    if anagram_list == []:
        print('Your word does not have any anagrams.')
    else:
        print(f'The anagrams of your word: ', end = '')
        for anagram in anagram_list[: -1]:
            print(f'{anagram}, ', end = '')
        for anagram in anagram_list[-1 :]:
            print(f'{anagram}.')


anagram_finder()
