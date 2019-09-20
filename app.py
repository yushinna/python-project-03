from phrasehunter import (
    game, set_phrase, restart
)


if __name__ == '__main__':
    while True:
        phrase = set_phrase()
        play = game.Game(phrase)
        play.start()
        if not restart():
            break
