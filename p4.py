class Contact:
    def __init__(self, name, phone_number, email):
        self.name, self.phone_number, self.email = name, phone_number, email

class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def display_contacts(self):
        print("Address Book:")
        for contact in self.contacts:
            print(f"Name: {contact.name}")
            print(f"Phone Number: {contact.phone_number}")
            print(f"Email: {contact.email}")
            print()

contact1 = Contact("Sami", "123-456-7890", "sami@example.com")
contact2 = Contact("Daniyal", "987-654-3210", "daniyal@example.com")

address_book = AddressBook()

address_book.add_contact(contact1)
address_book.add_contact(contact2)

address_book.display_contacts()