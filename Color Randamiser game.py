from tkinter import *
import random

root = Tk()
root.title("COLOR RANDOMIZER GAME")
root.geometry("1000x900")

lbl_color = Label(root,font = ("Comic Sans MS", 20, "bold"))
lbl_color.place(relx = 0.5, rely = 0.4, anchor = CENTER)

class Color():
    def __init__(self):
        self.__color = 0
        
    def updateScore(self):
        list = ["blue","pink","green","yellow","red"]
        random_no = random.randint(0,5)
        lbl_color["text"] =  list[random_no]
        lbl_color["fg"] =  list[random_no]
        
obj = Color()

btn = Button(root,text="Start",command=obj.updateScore())
btn.place(relx=0.5,rely=0.5,anchor=CENTER)
root.mainloop()