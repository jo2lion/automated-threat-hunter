import os
import vt
from dotenv import load_dotenv

# Load settings
load_dotenv()
client = vt.Client(os.getenv('VT_API_KEY'))

def hunt_threats(file_path):
    # Open and read the log file
    with open(file_path, 'r') as file:
        ips = file.readlines()
    
    print(f"--- Starting Threat Hunt on {len(ips)} IPs ---")
    
    for ip in ips:
        ip = ip.strip() # Clean up whitespace
        if not ip: continue
        
        try:
            # Query VirusTotal for the IP address
            ip_obj = client.get_object(f"/ip_addresses/{ip}")
            stats = ip_obj.last_analysis_stats
            
            # Check if any engines flagged it as malicious
            if stats['malicious'] > 0:
                print(f"[!] ALERT: {ip} is flagged as MALICIOUS by {stats['malicious']} engines!")
            else:
                print(f"[+] {ip} appears safe.")
                
        except Exception as e:
            print(f"[-] Could not analyze {ip}: {e}")

    client.close()

# Run the function
hunt_threats('logs/suspicious_ips.txt')