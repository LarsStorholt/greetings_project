import datetime

def log_message(contact, message):
    log_file_path = "messaging/message_log.txt"
    with open(log_file_path, "a") as log_file:
        log_file.write(f"{datetime.datetime.now()} - Sent to {contact['name']}: {message}\n")
    
