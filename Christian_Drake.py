import wordChoice

#random word choice
#def RandomWord
#import file as reading
#check line amount on file
# grab line (randomint 0 - lines - 1)
# check length of line
#turn word into list for later use
# ^ no longer my part. kept for reference later incase i come back to this code later.  ^

def playerInput(missCount, hiddenWord, chosenWord):
    global miss_Count
    global hidden_Word2
    shWord = list(hiddenWord)
    scWord = list(chosenWord)
    #print(scWord)
    #print(shWord)
    #print(chosenWord)
    inChar = input("Input a single letter:   ")
    if inChar in scWord:
        count = 0
        while count < len(hiddenWord):
            if inChar == scWord[count]:
                shWord[count] = inChar
            count += 1
    else:
        missCount += 1
    #print(shWord)
    hiddenWord = "".join(shWord)
    hidden_Word2 = hiddenWord
    miss_Count = missCount
#player input / misscheck
#get input
#check if not number
#if number repeat else:
# check if in Chosen_word
#  words  = list(string)
# while count < wordlength
# if input == words[count]
#  correct = 1,  reveal = count
#if correct = 0, miss += 1


