import os
import random
from datetime import datetime, timedelta

# Create the logs directory if it doesn't exist
os.makedirs('logs', exist_ok=True)

# Sample pools for generating realistic data
users = ["j.medrano", "a.smith", "m.jones", "admin", "system_svc"]
computers = ["DESKTOP-WK01", "DESKTOP-WK02", "SERVER-DC01", "LAPTOP-HR04"]

# A pool of clean and highly suspicious IPs
ip_pool = [
    "1.1.1.1",       # Clean (Cloudflare)
    "8.8.8.8",       # Clean (Google)
    "185.196.8.50",  # Malicious (Flagged on VT)
    "192.168.1.50",  # Clean Internal
    "142.250.190.46",# Clean (Google)
    "45.227.254.10", # Malicious (Known scanning/brute force)
]

def generate_mock_logs(filename="logs/network_traffic.log", entries=20):
    start_time = datetime.now() - timedelta(hours=1)
    
    with open(filename, "w") as file:
        print(f"--- Generating {entries} Realistic Security Events ---")
        
        for i in range(entries):
            # Advance time slightly for each log entry
            timestamp = (start_time + timedelta(seconds=random.randint(10, 180))).strftime("%Y-%m-%d %H:%M:%S")
            user = random.choice(users)
            computer = random.choice(computers)
            destination_ip = random.choice(ip_pool)
            port = random.choice([80, 443, 22, 3389, 8080])
            
            # Construct a realistic corporate proxy/firewall log line
            log_line = f"{timestamp} | Src:{computer} | User:{user} | Dst:{destination_ip}:{port} | Action:ALLOW\n"
            file.write(log_line)
            
    print(f"[+] Complete! Messy log file saved to: {filename}")

if __name__ == "__main__":
    generate_mock_logs()