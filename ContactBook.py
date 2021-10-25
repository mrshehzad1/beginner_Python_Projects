import sqlite3 as sql
import tkinter as tk
from tkinter import *

window = tk.Tk()
window.minsize(400, 400)
window.title('CONTACT BOOK')


def save_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    conn = sql.connect('contact.db')
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO contact_book VALUES(?,?)", [name, phone])
    except sql.Error:
        conn.rollback()
        raise
    else:
        conn.commit()
    finally:
        conn.close()


def delete_contact():
    name = del_entry.get()
    conn = sql.connect('contact.db')
    cur = conn.cursor()
    try:
        for row in cur.execute('SELECT rowid, * FROM contact_book'):
            if name == row[1]:
                cur.execute("DELETE FROM contact_book WHERE rowid=(?)", str(row[0]))
                break
    except sql.Error:
        conn.rollback()
    else:
        conn.commit()
    finally:
        conn.close()


def search_con():
    search_label.configure(text='Search With Name')
    conn = sql.connect('contact.db')
    name = str(search_entry.get()).lower()
    cur = conn.cursor()
    try:
        for row in cur.execute("SELECT rowid, * FROM contact_book"):
            if name in row:
                search_label.configure(text='Name: {}\nContact: {}'.format(row[1].upper(), row[2]))
                break
            elif name not in row:
                search_label.configure(text='Contact Does Not Exist')
                continue
    except sql.Error:
        conn.rollback()
    finally:
        conn.close()


def contact_list():
    conn = sql.connect('contact.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM contact_book")
    row = cur.fetchall()
    file = open('contacts.txt', 'w+')
    for items in row:
        file.write(f"{items[0]} {items[1]}\n")
    conn.close()


# Main Canvas
canvas = Canvas(window, bg='#87fc9e')
canvas.place(relheight=1, relwidth=1)

################ Search ##############################
search_label = tk.Label(canvas, text='Search With Name', bg='#87fc9e')
search_label.place(x=60, y=170)
search_entry = tk.Entry(canvas, width=20)
search_entry.place(x=60, y=150)
search_button = tk.Button(canvas, text='Search Contact', font=('calibri', 8, 'bold'), bd=3, command=search_con)
search_button.place(x=200, y=150)
################# Save Contact #################
# SAve Contact Entry
name_label = tk.Label(canvas, text="Name", bg='#87fc9e')
name_label.place(x=60, y=25)
name_entry = tk.Entry(canvas, width=20)
name_entry.focus()
name_entry.place(x=60, y=45)
phone_label = tk.Label(canvas, text="Phone No.", bg='#87fc9e')
phone_label.place(x=200, y=25)
phone_entry = tk.Entry(canvas, width=20)
phone_entry.place(x=200, y=45)
save_button = tk.Button(canvas, text='Save Contact', font=('calibri', 8, 'bold'), bd=3, command=save_contact)
save_button.place(x=60, y=70)
################ Delete Contact ################
del_label = tk.Label(canvas, text="Delete With Name", bg='#87fc9e')
del_label.place(x=60, y=230)
del_button = tk.Button(canvas, text='Delete Contact', font=('calibri', 8, 'bold'), bd=3, command=delete_contact)
del_button.place(x=200, y=250)
# Delete Entry Box
del_entry = tk.Entry(canvas, width=20)
del_entry.place(x=60, y=250)
################ Contact list #################
contact_list_button = tk.Button(canvas, text='Contact List', font=('calibri', 8, 'bold'), bd=3, command=contact_list)
contact_list_button.place(x=200, y=180)
window.mainloop()
