from tkinter import *
from PIL import ImageTk, Image
import os

window = Tk()
window.title("STOCK MANAGER")
window.iconbitmap("D:\stockmanager\ic.ico")
window.maxsize(450, 505)
window.minsize(450, 505)

my_img = ImageTk.PhotoImage(Image.open("logo.png"))
lab = Label(image=my_img)
lab.pack()


def bill():
    window.destroy()
    Call1 = os.system("D:\stockmanager/bill.py")
    print(Call1)


def second():
    window.destroy()
    Call1 = os.system("D:\stockmanager/second.py")
    print(Call1)


second_bu = Button(window, width=10, text="update", font=("Times New Roman", 15), bd=5, bg="seagreen",fg="white",
                   command=second)
second_bu.place(x=100, y=455)

bil_b = Button(window, width=10, text="bill", font=("Times New Roman", 15), bd=5,bg="seagreen",fg="white",
               command=bill)
bil_b.place(x=250, y=455)

window.mainloop()
