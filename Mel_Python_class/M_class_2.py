
from tkinter import *
import random
USER_CHOICE=""
COMP_CHOICE=""
USER_SCORE=0
COMP_SCORE=0
def choice_to_number(choice):
    rps={'rock':0, 'paper':1, 'scissor':2}
    return rps[choice]
def number_to_choice(number):
    rps={0:'rock', 1:'paper', 2:'scissor'}
    return rps[number]
def random_computer_choice():
    return random.choice(['rock', 'paper', 'scissor'])
def result(human_choice, comp_choice):
    global USER_SCORE
    global COMP_SCORE

    user=choice_to_number(human_choice)
    comp=choice_to_number(comp_choice)
    if (user==comp):
        print("TIE")
    elif((user-comp)%3==1):
        USER_SCORE+=1
        print("YOU WON!")
    else:
        COMP_SCORE+=1
        print("COMP WON")
    output="Your choice: " + USER_CHOICE +"\n Computer's choice: " + COMP_CHOICE + "\n Your score: " +str(USER_SCORE) + "\n Comp Score: " + str(COMP_SCORE)
    texty.insert(END, output)
def rock():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE="rock"
    COMP_CHOICE=random_computer_choice()
    result(USER_CHOICE, COMP_CHOICE)
def paper():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE="paper"
    COMP_CHOICE=random_computer_choice()
    result(USER_CHOICE, COMP_CHOICE)
def scissor():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE="scissor"
    COMP_CHOICE=random_computer_choice()
    result(USER_CHOICE, COMP_CHOICE)

window=Tk()
window.geometry("400x300")
window.title("Turnip King's Rock Paper Scissors Game!")


button1=Button(window, text="       ROCK       ", bg="blue", command=rock)
button1.pack()
button2=Button(window, text="       PAPER      ", bg="yellow")
button2.pack()
button3=Button(window, text="       SCISSOR    ", bg="green")
button3.pack()

texty=Text(window, height=12, width=30)
texty.pack()


window.mainloop()
