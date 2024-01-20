class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print(f"\nContact '{contact.name}' added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("\nContact book is empty.")
        else:
            print("\nContact List:")
            for i, contact in enumerate(self.contacts, start=1):
                print(f"{i}. Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}, Address: {contact.address}")

    def search_contact(self, search_term):
        search_results = []
        for contact in self.contacts:
            if (search_term.lower() in contact.name.lower()) or (search_term in contact.phone):
                search_results.append(contact)
        
        if not search_results:
            print(f"\nNo contacts found for '{search_term}'.")
        else:
            print(f"\nSearch Results for '{search_term}':")
            for i, result_contact in enumerate(search_results, start=1):
                print(f"{i}. Name: {result_contact.name}, Phone: {result_contact.phone}, Email: {result_contact.email}, Address: {result_contact.address}")

    def update_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                new_phone = input("Enter the updated phone number (press Enter to keep the current one): ").strip()
                new_email = input("Enter the updated email (press Enter to keep the current one): ").strip()
                new_address = input("Enter the updated address (press Enter to keep the current one): ").strip()

                if new_phone:
                    contact.phone = new_phone
                if new_email:
                    contact.email = new_email
                if new_address:
                    contact.address = new_address

                print(f"\nContact '{contact.name}' updated successfully.")
                return
        print(f"\nContact with name '{name}' not found.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print(f"\nContact '{contact.name}' deleted successfully.")
                return
        print(f"\nContact with name '{name}' not found.")

def print_menu():
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def main():
    contact_book = ContactBook()

    while True:
        print_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter contact phone: ")
            email = input("Enter contact email: ")
            address = input("Enter contact address: ")
            new_contact = Contact(name, phone, email, address)
            contact_book.add_contact(new_contact)
        elif choice == '2':
            contact_book.view_contacts()
        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            contact_book.search_contact(search_term)
        elif choice == '4':
            name_to_update = input("Enter name of contact to update: ")
            contact_book.update_contact(name_to_update)
        elif choice == '5':
            name_to_delete = input("Enter name of contact to delete: ")
            contact_book.delete_contact(name_to_delete)
        elif choice == '6':
            print("\nExiting Contact Book. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()

