import random
from tkinter import *

#import os


root = Tk()
root.geometry("600x600")
root.title("Frog-click")

label = Label(root)

img = PhotoImage(file="zabikrol.png")
img2 = PhotoImage(file="swiatecznazabka.png")
img3 = PhotoImage(file="zabkagreat.png")
img4 = PhotoImage(file="zabkaidziespac.png")
img5 = PhotoImage(file="zabkaiciastko.png")
img6 = PhotoImage(file="zabkasmutna.png")
img7 = PhotoImage(file="zabkastop.png")
img8 = PhotoImage(file="zabkawrr.png")
img9 = PhotoImage(file="click.png")

d = [img, img2, img3, img4, img5, img6, img7, img8]

label.config(image=img9)
label.pack()


current_img = img


def change():
    d = [img, img2, img3, img4, img5, img6, img7, img8]
    label.config(image=random.choice(d))
    
    label.pack()
    return()

bttn = Button(root, width=10, padx=300, pady=50, height=20, text="Click for changing frogs!", bg="Light Green", activebackground="#66FF99", command=change)
bttn.place(x=-300, y=300)
bttn.pack(side=BOTTOM)

root.mainloop()
