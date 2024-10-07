import random 

def generate_message(name):
    messages = [
        f"Good Morning, {name}! Wishing you a fantastic day ahead!",
        f"Hello {name}, rise and shine! Hope you have an amazing day!",
        f"Hey {name}, good morning! Have a productive and wonderful day!",
        f"{name}, good morning! Make today as great as you are!",
        f"Morning {name}! Ready to conquer the day?",
        f"Hi {name}, sending you good vibes for a great day!"
    ]
    
    return random.choice(messages)

