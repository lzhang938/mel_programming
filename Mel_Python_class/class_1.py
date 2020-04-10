
from tkinter import *
import random


def startGame(event):
    if (timeleft == 30):
        countdown()
    nextColor()


def nextColor():
    global score
    global timeleft
    if (timeleft>0):
        e.focus_set()
        if e.get().lower() == colors[1]:
            score += 1
        e.delete(0, END)
        random.shuffle(colors)
        colorLabel.config(fg=str(colors[1]), text=str(colors[0]))
        scoreLabel.config(text="Score: " + str(score))


def countdown():
    global timeleft
    if timeleft > 0:
        timeleft -= 1

        timeLabel.config(text="Time Left: " + str(timeleft))
        timeLabel.after(1000, countdown)


score = 0
colors = ['yellow', 'green', 'blue', 'purple', 'black', 'brown', 'pink', 'orange',
          'red']
timeleft = 30
window = Tk()
window.title("Color Game")
window.geometry("375x200")

instructions = Label(window, text="Type the color of the word, not the word itself", font=("Arial", 12))
instructions.pack()

scoreLabel = Label(window, text="Please press enter to start the game!", font=("Arial", 12))
scoreLabel.pack()

timeLabel = Label(window, text="Time Left: " + str(timeleft), font=("Arial", 12))
timeLabel.pack()

colorLabel = Label(window, font=("Arial", 60))
colorLabel.pack()
window.bind('<Return>', startGame)
e = Entry(window)
e.pack()

e.focus_set()

window.mainloop()
