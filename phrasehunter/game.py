import os
import re
from .phrase import Phrase


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


class Game:
    """
    The Game instance is responsible for starting the game loop, getting player's
    input() guesses to pass to a Phrase object to perform its responsibilities against,
    determining if a win/loss happens after the player runs out of turns
    or the phrase is completely guessed.
    """

    def __init__(self, phrases: Phrase):
        self.__phrases = phrases
        self.__word = ''.join(self.__phrases.original())
        self.__lives = 5

    def start(self):
        clear_screen()
        print("----------------------------------")
        print("Welcome to the Phrase Hunter Game!")
        print("----------------------------------")

        while not self.__phrases.all_guessed():
            print('\n----------------------------------\n')
            gss = input('Guess a letter: ')

            try:
                if not re.match('[a-z]+', gss) or len(gss) != 1:
                    raise ValueError

                else:
                    guess_check = list(
                        map(lambda x: x.guess(gss), self.__phrases.phrase))

                    if any(guess_check):
                        print('\n----------------------------------\n')
                        print('your guess is correct!\n')
                        print(*self.__phrases.show())

                        if self.__phrases.all_guessed():
                            print('\n----------------------------------\n')
                            print('You win!')
                            print('The answer is "{}"'.format(self.__word))
                            print('\n----------------------------------\n')
                            break

                    if not any(guess_check):
                        self.__lives -= 1
                        print('\n----------------------------------\n')
                        print('Yor guess is not correct..\n')
                        print(*self.__phrases.show())
                        print('\nYou have {} out of 5 lives remaining!'.format(
                            self.__lives))

                        if self.__lives == 0:
                            print('\n----------------------------------\n')
                            print('You lose!')
                            print('The answer is "{}"'.format(self.__word))
                            print('\n----------------------------------\n')
                            break

            except ValueError:
                print('Please input a single lowercase character string! '
                      'Received: %s' % gss)
                input('\nPress ENTER to continue.. ')
