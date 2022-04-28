from colorama import Fore, Back
import random
from wordlefunctions import WordleF
def main():
    print("Type (instructions) if you want the rules ")
    solutionlist = (load_word_set("possible-solutions.txt"))
    guesslist = (load_word_set("possible-guess.txt"))
    hiddensolution = random.choice(solutionlist)
    wordle = WordleF(hiddensolution.upper())

    while wordle.can_attempt:
        x = input("Type your guess: ").upper()

        if x == "instructions":
            instructions(wordle)

        if len(x) != wordle.word_length:
            print(f"The guess should be {wordle.word_length} characters long")
            continue
        elif x not in guesslist:
            print(f"{x} is not a real word")
            continue

        wordle.attempt(x)
        display(wordle)
        displayletters(wordle)

        if wordle.solved:
            print("you win")
            break

    print(f"{hiddensolution} was the right answer")

def load_word_set(path: str):
    word_set = []
    with open(path, "r") as f:
        for line in f.readlines():
            word = line.strip().upper()
            word_set.append(word)
    return word_set

def display(wordle: WordleF):
    print("┌" + "━" * 13 + "┐")
    for word in wordle.attempts:
        result = wordle.guess(word)
        colored = colorcheck(result)
        print("├ " + colored + " ┤")
    for a in range(wordle.remaining_att):
        print("├ " + "_ " * wordle.word_length + "┤")
    print("└" + "━" * 13 + "┘")

def displayletters(wordle: WordleF):
    alphabet = "q w e r t y u i o p \n a s d f g h j k l \n  z x c v b n m".upper()
    for word in wordle.attempts:
        result = wordle.guess(word)
        for letter in range(wordle.word_length):
            color = Back.LIGHTBLACK_EX
            if word[letter] == "m":
                continue
            if letter > 0 and word[letter - 1] == word[letter]:
                continue
            if result[letter].is_in_pos:
                color = Back.GREEN + Fore.LIGHTWHITE_EX
            elif result[letter].is_in_word:
                color = Back.YELLOW + Fore.LIGHTWHITE_EX
            alphabet = alphabet.replace(word[letter], (color) + word[letter] + Fore.RESET)
    print(alphabet)

def colorcheck(result):
    res = []
    for letter in result:
        if letter.is_in_pos:
            color = Back.GREEN + Fore.LIGHTWHITE_EX
        elif letter.is_in_word:
            color = Back.YELLOW + Fore.LIGHTWHITE_EX
        else:
            color = Back.LIGHTBLACK_EX
        colored_letter = (color) + letter.character + Fore.RESET
        res.append(colored_letter)
    return " ".join(res)

def instructions(wordle: WordleF):
    print("The goal of the game is to guess the secret word")
    print( f"The guess needs to be about {wordle.word_length} characters long")
    print("If you get a letter in the right position, it will turn blue")
    print("If you get a letter in the word, it will turn yellow")
    print("Else, if the letter isnt in the word, the letter will turn black")



main()
