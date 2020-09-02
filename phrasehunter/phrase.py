from .character import Character


class Phrase:
    """
    Phrase instance is to handle the creation of phrases
    """

    def __init__(self, word: str):
        """
        phrase: string
        """
        self.phrase = [Character(letter) for letter in word]

    def all_guessed(self) -> bool:
        if all(list(map(lambda x: x.was_guessed, self.phrase))):
            return True
        else:
            return False

    def show(self) -> list:
        return list(map(lambda x: x.show(), self.phrase))
