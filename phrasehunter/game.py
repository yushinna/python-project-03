import os
import re
import random
from .phrase import Phrase


with open('./phrasehunter/wordlist.txt') as f:
    data = f.read()
    word_list = data.strip().split(',')


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
        self.__word = random.choice(word_list)
        self.__phrases = Phrase(self.__word)
        self.__lives = 5

    def start(self):
        clear_screen()
        print("----------------------------------")
        print("Welcome to the Phrase Hunter Game!")
        print("----------------------------------")

        while not self.__phrases.all_guessed():
            print(*self.__phrases.show())
            print('\n----------------------------------\n')
            gss = input('Guess a letter: ').lower()

            try:
                if not re.match('[a-z]+', gss) or len(gss) != 1:
                    raise ValueError

                else:
                    guess_check = list(
                        map(lambda x: x.guess(gss), self.__phrases.phrase))

                    if any(guess_check):
                        print('\n----------------------------------\n')
                        print('your guess is correct!\n')

                        if self.__phrases.all_guessed():
                            print('\n----------------------------------\n')
                            print('You win!')
                            print('The answer is "{}"'.format(self.__word))
                            print('\n----------------------------------\n')
                            break

                    if not any(guess_check):
                        self.__lives -= 1
                        print('\n----------------------------------\n')
                        print('Yor guess is not correct..')
                        print('\nYou have {} out of 5 lives remaining!\n'.format(
                            self.__lives))

                        if self.__lives == 0:
                            print('\n----------------------------------\n')
                            print('You lose!')
                            print('The answer is "{}"'.format(self.__word))
                            print('\n----------------------------------\n')
                            break

            except ValueError:
                print('Please input a single character string! '
                      'Received: %s' % gss)
                input('\nPress ENTER to continue.. ')

    def restart(self):
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
