# Cybersecurity Incident Dataset

This folder contains synthetic cybersecurity events used for testing the AI Incident Response System.

## Files

### brute_force.json
Contains failed login events used to simulate brute force attacks.

Fields:
- event_type
- username
- ip_address
- attempt_count
- severity

### phishing.json
Contains phishing email events.

Fields:
- event_type
- sender
- subject
- attachment
- severity

### malware.json
Contains suspicious file upload events.

Fields:
- event_type
- filename
- severity

## Note

All datasets are synthetic and created for educational purposes only.


# Data Directory

This directory is designated for datasets, raw logs, security reports, and parsed telemetry used by the Cybersecurity Incident Response AI Agent.

## Subdirectory Contents

- **`raw/`**: Unprocessed log files (e.g., Syslog, Windows Event Logs, AWS CloudTrail, Zeek/Bro connection logs) and raw PCAP files.
- **`processed/`**: Normalized and cleaned log events formatted (e.g., JSON or CSV) for agent ingestion.
- **`threat_intel/`**: IOC (Indicators of Compromise) lists, IP reputation databases, and vulnerability feeds (e.g., CVE lists, MISP exports).

## Guidelines

- **Sensitive Data**: Avoid committing actual production data, PII (Personally Identifiable Information), or plaintext credentials. Use synthetic or sanitized logs for testing.
- **Large Files**: Avoid committing files larger than 50MB directly to Git. Consider utilizing Git LFS (Large File Storage) or external cloud buckets if large PCAP files are required.
