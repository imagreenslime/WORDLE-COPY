class LetterChecker:
    def __init__(self, character: str):
        self.is_in_word: bool = False
        self.is_in_pos: bool = False
        self.character: str = character
    def __repr__(self):
        return "('{}', {}, {})".format(self.character, self.is_in_pos, self.is_in_word)
