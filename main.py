# main.py

from contacts import ContactsManager
from messaging import generate_message, send_message, log_message

def main():
    # Initialize ContactsManager
    contact_manager = ContactsManager()
    
    # Fetch contacts
    contacts = contact_manager.get_contacts()

    # Iterate over each contact
    for contact in contacts:
        # Generate the personalized message
        message = generate_message(contact['name'])

        # Send the message (simulated)
        try:
            send_message(contact['email'], message)
            # Log the message after sending
            log_message(contact, message)
        except ValueError as e:
            print(f"Failed to send message to {contact['name']}: {e}")

if __name__ == "__main__":
    main()
