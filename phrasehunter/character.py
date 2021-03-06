class Character:
    """
    The Character instance is responsible for holding the state of a given single character.
    """

    def __init__(self, char: str):
        self.original = char
        self.was_guessed = False

    def guess(self, gss: str) -> None or bool:
        if self.was_guessed:
            return None

        elif not self.was_guessed and gss == self.original:
            self.was_guessed = True
            return True

        else:
            return False

    def show(self) -> str:
        if self.was_guessed:
            return self.original
        else:
            return '_'
