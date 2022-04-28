from letterchecker import LetterChecker

class WordleF:
    max_attempts = 6
    word_length = 5
    def __init__(self, secret):
        self.secret: str = secret
        self.attempts = []
        pass
    def attempt(self, word: str):
        word = word.upper()
        self.attempts.append(word)
    def guess(self, word: str):
        word = word.upper()
        result = []
        temp = self.secret
        for i in range(self.word_length):
            character = word[i]
            letter = LetterChecker(character)
            letter.is_in_pos = character == temp[i]
            letter.is_in_word = character in temp
            if letter.is_in_pos:
                temp = temp.replace(character, "?", 1)
                result.insert(i, letter)
            elif letter.is_in_word:
                temp = temp.replace(character, "?", 1)
                result.insert(i, letter)
            else:
                result.insert(i, letter)
        return result


    @property
    def can_attempt(self):
        return self.remaining_att > 0 and not self.solved
    @property
    def remaining_att(self) -> int:
        return self.max_attempts - len(self.attempts)
    @property
    def solved(self):
        return len(self.attempts) > 0 and self.attempts[-1] == self.secret
