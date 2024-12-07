import random
import logging
import time
from datetime import datetime

# Define log file path for Windows (e.g., in C:\temp\sample-data.log)
log_file = r'C:\tmp\sample-data.log'

# Set up the logger with log level included in the format
logging.basicConfig(
    filename=log_file,
    level=logging.DEBUG,  # Captures all log levels from DEBUG and higher
    format='%(asctime)s %(levelname)s %(message)s',  # Include log level in the format
    datefmt='%b %d %H:%M:%S'
)

# Function to generate realistic log entries
def generate_log_entry():
    log_level = random.choices(
        ['INFO', 'DEBUG', 'WARNING', 'ERROR', 'CRITICAL'],
        weights=[60, 20, 10, 8, 2],
        k=1
    )[0]
    
    # Generate random log messages based on log level
    if log_level == 'INFO':
        message = f"System health check: CPU usage at {random.randint(10, 50)}%."
    elif log_level == 'DEBUG':
        message = f"Debugging connection to database: Connection established on port 5432."
    elif log_level == 'WARNING':
        message = f"Disk space running low on C:\\: {random.randint(80, 95)}% used."
    elif log_level == 'ERROR':
        message = f"Application 'webserver' failed to start: Port 80 already in use."
    elif log_level == 'CRITICAL':
        message = f"Unauthorized login attempt detected from IP {random.randint(192, 223)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}."
    
    # Log the message at the appropriate level
    if log_level == 'INFO':
        logging.info(message)
    elif log_level == 'DEBUG':
        logging.debug(message)
    elif log_level == 'WARNING':
        logging.warning(message)
    elif log_level == 'ERROR':
        logging.error(message)
    elif log_level == 'CRITICAL':
        logging.critical(message)

# Generate logs
for _ in range(10000):  # Generate 100 log entries
    generate_log_entry()
    time.sleep(0.1)  # Slight delay to simulate real-time logging

print(f"Logs written to {log_file}")
