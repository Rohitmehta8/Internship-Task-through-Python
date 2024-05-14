class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone_number, email, address):
        self.contacts[name] = {'phone_number': phone_number, 'email': email, 'address': address}
        print("Contact added successfully!")

    def view_contact_list(self):
        print("Contact List:")
        for name, contact_info in self.contacts.items():
            print(f"Name: {name}, Phone: {contact_info['phone_number']}")

    def search_contact(self, search_term):
        found = False
        for name, contact_info in self.contacts.items():
            if search_term.lower() in name.lower() or search_term in contact_info['phone_number']:
                print(f"Name: {name}, Phone: {contact_info['phone_number']}, Email: {contact_info['email']}, Address: {contact_info['address']}")
                found = True
        if not found:
            print("Contact not found.")

    def update_contact(self, name, new_phone_number, new_email, new_address):
        if name in self.contacts:
            self.contacts[name] = {'phone_number': new_phone_number, 'email': new_email, 'address': new_address}
            print("Contact updated successfully!")
        else:
            print("Contact not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found.")

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_book.add_contact(name, phone_number, email, address)
        elif choice == '2':
            contact_book.view_contact_list()
        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            contact_book.search_contact(search_term)
        elif choice == '4':
            name = input("Enter name of contact to update: ")
            new_phone_number = input("Enter new phone number: ")
            new_email = input("Enter new email: ")
            new_address = input("Enter new address: ")
            contact_book.update_contact(name, new_phone_number, new_email, new_address)
        elif choice == '5':
            name = input("Enter name of contact to delete: ")
            contact_book.delete_contact(name)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()
