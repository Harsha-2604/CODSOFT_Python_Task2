class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}, Address: {self.address}"


class ContactManager:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email, address):
        if phone in self.contacts:
            print("Contact with this phone number already exists.")
        else:
            contact = Contact(name, phone, email, address)
            self.contacts[phone] = contact
            print("Contact added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            for phone, contact in self.contacts.items():
                print(contact)

    def search_contact(self, search_term):
        results = [contact for contact in self.contacts.values() if search_term in contact.name or search_term in contact.phone]
        if results:
            for contact in results:
                print(contact)
        else:
            print("No contacts found.")

    def update_contact(self, phone):
        if phone in self.contacts:
            name = input("Enter new name: ")
            email = input("Enter new email: ")
            address = input("Enter new address: ")
            self.contacts[phone].name = name
            self.contacts[phone].email = email
            self.contacts[phone].address = address
            print("Contact updated successfully.")
        else:
            print("Contact not found.")

    def delete_contact(self, phone):
        if phone in self.contacts:
            del self.contacts[phone]
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")


def main():
    manager = ContactManager()
    
    while True:
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            manager.add_contact(name, phone, email, address)
        elif choice == '2':
            manager.view_contacts()
        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            manager.search_contact(search_term)
        elif choice == '4':
            phone = input("Enter phone number of the contact to update: ")
            manager.update_contact(phone)
        elif choice == '5':
            phone = input("Enter phone number of the contact to delete: ")
            manager.delete_contact(phone)
        elif choice == '6':
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
