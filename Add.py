from tkinter import *
import tkinter.messagebox
import sqlite3
import os

try:
    db = sqlite3.connect("D:\stockmanager\Database\stock_manager.db")
    c = db.cursor()
except:
    print(" database not available")
    
result = c.execute("select max(id) from stock_manager")
for r in result:
    id = r[0]


def back():
    win.destroy()
    Call = os.system("D:\stockmanager/Main.py")
    print(Call)


def back1():
    Call = os.system("D:\stockmanager/Main.py")
    print(Call)


def exit():
    tkinter.messagebox.showinfo("Exit", "Do you really wanna Exit?")
    win.destroy()


class stock:
    def __init__(self, win):
        self.win = win
        Label(win, text="STOCK MANAGER", font=("Times New Roman", 30), bg="seagreen", fg="white", bd=5,
              relief=GROOVE, width=50, pady=2).pack()
        text_L = LabelFrame(win, text="Product info", font=("Times New Roman", 11, "bold"), bg="seagreen", fg="white")
        text_L.place(x=0, y=60, width=340, height=650)

        id_t = Label(text_L, text="Enter Id", font=("Times New Roman", 20), bg="seagreen", fg="white")
        id_t.place(x=0, y=15)
        name_t = Label(text_L, text="Enter Product Name: ", font=("Times New Roman", 20), bg="seagreen", fg="white")
        name_t.place(x=0, y=70)
        QTY_t = Label(text_L, text="Enter Quantity: ", font=("Times New Roman", 20), bg="seagreen", fg="white")
        QTY_t.place(x=0, y=120)
        cost_price_t = Label(text_L, text="Enter Cost Price: ", font=("Times New Roman", 20), bg="seagreen", fg="white")
        cost_price_t.place(x=0, y=170)
        selling_price_t = Label(text_L, text="Enter Selling Price: ", font=("Times New Roman", 20), bg="seagreen",
                                fg="white")
        selling_price_t.place(x=0, y=225)
        suppliers_t = Label(text_L, text="Enter Suppliers Name ", font=("Times New Roman", 20), bg="seagreen",
                            fg="white")
        suppliers_t.place(x=0, y=270)
        suppliers_phonenumber_t = Label(text_L, text="Enter Suppliers Phonenumber", font=("Times New Roman", 20),
                                        fg="white"
                                        , bg="seagreen")
        suppliers_phonenumber_t.place(x=0, y=320)

        entry_L = LabelFrame(win, text="Product Entery", font=("Times New Roman", 11, "bold"), bg="seagreen",
                             fg="white")
        entry_L.place(x=341, y=60, width=407, height=650)

        self.id_e = Entry(entry_L, text="Enter Id", width=7, font=("Times New Roman", 20), bd=5)
        self.id_e.place(x=30, y=15)
        self.id_e.focus()

        self.name_e = Entry(entry_L, width=24, font=("Times New Roman", 20), bd=5)
        self.name_e.place(x=30, y=70)
        self.QTY_e = Entry(entry_L, width=15, font=("Times New Roman", 20), bd=5)
        self.QTY_e.place(x=30, y=120)
        self.cost_price_e = Entry(entry_L, width=15, font=("Times New Roman", 20), bd=5)
        self.cost_price_e.place(x=30, y=170)
        self.selling_price_e = Entry(entry_L, width=15, font=("Times New Roman", 20), bd=5)
        self.selling_price_e.place(x=30, y=220)
        self.suppliers_e = Entry(entry_L, width=25, font=("Times New Roman", 20), bd=5)
        self.suppliers_e.place(x=30, y=270)
        self.suppliers_phone = Entry(entry_L, width=15, font=("Times New Roman", 20), bd=5)
        self.suppliers_phone.place(x=30, y=320)

        button = LabelFrame(win, text="Button", font=("Times New Roman", 11, "bold"), bg="seagreen", fg="white", bd=5)
        button.place(x=0, y=450, width=1024, height=100)

        search_b = Button(button, text="Search", font=("Times New Roman", 10), width=12, bd=5,
                          command=self.search)
        search_b.place(x=410, y=0)

        submit_b = Button(button, text="Submit", font=("Times New Roman", 10), width=12, bd=5,
                          command=self.update)
        submit_b.place(x=300, y=0)

        clear_b = Button(button, text="Clear", font=("Times New Roman", 10), width=12, bd=5, command=self.clear)
        clear_b.place(x=520, y=0)

        del_b = Button(button, text="Delete", font=("Times New Roman", 10), bd=5, width=12, command=self.delete)
        del_b.place(x=640, y=0)

        id_t = Label(win, text="Total ID no: " + str(id), font=("Times New Roman", 12), bg="seagreen", fg="white")
        id_t.place(x=490, y=97)

        show_b = Button(button, text="Records", font=("Times New Roman", 10), bd=5, width=12,
                        command=self.show_records)
        show_b.place(x=760, y=0)

        add_b = Button(button, text="ADD", font=("Times New Roman", 10), bd=5, width=15,
                       command=manager)
        add_b.place(x=10, y=0)
        back_b = Button(win, text="Back", font=("Times New Roman", 10), bd=5, width=15, command=back, bg="seagreen")
        back_b.place(x=900, y=10)
        exit_b = Button(button, text="Exit", font=("Times New Roman", 10), bd=5, width=15, command=exit)
        exit_b.place(x=870, y=0)

        self.box = LabelFrame(win, text="Records", bg="seagreen", fg="white", font=("Times New Roman", 11, "bold"))
        self.box.place(x=748, y=60, width=270, height=392)

    def search(self):
        id_s = self.id_e.get()
        sql = "SELECT * FROM stock_manager WHERE id=?"
        search = c.execute(sql, id_s)
        for s in search:
            self.s1 = s[1]
            self.s2 = s[2]
            self.s3 = s[3]
            self.s4 = s[4]
            self.s5 = s[5]
            self.s6 = s[6]
        db.commit()

        self.name_e.delete(0, END)
        self.name_e.insert(0, str(self.s1))

        self.QTY_e.delete(0, END)
        self.QTY_e.insert(0, str(self.s2))

        self.cost_price_e.delete(0, END)
        self.cost_price_e.insert(0, str(self.s3))

        self.selling_price_e.delete(0, END)
        self.selling_price_e.insert(0, str(self.s4))

        self.suppliers_e.delete(0, END)
        self.suppliers_e.insert(0, str(self.s5))

        self.suppliers_phone.delete(0, END)
        self.suppliers_phone.insert(0, str(self.s6))

    def update(self):
        u1 = self.name_e.get()
        u2 = self.QTY_e.get()
        u3 = self.cost_price_e.get()
        u4 = self.selling_price_e.get()
        u5 = self.suppliers_e.get()
        u6 = self.suppliers_phone.get()

        my_db = "UPDATE stock_manager SET name=?, QTY=?, cost_price=?, selling_price=?, suppliers=?, " \
                "suppliers_phonenumber=? WHERE id=? "
        c.execute(my_db, (u1, u2, u3, u4, u5, u6, self.id_e.get()))
        db.commit()

    def clear(self):
        self.name_e.delete(0, END)
        self.QTY_e.delete(0, END)
        self.cost_price_e.delete(0, END)
        self.selling_price_e.delete(0, END)
        self.suppliers_e.delete(0, END)
        self.suppliers_phone.delete(0, END)

    def show_records(self):

        show = ""
        c.execute("SELECT id, name FROM stock_manager")
        i = c.fetchall()
        for records in i:
            show += str(records) + "\n"
        Label(self.box, text=show, bg="seagreen", fg="white", font=("Times New Roman", 15)).place(x=0, y=2)

    def delete(self):
        db = sqlite3.connect("D:\stockmanager\stock_manager.db")
        c = db.cursor()
        c.execute("Delete from stock_manager where id=" + self.id_e.get())
        db.commit()


class manager(stock):
    def __init__(self):

        self.windo = Tk()
        windo = self.windo
        windo.title("Update")
        windo.iconbitmap("D:\stockmanager\ic.ico")
        windo.geometry("1024x520")
        windo.config(bg="gray")
        title = Label(windo, text="ADD TO DATABASE", font=("Times New Roman", 30), bg="seagreen", fg="white", bd=5,
                      relief=GROOVE, width=50, pady=2).pack()
        text_L = LabelFrame(windo, text="Product info", font=("Times New Roman", 11, "bold"), bg="seagreen", fg="white")
        text_L.place(x=0, y=60, width=340, height=338)
        name_t = Label(text_L, text="Enter Product Name: ", font=("Times New Roman", 20), bg="seagreen", fg="white")
        name_t.place(x=0, y=15)
        QTY_t = Label(text_L, text="Enter Quantity: ", font=("Times New Roman", 20), bg="seagreen", fg="white")
        QTY_t.place(x=0, y=70)
        cost_price_t = Label(text_L, text="Enter Cost Price: ", font=("Times New Roman", 20), bg="seagreen", fg="white")
        cost_price_t.place(x=0, y=120)
        selling_price_t = Label(text_L, text="Enter Selling Price: ", font=("Times New Roman", 20), bg="seagreen",
                                fg="white")
        selling_price_t.place(x=0, y=170)
        suppliers_t = Label(text_L, text="Enter Suppliers Name ", font=("Times New Roman", 20), bg="seagreen",
                            fg="white")
        suppliers_t.place(x=0, y=225)
        suppliers_phonenumber_t = Label(text_L, text="Enter Suppliers Phonenumber", font=("Times New Roman", 20),
                                        bg="seagreen", fg="white")
        suppliers_phonenumber_t.place(x=0, y=270)

        entry_L = LabelFrame(windo, text="Product Entery", font=("Times New Roman", 11, "bold"), bg="seagreen",
                             fg="white")
        entry_L.place(x=341, y=60, width=407, height=338)
        self.name_e = Entry(entry_L, width=25, bd=5, font=("Times New Roman", 20))
        self.name_e.place(x=30, y=15)
        self.name_e.focus()

        self.QTY_e = Entry(entry_L, width=10, bd=5, font=("Times New Roman", 20))
        self.QTY_e.place(x=30, y=70)
        self.cost_price_e = Entry(entry_L, width=15, bd=5, font=("Times New Roman", 20))
        self.cost_price_e.place(x=30, y=120)
        self.selling_price_e = Entry(entry_L, width=15, bd=5, font=("Times New Roman", 20))
        self.selling_price_e.place(x=30, y=170)
        self.suppliers_e = Entry(entry_L, width=25, bd=5, font=("Times New Roman", 20))
        self.suppliers_e.place(x=30, y=220)
        self.suppliers_phone = Entry(entry_L, width=15, bd=5, font=("Times New Roman", 20))
        self.suppliers_phone.place(x=30, y=270)

        button = LabelFrame(windo, text="Button", bg="seagreen", font=("Times New Roman", 11, "bold"), fg="white")
        button.place(x=0, y=400, width=1024, height=200)

        submit_b = Button(button, text="submit", font=("Times New Roman", 10), bd=5, width=12, command=self.submit)
        submit_b.place(x=350, y=0)

        clear_b = Button(button, text="clear", font=("Times New Roman", 10), bd=5, width=12, command=self.clear)
        clear_b.place(x=460, y=0)

        show_b = Button(button, text="Records", font=("Times New Roman", 10), bd=5, width=12,
                        command=self.show_records)
        show_b.place(x=750, y=0)

        back_b = Button(windo, text="Back", font=("Times New Roman", 10), bd=5, width=15, command=back1, bg="seagreen")
        back_b.place(x=870, y=10)

        self.box = LabelFrame(windo, text="Records", font=("Times New Roman", 11, "bold"), bg="seagreen", fg="white")
        self.box.place(x=751, y=60, width=270, height=338)

        self.scroll = Scrollbar(self.box, orient=VERTICAL)
        self.scroll.pack(side=RIGHT, fill=Y)

        win.mainloop()

    def submit(self):
        name = self.name_e.get()
        QTY = self.QTY_e.get()
        cost_price = self.cost_price_e.get()
        selling_price = self.selling_price_e.get()
        suppliers = self.suppliers_e.get()
        suppliers_phonenumber = self.suppliers_phone.get()

        if name == "" or QTY == "" or cost_price == "" or selling_price == "" or suppliers == \
                "" or suppliers_phone == "":
            tkinter.messagebox.showerror("ERROR", "Fill all the Entry")
        else:
            tkinter.messagebox.showinfo("Successful", "submitted")
            sql = "INSERT INTO stock_manager (name, QTY, cost_price, selling_price, suppliers, suppliers_phonenumber) " \
                  "values(?,?,?,?,?,?) "
            c.execute(sql, (
                name, QTY, cost_price, selling_price, suppliers, suppliers_phonenumber))
            db.commit()
            tkinter.messagebox.showinfo("Successful", "submitted")

            self.name_e.delete(0, END)
            self.QTY_e.delete(0, END)
            self.cost_price_e.delete(0, END)
            self.selling_price_e.delete(0, END)
            self.suppliers_e.delete(0, END)
            self.suppliers_phone.delete(0, END)


win = Tk()
obj = stock(win)
win.title("Stock Manager")
win.iconbitmap("D:\stockmanager\ic.ico")
win.geometry("1024x520+0+0")
win.maxsize(1024, 520)
win.minsize(1024, 520)
win.config(bg="#074463")

win.mainloop()