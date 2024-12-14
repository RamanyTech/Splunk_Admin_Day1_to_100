import random
import datetime

def random_ip():
    return ".".join(str(random.randint(0, 255)) for _ in range(4))

def random_device_id():
    return f"Juniper{random.randint(100, 999)}"

def random_user_id():
    return f"user{random.randint(100, 999)}"

def random_port():
    return random.randint(20000, 30000)

def generate_log_entry():
    timestamp = datetime.datetime.now().strftime("%b %d %H:%M:%S")
    source_ip = random_ip()
    device_id = random_device_id()
    user_id = random_user_id()
    failed_ip = random_ip()
    failed_port = random_port()
    log_entry = (
        f"{timestamp} {source_ip} SSG350M: NetScreen device_id=[{device_id}] "
        f"[Root]system-warning-00518: Admin user \"{user_id}\" login attempt for Web(http) "
        f"management (port {failed_port}) from {failed_ip}:{random.randint(20000, 30000)} failed. "
        f"({datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')})"
    )
    return log_entry

def generate_logs(count=10):
    logs = [generate_log_entry() for _ in range(count)]
    return "\n".join(logs)

if __name__ == "__main__":
    num_logs = 100
    log_data = generate_logs(num_logs)
    print(log_data)
    with open("sample_logs.txt", "w") as log_file:
        log_file.write(log_data)
