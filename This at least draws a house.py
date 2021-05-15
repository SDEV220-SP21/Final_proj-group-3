
# Because I was having trouble getting the Code to work, I wrote this program
#simply to have a template for drawing the house in canvas. You just check the
#radiobuttons 1 through 7 and it will draw the house

from tkinter import *
class HangmanGUI:
    
    def __init__(self):
        window = Tk()
        window.title("Hangman 2: House Edition")
        self.width = 1000
        self.height = 500

        frame2 = Frame(window)
        frame2.pack()
        self.canvas = Canvas(frame2, width=self.width, height=self.height, bg='white')
        self.canvas.pack()
        
        frame1 = Frame(window)
        frame1.pack()
        self.guesses = IntVar()
        
        
        rbgus1 = Radiobutton(frame1, text = "Guess 1",
                                variable = self.guesses, value =1,
                                command = self.processButtons)
        rbgus2 = Radiobutton(frame1, text = "Guess 2",
                                variable = self.guesses, value =2,
                                command = self.processButtons)
        rbgus3 = Radiobutton(frame1, text = "Guess 3",
                                variable = self.guesses, value =3,
                                command = self.processButtons)
        rbgus4 = Radiobutton(frame1, text = "Guess 4",
                                variable = self.guesses, value =4,
                                command = self.processButtons)
        rbgus5 = Radiobutton(frame1, text = "Guess 5",
                                variable = self.guesses, value =5,
                                command = self.processButtons)
        rbgus6 = Radiobutton(frame1, text = "Guess 6",
                                variable = self.guesses, value =6,
                                command = self.processButtons)
        rbgus7 = Radiobutton(frame1, text = "Guess 7",
                                variable = self.guesses, value =7,
                                command = self.processButtons)
        
        
        
        rbgus1.grid(row = 1, column = 1)
        rbgus2.grid(row = 1, column = 2)
        rbgus3.grid(row = 1, column = 3)
        rbgus4.grid(row = 1, column = 4)
        rbgus5.grid(row = 1, column = 5)
        rbgus6.grid(row = 1, column = 6)
        rbgus7.grid(row = 1, column = 7)
        
        window.mainloop()

    def processButtons(self):
        
        color = 'grey'
        self.clear()

        

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
            
                                    
        
            
        
        #print("you have " + ("Diamond " if self.radio == 1 else "Triangle"))

    def clear(self):
        self.canvas.delete('polygon')

        


HangmanGUI()
        
