import os
import re
import streamlit as st
import vt
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('VT_API_KEY')

st.set_page_config(page_title="Automated Threat Hunter", page_icon="🛡️", layout="wide")
st.title("🛡️ Automated Threat Hunter Dashboard")

st.sidebar.header("Configuration")
if api_key:
    st.sidebar.success("VirusTotal API Key Loaded")
else:
    st.sidebar.error("API Key Missing!")

st.subheader("1. Monitor Active Log Pipeline")

log_file_path = "logs/network_traffic.log"

if os.path.exists(log_file_path):
    st.info(f"📁 Target Log Detected: `{log_file_path}`")
    
    # Read and display the raw logs inside an expanding section
    with st.expander("View Raw Ingested Security Logs"):
        with open(log_file_path, "r") as f:
            log_data = f.read()
            st.text(log_data)
            
    # Execution Button
    if st.button("Analyze Logs for Threats 🚀"):
        # Regex to find all IP addresses in the log file
        ip_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
        found_ips = set(re.findall(ip_pattern, log_data)) # Using set() to remove duplicates
        
        st.subheader(f"2. Analysis Results ({len(found_ips)} Unique IPs Found)")
        
        client = vt.Client(api_key)
        progress_bar = st.progress(0)
        
        for index, ip in enumerate(found_ips):
            # Skip local internal networks
            if ip.startswith("192.168."):
                st.info(f"🏠 **INTERNAL:** {ip} is local traffic. Skipping external API check.")
                continue
                
            try:
                ip_obj = client.get_object(f"/ip_addresses/{ip}")
                stats = ip_obj.last_analysis_stats
                malicious_count = stats.get('malicious', 0)
                
                if malicious_count > 0:
                    st.error(f"🚨 **ALERT:** External IP `{ip}` is flagged as **MALICIOUS** by {malicious_count} engines.")
                else:
                    st.success(f"✅ **CLEAN:** External IP `{ip}` appears safe.")
            except Exception as e:
                st.warning(f"⚠️ **Could not analyze {ip}:** {e}")
                
            progress_bar.progress((index + 1) / len(found_ips))
            
        client.close()
        st.balloons()
else:
    st.error(f"Log file not found at `{log_file_path}`. Run the generator script first!")