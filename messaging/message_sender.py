# message_sender.py
def send_message(email, message):
    if not email:
        raise ValueError("Email address is missing")
    
    # Simulate sending a message (replace this with actual email sending logic if needed)
    print(f"Sending message to {email}: {message}")