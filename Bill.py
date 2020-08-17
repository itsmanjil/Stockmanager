from tkinter import *
import tkinter.messagebox
import sqlite3
import os

try:
    db = sqlite3.connect("D:\stockmanager\Database\stock_manager.db")
    c = db.cursor()
except:
    print("database not available")
product_list = []
price_list = []
QTY_list = []
discount_list = []

total_list = []


def back():
    root.destroy()
    Call = os.system("D:\stockmanager/Main.py")
    print(Call)


def exit():
    tkinter.messagebox.showinfo("Exit", "Do you really wanna Exit?")
    root.destroy()


class bill:
    def __init__(self, root):
        self.root = root
        root.title("BILLING")
        root.iconbitmap("D:\stockmanager\ic.ico")
        root.geometry("1024x520+0+0")
        root.maxsize(1024, 520)
        root.minsize(1024, 520)
        Label(root, text="BILLING", font=("Times New Roman", 30), bg="seagreen", fg="white", bd=5,
              relief=GROOVE,
              width=50, pady=2).pack()

        self.text_L = LabelFrame(root, text="Product Entry", font=("Times New Roman", 11, "bold"), bg="seagreen",
                                 fg="white")
        self.text_L.place(x=5, y=60, width=515, height=210)

        self.bill = Listbox(root, bd=5, width=495, height=450, relief=GROOVE)
        self.bill.place(x=525, y=65)

        text_f = LabelFrame(root, text="Entry:", font=("Times New Roman", 11, "bold"), bg="seagreen", fg="white")
        text_f.place(x=5, y=280, width=515, height=230)

        self.ID_t = Label(self.text_L, text="Enter Product ID", font=("Times New Roman", 18), bg="seagreen", fg="white")
        self.ID_t.place(x=0, y=20)
        self.ID_e = Entry(self.text_L, width=12, font=("Times New Roman", 17), bd=5)
        self.ID_e.place(x=180, y=20)
        self.ID_e.focus()
        self.products_e = Entry(self.text_L, font=("Times New Roman", 18), bd=5, bg="seagreen", fg="white")
        self.products_e.place(x=180, y=80)
        self.price_e = Entry(self.text_L, font=("Times New Roman", 18), bd=5, bg="seagreen", fg="white")
        self.price_e.place(x=180, y=120)
        products_la = Label(self.text_L, text="Products: ", font=("Times New Roman", 18), bg="seagreen", fg="white")
        products_la.place(x=0, y=80)
        price_la = Label(self.text_L, text="Price: ", font=("Times New Roman", 18), bg="seagreen", fg="white")
        price_la.place(x=0, y=120)

        search_bu = Button(self.text_L, width=10, text="Search", font=("Times New Roman", 12), bd=5, command=self.half)
        search_bu.place(x=330, y=20)

        reset_bu = Button(self.text_L, width=6, text="reset", font=("Times New Roman", 12), bd=5, command=self.delete)
        reset_bu.place(x=440, y=20)

        products_l = Label(self.bill, text="Products", font=("Times New Roman", 18), bg="white")
        products_l.place(x=0, y=10)
        QTY_l = Label(self.bill, text="QTY", font=("Times New Roman", 18), bg="white")
        QTY_l.place(x=200, y=10)
        price_l = Label(self.bill, text="Price", font=("Times New Roman", 18), bg="white")
        price_l.place(x=400, y=10)
        discount_l = Label(self.bill, text="Discount", font=("Times New Roman", 18), bg="white")
        discount_l.place(x=290, y=10)
        total_l = Label(self.bill, text="Total:", font=("Times New Roman", 18), bg="white")
        total_l.place(x=285, y=400)
        self.total_a = Label(self.bill, text="", font=("Times New Roman", 18), bg="white")
        self.total_a.place(x=350, y=400)

        QTY_t = Label(text_f, text="Enter QTY: ", font=("Times New Roman", 18), bg="seagreen", fg="white")
        QTY_t.place(x=0, y=20)
        self.QTY_en = Entry(text_f, width=12, font=("Times New Roman", 15), bd=5)
        self.QTY_en.place(x=150, y=20)

        discount_t = Label(text_f, text="Enter Discont: ", font=("Times New Roman", 18), bg="seagreen",
                           fg="white")
        discount_t.place(x=0, y=60)
        self.discount_e = Entry(text_f, width=12, font=("Times New Roman", 15), bd=5)
        self.discount_e.place(x=150, y=60)
        self.discount_e.insert(END, 0)

        add = Button(text_f, text="ADD To Cart", width=10, bd=5, font=("Times New Roman", 12),
                     command=self.add)
        add.place(x=150, y=100)

        label_bu = Button(text_f, text="BILLING", width=10, bd=5, font=("Times New Roman", 12), command=self.add_labels)
        label_bu.place(x=150, y=150)
        exit_b = Button(text_f, text="EXIT", font=("Times New Roman", 10), bd=5, width=15, command=exit)
        exit_b.place(x=380, y=170)

        back_b = Button(root, text="Back", font=("Times New Roman", 10), bd=5, width=15, command=back, bg="seagreen")
        back_b.place(x=880, y=10)

    def half(self):
        id_p = self.ID_e.get()
        my_db = "select * from stock_manager where id = ?"
        c.execute(my_db, id_p)
        show = c.fetchall()
        for self.s in show:
            self.get_id = self.s[0]
            self.get_name = self.s[1]
            self.get_price = self.s[4]
            self.get_QTY = self.s[2]

        self.products_e.insert(0, str(self.get_name))
        self.price_e.insert(0, str(self.get_price))

    def delete(self):
        db = sqlite3.connect("D:\stockmanager\Database\stock_manager.db")
        c = db.cursor()
        c.execute("Delete from bill")
        db.commit()

    def add(self):
        id = self.ID_e.get()
        products = self.products_e.get()
        QTY = self.QTY_en.get()
        price = self.price_e.get()
        discount = self.discount_e.get()

        if products == "" or QTY == "" or price == "":
            tkinter.messagebox.showerror("ERROR", "Search for products")
        else:
            tkinter.messagebox.showinfo("Successful", "submitted")
            sql = "INSERT INTO bill (productse, QTYe, pricee, discounte) ""values(?,?,?,?) "
            sql2 = "update stock_manager set QTY = QTY-(select QTYe from bill) where id = '" + id + "' "
            sql1 = " update bill set totale = (QTYe*pricee)-(QTYe*pricee*discounte*0.01 )"

            c.execute(sql, (products, QTY, price, discount))
            c.execute(sql1)
            c.execute(sql2)
            db.commit()

            self.products_e.delete(0, END)
            self.QTY_en.delete(0, END)
            self.price_e.delete(0, END)
            self.discount_e.delete(0, END)
            self.ID_e.delete(0, END)

    def total(self):
        db = sqlite3.connect("D:\stockmanager\Database\stock_manager.db")
        c = db.cursor()
        c.execute("select pricee from bill ")
        result = c.fetchall()
        d = 0
        for x in result:
            d += x[0]
        self.total_a.configure(text="" + str(d))

        db.commit()

    def add_labels(self):
        self.total()
        my_db = "select * from bill"
        c.execute(my_db)
        show = c.fetchall()
        for self.s in show:
            get_name = self.s[1]
            get_price = self.s[4]
            get_QTY = self.s[2]
            get_discount = self.s[5]

            product_list.append(get_name)
            price_list.append(get_price)
            QTY_list.append(get_QTY)
            discount_list.append(get_discount)

            y_index = 58
            counter = 0

            for p in product_list:
                name = Label(self.bill, text=str(product_list[counter]), font=("Times New Roman", 12), bg="white")
                name.place(x=0, y=y_index)
                total_list.append(name)

                QTY = Label(self.bill, text=str(QTY_list[counter]), font=("Times New Roman", 12), bg="white")
                QTY.place(x=220, y=y_index)
                total_list.append(QTY)

                price = Label(self.bill, text=str(price_list[counter]), font=("Times New Roman", 12), bg="white")
                price.place(x=400, y=y_index)
                total_list.append(price)

                discount = Label(self.bill, text=str(discount_list[counter]), font=("Times New Roman", 12), bg="white")
                discount.place(x=310, y=y_index)
                total_list.append(price)

                y_index += 35
                counter += 1


root = Tk()
ob = bill(root)
root.config(bg="seagreen")

root.mainloop()
