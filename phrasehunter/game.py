import os
import random
import re
from .phrase import Phrase
from .character import Character


PHRASES = ['hello']


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


class Game:
    """
    The Game instance is responsible for starting the game loop, getting player's
    input() guesses to pass to a Phrase object to perform its responsibilities against,
    determining if a win/loss happens after the player runs out of turns
    or the phrase is completely guessed.
    """
    def __init__(self):
        self.__char_list = []

        for char in random.choice(PHRASES):
            self.__char_list.append(Character(char))

        self.__phrases = Phrase(self.__char_list)
        self.__lives = 5

    def start(self):
        while not self.__phrases.all_guessed():
            print('\n- - - - -\n')
            gss = input('Guess a letter: ')

            try:
                if not re.match('[a-z]+', gss) or len(gss) != 1:
                    raise ValueError

                else:
                    guess_check = list(map(lambda x: x.guess(gss), self.__phrases.phrase))

                    if any(guess_check):
                        print('\n- - - - -\n')
                        print('your guess is correct!')
                        print(self.__phrases.show())

                        if self.__phrases.all_guessed():
                            print('\n- - - - -\n')
                            print('You win! Have a nice day!')
                            print('\n- - - - -\n')
                            break

                    if not any(guess_check):
                        self.__lives -= 1
                        print('\n- - - - -\n')
                        print('Yor guess is not correct..')
                        print(self.__phrases.show())
                        print('You have {} out of 5 lives remaining!'.format(self.__lives))

                        if self.__lives == 0:
                            print('\n- - - - -\n')
                            print('You lose! See you next time!')
                            print('\n- - - - -\n')
                            break

            except ValueError:
                print('Please input a single lowercase character string! '
                      'Received: %s' % gss)
                input('\nPress ENTER to continue.. ')

    @staticmethod
    def welcome():
        clear_screen()
        print("----------------------------------")
        print("Welcome to the Phrase Hunter Game!")
        print("----------------------------------")
