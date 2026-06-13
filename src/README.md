# Source Code (`src/`)

This directory houses the codebase for the AI Agent for Cybersecurity Incident Response.

## Architecture & Modules

The application is structured into the following modular packages:

- **`agent/`**: The core LLM planning and reasoning loop (e.g., ReAct loop, tool-use orchestration, prompt templates, and conversational interface).
- **`tools/`**: Interfaces for the AI agent to interact with external security systems:
  - Network analyzers (e.g., WHOIS lookup, DNS resolution, Shodan querying).
  - Threat Intel APIs (e.g., VirusTotal, AlienVault OTX).
  - SIEM/Log query interfaces (e.g., Elasticsearch, Splunk).
  - Containment actions (e.g., blocking an IP via firewall/AWS SG, disabling a compromised user account).
- **`playbooks/`**: Pre-defined incident response playbooks (e.g., Ransomware outbreak containment, Phishing analysis, SSH brute force response) represented as structured executable code or state machines.
- **`utils/`**: Shared helper utilities (e.g., log parsers, encryption utilities, configuration management).

## Development Setup

1. Configure your environment variables in `.env` (refer to `.env.example`).
2. Run unit tests using:
   ```bash
   pytest tests/
   ```
