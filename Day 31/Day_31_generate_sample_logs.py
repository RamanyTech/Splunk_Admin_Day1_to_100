import random
import time
from datetime import datetime

# Function to generate realistic postfix syslog sample data (100 lines)
def generate_postfix_syslog():
    postfix_logs = []
    for i in range(100):
        timestamp = datetime.now().strftime("%b %d %H:%M:%S")
        message_id = f"{random.randint(1000, 9999)}{random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}{random.randint(1000, 9999)}"
        recipient = random.choice(['user@example.com', 'admin@example.org', 'test@domain.com'])
        relay_ip = f"192.168.{random.randint(1, 255)}.{random.randint(1, 255)}"
        delay = round(random.uniform(0.1, 1.0), 2)
        status = random.choice(['sent', 'deferred', 'bounced'])
        postfix_logs.append(f"{timestamp} server postfix/smtp[{random.randint(1000, 9999)}]: {message_id}: to=<{recipient}>, relay={relay_ip}[{random.randint(1000, 9999)}]:25, delay={delay}, status={status} (250 2.0.0 Ok: queued as {random.randint(1000, 9999)})")
    return "\n".join(postfix_logs)


# Function to generate realistic breakable text sample data (100 lines)
def generate_breakable_text():
    breakable_text_logs = []
    for i in range(100):
        if i % 10 == 0:
            breakable_text_logs.append(f"=== BREAK SECTION {i//10 + 1} ===")
        if random.random() > 0.8:
            breakable_text_logs.append("    ")  # Blank lines
        else:
            breakable_text_logs.append(f"Sample log data without a timestamp. Random text on line {i + 1}.")
    return "\n".join(breakable_text_logs)


# Function to save data to a file
def save_to_file(filename, data):
    with open(filename, 'w') as f:
        f.write(data)

# Generate and save all the logs
def generate_and_save_logs():
    # Generate logs
    postfix_data = generate_postfix_syslog()
    breakable_text_data = generate_breakable_text()

    # Save logs to files
    save_to_file('postfix_syslog.log', postfix_data)
    save_to_file('breakable_text.log', breakable_text_data)
    
    print("Sample log files with 100 lines generated successfully!")

# Run the script
if __name__ == "__main__":
    generate_and_save_logs()
