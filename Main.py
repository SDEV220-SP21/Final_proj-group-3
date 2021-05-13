import Christian_Drake
import wordChoice

wordChoice.fileOpen()
wordChoice.getword()
#print(wordChoice.chosen_Word)
Christian_Drake.playerInput(0, wordChoice.hidden_Word, wordChoice.chosen_Word)
while Christian_Drake.hidden_Word2 != wordChoice.chosen_Word:
    print("Miss Count: " + str(Christian_Drake.miss_Count))
    if Christian_Drake.miss_Count < 7:
        

        print(Christian_Drake.hidden_Word2)
    
        Christian_Drake.playerInput(Christian_Drake.miss_Count, Christian_Drake.hidden_Word2, wordChoice.chosen_Word)
        
    else:
        print("Ahaha you lost")
        Christian_Drake.hidden_Word2 = wordChoice.chosen_Word
    
    


