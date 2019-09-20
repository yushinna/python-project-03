import random
from .character import Character
from .phrase import Phrase


def set_phrase():
    with open('./phrasehunter/wordlist.txt') as f:
        data = f.read()
        word_list = data.strip().split(',')
        word = random.choice(word_list)
        char_list = []

        for char in word:
            char_list.append(Character(char))

        return Phrase(char_list)


def restart():
    while True:
        try:
            replay = input('Do you want to play again? [y]es or [n]o: ')

            if replay.lower() == 'n' or replay.lower() == 'no':
                print('\nThank you! See you next time!\n')
                return False

            if replay.lower() == 'y' or replay.lower() == 'yes':
                return True

            else:
                raise ValueError

        except ValueError:
            print('\nThat was no valid input! Try again..\n')
