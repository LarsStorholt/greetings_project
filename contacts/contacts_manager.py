import json

class ContactsManager:
    def __init__(self):
        self.contacts = [
                {"name": "Alice", "email": "abc@example.com", "preferred_time": "08:00 AM"},
                {"name": "Bob", "email": "bcd@example.com", "preferred_time": "09:00 AM"},
                {"name": "Charlie", "email": "cde@example.com", "preferred_time": "07:30 AM"}
        ]
        
    def add_contact(self, name, email, preferred_time="08:00 AM"):
        if not name:
            raise ValueError("Name cannot be empty.")
        if not email:
            raise ValueError("Email cannot be empty.")
    
        contact = {
            'name': name,
            'email': email,
            'preferred_time': preferred_time
        }
        self.contacts.append(contact)

    def remove_contact(self, name):
        self.contacts = [c for c in self.contacts if c['name'] != name]

    def get_contacts(self):
        if not self.contacts: 
            print("Warning: No contacts found!")
        return self.contacts

    def list_contacts(self):
        if not self.contacts: 
            print("No contacts in the list.")
        for contact in self.contacts:
            print(f"Name: {contact['name']}, Email: {contact['email']}, Preferred Time: {contact['preferred_time']}")
    




