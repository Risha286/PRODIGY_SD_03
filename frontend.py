import tkinter as tk
from tkinter import messagebox

class ContactManagerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Contact Management System")
        
        # Create GUI elements
        self.add_button = tk.Button(master, text="Add Contact", command=self.add_contact)
        self.view_button = tk.Button(master, text="View Contacts", command=self.view_contacts)
        
        # Layout GUI elements
        self.add_button.pack()
        self.view_button.pack()
        
    def add_contact(self):
        name = input("Enter contact name: ")
        phone = input("Enter contact phone number: ")
        email = input("Enter contact email: ")
        
        messagebox.showinfo("Success", "Contact added successfully!")
    
    def view_contacts(self):
        messagebox.showinfo("View Contacts", "No contacts available.")

def main():
    root = tk.Tk()
    app = ContactManagerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
