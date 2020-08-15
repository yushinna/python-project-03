# Phrase Hunter
## Description
A word guessing game: "Phrase Hunter", created by using Python and OOP (Object-Oriented Programming) approaches to select a phrase at random, hidden from the player. A player tries to guess the phrase by inputting individual characters.

### Flow of the game
- Each time the player guesses a letter, the program compares the letter the player has chosen with the random phrase. If the letter is in the phrase, the phrase object is updated so that it displays the chosen letters on the screen.

- A player continues to select letters until they guess the phrase (and win), or make five incorrect guesses (and lose).

- If the player completes the phrase before they run out of guesses, a winning screen appears. If the player guesses incorrectly five times, a losing screen appears.

- A player can guess a letter only once. After they’ve guessed a letter, your programming logic will need to prevent that letter from being guessed a 2nd time.

## Usage
```
python app.py
```
