# Automated Threat Hunter (Real-Time Threat Intelligence Dashboard)

## Project Overview
This project delivers a full-stack Security Operations Center (SOC) workflow application that automates the triage of suspicious network traffic. Built using Python and Streamlit, the application transforms raw log data into an interactive, real-time threat intelligence dashboard backed by the live VirusTotal API.

## Core Features
* **Interactive Frontend Dashboard:** Built with Streamlit to enable security analysts to paste raw network indicators directly into a web UI.
* **Secure Credential Management:** Utilizes environment variables via `python-dotenv` to isolate production API keys from version control.
* **Live Threat Triage Pipelines:** Features dynamic visual feedback (progress tracking and severity-based alerting) based on real-world reputation scores.

## Architecture & Production Workflow
1. **Data Simulation (`scripts/log_generator.py`):** Simulates a corporate firewall or proxy feed, streaming multi-vector records with realistic timestamps, hostnames, user scopes, and destination sockets.
2. **Regex Parsing & Ingestion (`scripts/app.py`):** Uses Python's regular expressions (`re`) to dynamically extract indicators of compromise (IOCs) from unstructured textual logging formats while utilizing a `set()` data structure to eliminate processing duplication.
3. **Traffic Triage:** Intelligently isolates local subnets (`192.168.x.x`) via string analysis to preserve third-party API quotas before querying the VirusTotal REST API for external reputational risk.
4. **Visual Analysis:** Streamlit interactive layer surfaces clean data matrices alongside high-visibility alerting arrays for immediate incident response.
