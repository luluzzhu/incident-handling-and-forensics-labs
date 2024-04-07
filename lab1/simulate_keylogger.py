import random
import datetime

applications = ['Web Browser', 'Text Editor', 'Email Client']

inputs = ['hello', 'password123', 'john.doe@example.com', 'search for cat videos', 'how to learn python']

def generate_log_entry():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    application = random.choice(applications)
    input_text = random.choice(inputs)
    return f"{timestamp} - {application} - {input_text}"

def write_log_entries(filename, entries_count=10):
    with open(filename, 'w') as file:
        for _ in range(entries_count):
            log_entry = generate_log_entry()
            print(log_entry)
            file.write(log_entry + "\n")

write_log_entries("mock_keylogger_data.txt", 50)
