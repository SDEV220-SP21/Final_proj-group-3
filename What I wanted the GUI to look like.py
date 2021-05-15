

from tkinter import *
import tkinter.messagebox 
from tkinter.filedialog import askopenfilename

#this is just the code that makes the GUI look as close as I could get to have
#the GUI as I envisioned with the entry box and guess button

#basic tkinter code to make a window, 
window = Tk()
window.title("Hangman 2: House Edition")
width = 1000
height = 500

frame1 = Frame(window)
frame1.pack()
canvas = Canvas(frame1, width=width, height=400, bg='white')
canvas.pack()

#canvas.create_line(200, 400, 800, 400 fill = "red", tags = "base"

frame2 = Frame(window)
frame2.pack()

letterGuess = ""

guesses = 0
def wrongGuess():
    guesses += 1

 

Label(frame2, text = "Guess A Letter: ").pack(side = LEFT)
#letterGuess = StringVar()
Entry(frame2, width = 20, textvariable = letterGuess).pack(side = LEFT)
Button(frame2, text = "Guess", command = None).pack(side = LEFT)


