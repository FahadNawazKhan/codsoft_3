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
root.geometry("600x400")

font_style = ("Helvetica Neue", 16)

entry_frame = Frame(root)
entry_frame.pack(side=TOP, fill=X, padx=20, pady=20)

name_label = Label(entry_frame, text="Name:", font=font_style)
name_label.pack(side=LEFT, padx=10)
name_entry = Entry(entry_frame, font=font_style)
name_entry.pack(side=LEFT, expand=True, fill=X, padx=10)

phone_label = Label(entry_frame, text="Phone:", font=font_style)
phone_label.pack(side=LEFT, padx=10)
phone_entry = Entry(entry_frame, font=font_style)
phone_entry.pack(side=LEFT, expand=True, fill=X, padx=10)

button_frame = Frame(root)
button_frame.pack(side=TOP, fill=X, padx=20, pady=20)

add_button = Button(button_frame, text="Add Contact", command=add_contact, font=font_style)
add_button.pack(side=LEFT, padx=10)

delete_button = Button(button_frame, text="Delete Contact", command=delete_contact, font=font_style)
delete_button.pack(side=LEFT, padx=10)

clear_button = Button(button_frame, text="Clear Contacts", command=clear_contacts, font=font_style)
clear_button.pack(side=LEFT, padx=10)

contact_list = Listbox(root, height=10, width=50, font=font_style)
contact_list.pack(side=TOP, fill=BOTH, expand=True, padx=20, pady=20)
contact_list.bind('<<ListboxSelect>>', get_selected_contact)

root.mainloop()
