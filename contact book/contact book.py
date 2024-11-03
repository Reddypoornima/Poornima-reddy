class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactList:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print(f'Contact {contact.name} added successfully.')

    def view_contacts(self):
        if not self.contacts:
            print('No contacts found.')
            return
        print('Contact List:')
        for contact in self.contacts:
            print(f'Name: {contact.name}, Phone: {contact.phone}')

    def search_contact(self, search_term):
        results = [contact for contact in self.contacts if search_term.lower() in contact.name.lower() or search_term in contact.phone]
        if not results:
            print('No contacts found.')
            return
        print('Search Results:')
        for contact in results:
            print(f'Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}, Address: {contact.address}')

    def update_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                contact.phone = input('Enter new phone: ').strip()
                contact.email = input('Enter new email: ').strip()
                contact.address = input('Enter new address: ').strip()
                print(f'Contact {name} updated successfully.')
                return
        print('Contact not found.')

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print(f'Contact {name} deleted successfully.')
                return
        print('Contact not found.')

def main():
    contact_list = ContactList()

    while True:
        print('\nOptions: add, view, search, update, delete, exit')
        choice = input('What would you like to do? ').strip().lower()

        if choice == 'add':
            name = input('Enter name: ').strip()
            phone = input('Enter phone: ').strip()
            email = input('Enter email: ').strip