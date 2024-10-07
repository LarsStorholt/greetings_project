# main.py

from contacts import ContactsManager
from messaging import generate_message, send_message, log_message

def main():

    contact_manager = ContactsManager()
    
    contacts = contact_manager.get_contacts()

    for contact in contacts:
        
        message = generate_message(contact['name'])

        try:
            send_message(contact['email'], message)
            log_message(contact, message)
        except ValueError as e:
            print(f"Failed to send message to {contact['name']}: {e}")

if __name__ == "__main__":
    main()
