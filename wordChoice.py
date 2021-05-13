import random
import re
def fileOpen():
    global hidden_Word
    global chosen_Word
    # open the file with words
    with open("wordList.txt") as word:
        wordList = word.read().splitlines()

    # Pick a random word from the list
    number = random.randint(0, len(wordList)-1)
    chosenWord = wordList[number]

    # Encode the word with dashes
    hiddenWord = re.sub('[0-9a-zA-Z]', '*', chosenWord)
    hidden_Word = hiddenWord
    chosen_Word = chosenWord
    print(hidden_Word)

    #//print(chosenWord)
    #// print(hiddenWord)
def getword():
    return hidden_Word
    return chosen_Word
