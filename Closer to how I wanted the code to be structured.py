from tkinter import *
# This is more or less how I wanted to write the program, a class that handles the GUI and
#has a number of missed guesses attribute (guesses)
class Shapes:
    
    def __init__(self, guesses):
        window = Tk()
        window.title("Hangman 2: house edition")
        self.width = 1000
        self.height = 500
        self.guesses = 0
        self.letterGuess = ""
        frame2 = Frame(window)
        frame2.pack()
        self.canvas = Canvas(frame2, width=self.width, height=self.height, bg='white')
        self.canvas.pack()
        
        frame1 = Frame(window)
        frame1.pack()
        btnGuess = Button(frame1, text = "Guess", command = self.processButtons)
        letterEntry = Entry(frame2, width = 20, textvariable = self.letterGuess)
        
        btnGuess.grid(row = 1, column = 2)
        letterEntry.grid(row = 1, column = 1)

        window.mainloop()
    def getGuesses(self):
        return self.guesses
    def setGetGuesses(self):
        self.guesses = guesses
        
        
        
    def processButtons(self):
        
        color = 'grey'
        self.clear()
        #in the real program guesses would only increment by 1 here if the letter guessed
        #was not in the word
        self.guesses += 1

        if self.guesses.get() == 1:
            self.canvas.create_line(250, 400, 750, 400 , tags = "base")
        if self.guesses.get() == 2:
            self.canvas.create_line(250, 400, 250, 225 , tags = "leftSide")
        if self.guesses.get() == 3:
            self.canvas.create_line(750, 225, 750, 400 , tags = "rightSide")
        if self.guesses.get() == 4:
            self.canvas.create_line(150, 225, 850, 225 , tags = "top")
        if self.guesses.get() == 5:
            self.canvas.create_line(150, 225, 500, 20 , tags = "leftRoof")
        if self.guesses.get() == 6:
            self.canvas.create_line(500, 20, 850, 225 , tags = "rightRoof")
        if self.guesses.get() == 7:
            self.canvas.create_rectangle(450, 400, 550, 250 , tags = "door")
            self.canvas.create_oval(520, 330, 535, 345, tags = "doorKnob")
            self.canvas.create_rectangle(290, 330, 375, 250, tags = "leftWindow")
            self.canvas.create_rectangle(710, 330, 625, 250, tags = "RightWindow")
            self.canvas.create_line(332, 330, 332, 250 , tags = "rightRoof")
            self.canvas.create_line(290, 290, 375, 290 , tags = "rightRoof")
            self.canvas.create_line(667, 330, 667, 250 , tags = "rightRoof")
            self.canvas.create_line(625, 290, 710, 290 , tags = "rightRoof")
    def clear(self):
        self.canvas.delete('polygon')

        


Shapes(0)
        
