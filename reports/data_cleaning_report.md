# Data Cleaning Report

## Project

AI Agent for Cybersecurity Incident Response

## Task Objective

The objective of this task was to improve data quality by validating cybersecurity event data, removing inconsistencies, and ensuring that the dataset is suitable for storage, analysis, and future model development.

---

## Dataset Overview

The project uses simulated cybersecurity incident data for the following attack categories:

1. Brute Force Attacks
2. Phishing Attacks
3. Malware Detection Events

Data is stored in JSON format and later processed for database storage and dashboard visualization.

---

## Data Validation Checks Performed

### 1. Missing Value Detection

The dataset was checked for:

* Missing usernames
* Missing IP addresses
* Missing severity values
* Missing event types

Records with critical missing information were corrected or removed.

---

### 2. Duplicate Record Detection

Duplicate cybersecurity events were identified and removed to prevent redundant incident generation.

Examples:

* Duplicate failed login attempts
* Repeated phishing alerts
* Repeated malware detection events

---

### 3. Severity Standardization

Severity labels were standardized to ensure consistency across all datasets.

Before:

* HIGH
* high
* High
* medium
* MEDIUM

After:

* High
* Medium
* Low

---

### 4. Event Type Validation

Event names were normalized to maintain consistent formatting.

Examples:

Before:

* Failed_Login
* failed login
* FAILED_LOGIN

After:

* failed_login

---

### 5. Data Format Verification

The following fields were verified:

| Field      | Validation            |
| ---------- | --------------------- |
| event_type | String                |
| username   | String                |
| ip_address | Valid IP Format       |
| severity   | Low / Medium / High   |
| threat     | Valid Threat Category |

---

## Cleaning Summary

### Before Cleaning

* Inconsistent severity labels
* Duplicate event entries
* Missing field values
* Non-standard event naming

### After Cleaning

* Standardized severity values
* Duplicate records removed
* Missing values handled
* Event names normalized
* Dataset validated for storage

---

## Output Files

### Raw Datasets

* data/brute_force.json
* data/phishing.json
* data/malware.json

### Cleaned Datasets

* data/brute_force_cleaned.json
* data/phishing_cleaned.json
* data/malware_cleaned.json

---

## Result

The cleaned cybersecurity datasets are now consistent, structured, and ready for:

* SQLite database storage
* Incident analysis
* Dashboard visualization
* Future AI model development

Data quality checks were completed successfully.
