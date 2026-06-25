# Automated Threat Hunter (Real-Time Threat Intelligence Dashboard)

## Project Overview
This project delivers a full-stack Security Operations Center (SOC) workflow application that automates the triage of suspicious network traffic. Built using Python and Streamlit, the application transforms raw log data into an interactive, real-time threat intelligence dashboard backed by the live VirusTotal API.

## Core Features
* **Interactive Frontend Dashboard:** Built with Streamlit to enable security analysts to paste raw network indicators directly into a web UI.
* **Secure Credential Management:** Utilizes environment variables via `python-dotenv` to isolate production API keys from version control.
* **Live Threat Triage Pipelines:** Features dynamic visual feedback (progress tracking and severity-based alerting) based on real-world reputation scores.

## Architecture & Workflow
1. **Ingestion:** The analyst enters a list of suspected indicators of compromise (IOCs) into the UI text interface.
2. **Analysis:** The backend pipeline strips whitespace, validates formats, and initiates concurrent queries to the VirusTotal REST API.
3. **Visualization:** High-risk vectors trigger immediate visual warning blocks detailing engine detection counts, facilitating rapid incident response.
