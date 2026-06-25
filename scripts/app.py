import os
import streamlit as st
import vt
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv('VT_API_KEY')

# Page Configuration
st.set_page_config(page_title="Automated Threat Hunter", page_icon="🛡️", layout="wide")

st.title("🛡️ Automated Threat Hunter Dashboard")
st.markdown("Ingest network indicators and cross-reference with live VirusTotal Threat Intelligence.")

# Sidebar Configuration
st.sidebar.header("Configuration")
if api_key:
    st.sidebar.success("VirusTotal API Key Loaded Successfully")
else:
    st.sidebar.error("API Key Missing! Check your .env file.")

# Main Layout: Text input area for IPs
st.subheader("1. Ingest Network Logs")
ip_input = st.text_area(
    "Paste IP Addresses to analyze (one per line):", 
    value="8.8.8.8\n1.1.1.1\n185.196.8.50", 
    height=150
)

# Execution Button
if st.button("Run Threat Hunt 🚀"):
    if not api_key:
        st.error("Cannot proceed without a valid API key.")
    else:
        # Process the input text into a clean list of IPs
        ips = [ip.strip() for ip in ip_input.split("\n") if ip.strip()]
        
        st.subheader("2. Threat Intelligence Results")
        
        # Initialize VirusTotal Client
        client = vt.Client(api_key)
        
        # Create a progress bar for visual feedback
        progress_bar = st.progress(0)
        
        for index, ip in enumerate(ips):
            try:
                ip_obj = client.get_object(f"/ip_addresses/{ip}")
                stats = ip_obj.last_analysis_stats
                malicious_count = stats.get('malicious', 0)
                
                # Visual alerting based on risk level
                if malicious_count > 0:
                    st.error(f"🚨 **ALERT:** {ip} is flagged as **MALICIOUS** by {malicious_count} security engines.")
                else:
                    st.success(f"✅ **CLEAN:** {ip} appears safe.")
                    
            except Exception as e:
                st.warning(f"⚠️ **Could not analyze {ip}:** {e}")
            
            # Update the progress bar dynamically
            progress_bar.progress((index + 1) / len(ips))
            
        client.close()
        st.balloons() # Visual celebration on completion!