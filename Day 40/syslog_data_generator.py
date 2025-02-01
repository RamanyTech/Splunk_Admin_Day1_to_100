import os
import random
from datetime import datetime, timedelta

# Define base directory for logs
BASE_DIR = "/"

# Ensure base directory exists
os.makedirs(BASE_DIR, exist_ok=True)

# Sample Data Pools
hosts = ["host_server1", "host_router1", "host_firewall1", "host_switch-core"]
processes = ["kernel", "sshd", "systemd"]
protocols = ["BGP", "OSPF", "INTERFACE"]
firewall_actions = ["BLOCK", "ALLOW"]
vendors = ["PaloAlto", "CiscoASA"]
interfaces = ["GigabitEthernet1/0/1", "GigabitEthernet1/0/2"]
src_ips = ["192.168.50.5", "10.10.10.2", "192.168.8.1"]
dst_ips = ["10.0.3.5", "192.168.1.5"]
ports = [443, 55443, 50230]

# Generate current timestamp
now = datetime.now()

# Helper function to generate random timestamps
def random_time():
    return (now - timedelta(minutes=random.randint(1, 120))).strftime("%b %d %H:%M:%S")

def random_date():
    return (now - timedelta(days=random.randint(0, 30))).strftime("%Y-%m-%d %H:%M:%S")

# **1. Default Syslog Folder Structure**
default_syslog_path = os.path.join(BASE_DIR, "var", "log", "syslog.log")
os.makedirs(os.path.dirname(default_syslog_path), exist_ok=True)

with open(default_syslog_path, "w") as f:
    for _ in range(50):
        log_entry = f"{random_time()} {random.choice(hosts)} {random.choice(processes)}[{random.randint(1000, 9999)}]: " \
                    f"System event triggered successfully."
        f.write(log_entry + "\n")

# **2. Host-Based Folder Structure**
for host in hosts:
    host_syslog_path = os.path.join(BASE_DIR, "var", "log", "syslog", host, "syslog.log")
    os.makedirs(os.path.dirname(host_syslog_path), exist_ok=True)

    with open(host_syslog_path, "w") as f:
        for _ in range(50):
            log_entry = f"{random_time()} {random.choice(protocols)}[{random.randint(1000, 9999)}]: " \
                        f"Routing event detected."
            f.write(log_entry + "\n")

# **3. Date-Based Folder Structure**
date_folder = now.strftime("%Y/%m/%d")
date_syslog_path = os.path.join(BASE_DIR, "var", "log", "syslog", date_folder, "syslog.log")
os.makedirs(os.path.dirname(date_syslog_path), exist_ok=True)

with open(date_syslog_path, "w") as f:
    for _ in range(50):
        log_entry = f"{random_date()} {random.choice(hosts)} {random.choice(firewall_actions)}: " \
                    f"Packet activity detected from {random.choice(src_ips)} to {random.choice(dst_ips)}:{random.choice(ports)}"
        f.write(log_entry + "\n")

# **4. Device-Type-Based Folder Structure**
device_types = ["firewall_device", "router_device", "switch_device"]
for device in device_types:
    device_syslog_path = os.path.join(BASE_DIR, "var", "log", "syslog", device, "syslog.log")
    os.makedirs(os.path.dirname(device_syslog_path), exist_ok=True)

    with open(device_syslog_path, "w") as f:
        for _ in range(50):
            log_entry = f"{random_time()} {random.choice(hosts)} {random.choice(vendors)}: " \
                        f"Security event - Detected traffic anomaly."
            f.write(log_entry + "\n")

# **5. Year/Month/Host-Based Folder Structure**
year_month_folder = now.strftime("%Y/%m")
for host in hosts:
    hybrid_syslog_path = os.path.join(BASE_DIR, "var", "log", "syslog", year_month_folder, host, "syslog.log")
    os.makedirs(os.path.dirname(hybrid_syslog_path), exist_ok=True)

    with open(hybrid_syslog_path, "w") as f:
        for _ in range(50):
            log_entry = f"{random_date()} LINK-3-UPDOWN: Interface {random.choice(interfaces)}, changed state to up."
            f.write(log_entry + "\n")

print(f"Sample syslog data generated at: {BASE_DIR}")
