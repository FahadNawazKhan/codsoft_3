from tkinter import *
from tkinter import messagebox

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    if name and phone:
        contact_list.insert(END, f"{name} - {phone}")
        name_entry.delete(0, END)
        phone_entry.delete(0, END)
    else:
        messagebox.showerror("Error", "Please enter both name and phone number.")

def delete_contact():
    try:
        selected_index = contact_list.curselection()[0]
        contact_list.delete(selected_index)
    except IndexError:
        messagebox.showerror("Error", "No contact selected.")

def clear_contacts():
    contact_list.delete(0, END)

def get_selected_contact(event):
    try:
        selected_index = contact_list.curselection()[0]
        selected_contact = contact_list.get(selected_index)
        name, phone = selected_contact.split(" - ")
        name_entry.delete(0, END)
        phone_entry.delete(0, END)
        name_entry.insert(END, name)
        phone_entry.insert(END, phone)
    except IndexError:
        pass

root = Tk()
root.title("Contact Book")

entry_frame = Frame(root)
entry_frame.pack(side=TOP, fill=X)

name_label = Label(entry_frame, text="Name:")
name_label.pack(side=LEFT)
name_entry = Entry(entry_frame)
name_entry.pack(side=LEFT, expand=True, fill=X)

phone_label = Label(entry_frame, text="Phone:")
phone_label.pack(side=LEFT)
phone_entry = Entry(entry_frame)
phone_entry.pack(side=LEFT, expand=True, fill=X)

button_frame = Frame(root)
button_frame.pack(side=TOP, fill=X)

add_button = Button(button_frame, text="Add Contact", command=add_contact)
add_button.pack(side=LEFT)

delete_button = Button(button_frame, text="Delete Contact", command=delete_contact)
delete_button.pack(side=LEFT)

clear_button = Button(button_frame, text="Clear Contacts", command=clear_contacts)
clear_button.pack(side=LEFT)

# Making the contact list bigger and modifying the layout to be more horizontal
contact_list = Listbox(root, height=10, width=50)
contact_list.pack(side=TOP, fill=BOTH, expand=True)
contact_list.bind('<<ListboxSelect>>', get_selected_contact)

root.mainloop()
