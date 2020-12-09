from tkinter import *
from tkinter import messagebox
from db import Database

db = Database('store.db')

def populate_list():
    seed_list.delete(0, END)
    for row in db.fetch():
        seed_list.insert(END, row)

def add_item():
    if strain_text.get() == '' or types_text.get() == '' or date_text.get() == '' or quantity_text.get() == '':
        messagebox.showerror('Required Fields', 'Please include all fields')
        return
    db.insert(strain_text.get(), types_text.get(), date_text.get(), quantity_text.get())
    seed_list.delete(0, END)
    seed_list.insert(END, (strain_text.get(), types_text.get(), date_text.get(), quantity_text.get()))
    clear_text()
    populate_list()

def select_item(event):
    try:
        global selected_item
        index = seed_list.curselection()[0]
        selected_item = seed_list.get(index)

        strain_entry.delete(0, END)
        strain_entry.insert(END, selected_item[1])

        types_entry.delete(0, END)
        types_entry.insert(END, selected_item[2])

        date_entry.delete(0, END)
        date_entry.insert(END, selected_item[3])

        quantity_entry.delete(0, END)
        quantity_entry.insert(END, selected_item[4])
    except IndexError:
        pass
    
def remove_item():
    db.remove(selected_item[0])
    clear_text()
    populate_list()

def update_item():
    db.update(selected_item[0], strain_text.get(), types_text.get(),
              date_text.get(), quantity_text.get())
    populate_list()

def clear_text():
    strain_entry.delete(0, END)
    types_entry.delete(0, END)
    date_entry.delete(0, END)
    quantity_entry.delete(0, END)

# Create window object
app = Tk()

# Strain
strain_text = StringVar()
strain_label = Label(app, text='Strain', font=('bold', 14), pady=20)
strain_label.grid(row=0, column=0, sticky=W)
strain_entry = Entry(app, textvariable=strain_text)
strain_entry.grid(row=0, column=1)

# Type
types_text = StringVar()
types_label = Label(app, text='Type', font=('bold', 14))
types_label.grid(row=0, column=2, sticky=W)
types_entry = Entry(app, textvariable=types_text)
types_entry.grid(row=0, column=3)

# Date
date_text = StringVar()
date_label = Label(app, text='Date', font=('bold', 14))
date_label.grid(row=1, column=0, sticky=W)
date_entry = Entry(app, textvariable=date_text)
date_entry.grid(row=1, column=1)

# Quantity
quantity_text = StringVar()
quantity_label = Label(app, text='Quantity', font=('bold', 14))
quantity_label.grid(row=1, column=2, sticky=W)
quantity_entry = Entry(app, textvariable=quantity_text)
quantity_entry.grid(row=1, column=3)

# Seed List
seed_list = Listbox(app, height=8, width=50, border=0)
seed_list.grid(row=3, column=0, columnspan=3, rowspan=6, pady=20, padx=20)

# Create scrollbar
scrollbar = Scrollbar(app)
scrollbar.grid(row=3, column=3)

# Set scroll to listbox
seed_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=seed_list.yview)

# Bind select
seed_list.bind('<<ListboxSelect>>', select_item)

# Buttons
add_btn = Button(app, text="Add Seeds", width=12, command=add_item)
add_btn.grid(row=2, column=0, pady=20)

remove_btn = Button(app, text="Remove Seeds", width=12, command=remove_item)
remove_btn.grid(row=2, column=1)

update_btn = Button(app, text="Update Seeds", width=12, command=update_item)
update_btn.grid(row=2, column=2)

clear_btn = Button(app, text="Clear Input", width=12, command=clear_text)
clear_btn.grid(row=2, column=3, pady=20)

app.title('Seed Tracker')
app.geometry('650x500')

# Populate data
populate_list()

# Start program
app.mainloop()






