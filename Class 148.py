from tkinter import *
import random

root = Tk()
root.title("Lists")
root.geometry("550x500")
root.configure(bg = "blue")

gifList = Label(root, bg = "black", fg = "white")
randomList = Label(root, bg = "black", fg = "white")
giftlist = ["Bottle", "Tiffin Bag", "ID Card", "Chocolates", "Chips", "Tickets", "Hanky"]

def randomlist():
    gifList["text"] = "Random Gifts List : " + str(giftlist)
    randno = random.randint(0,7)
    giftno = giftlist[randno]
    randomList["text"] = "Give Gift : " + str(giftno)
    
button = Button(root,text = "Give Random Gift", command = randomlist, bg = "black", fg = "white")

button.place(relx = 0.5, rely = 0.5, anchor = CENTER)
randomList.place(relx = 0.5, rely = 0.6, anchor = CENTER)
gifList.place(relx = 0.5, rely = 0.7, anchor = CENTER)


root.mainloop()