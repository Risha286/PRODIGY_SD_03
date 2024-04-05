class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email):
        contact = Contact(name, phone, email)
        self.contacts.append(contact)

    def get_contacts(self):
        return self.contacts

def main():
    contact_manager = ContactManager()
    while True:
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Enter contact name: ")
            phone = input("Enter contact phone number: ")
            email = input("Enter contact email: ")
            contact_manager.add_contact(name, phone, email)
            print("Contact added successfully!")
        elif choice == "2":
            contacts = contact_manager.get_contacts()
            if contacts:
                print("Contacts:")
                for contact in contacts:
                    print(f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}")
            else:
                print("No contacts available.")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
