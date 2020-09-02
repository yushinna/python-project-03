from phrasehunter import game


if __name__ == '__main__':
    while True:
        play = game.Game()
        play.start()
        if not play.restart():
            break
