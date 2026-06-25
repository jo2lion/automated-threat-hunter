# Automated Threat Hunter (Real-Time Log Analysis Pipeline)

## Project Overview
This project simulates a live Security Operations Center (SOC) workflow by automating the triage of suspicious network traffic. The script ingests local network logs, extracts IP addresses, and correlates them against real-world threat intelligence via the VirusTotal API.

## Core Features
* **Secure Credential Management:** Utilizes environment variables (`.env`) to protect active API keys.
* **Automated Log Parsing:** Sanitizes and processes raw, messy log data automatically.
* **Threat Intelligence Correlation:** Cross-references active indicators of compromise (IOCs) with global security engines.

## How It Works
1. The system reads network connection events from a local file (`logs/suspicious_ips.txt`).
2. The Python script extracts the endpoints and requests live data from VirusTotal.
3. High-risk indicators trigger an immediate alert flag for incident responders.
