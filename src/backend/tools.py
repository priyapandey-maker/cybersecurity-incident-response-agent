import re

def verify_email_domain(sender_email: str) -> dict:
    """
    Analyzes the domain of an incoming email address to identify known spoofing patterns.
    """
    try:
        # Extract domain from email address string
        domain = sender_email.split('@')[-1].lower() if '@' in sender_email else sender_email
        
        # Simple local blocklist array for common look-alike phishing variations
        suspicious_keywords = ["amazon-support", "paypaI-security", "fakebank", "verification"]
        
        is_suspicious = any(keyword in domain for keyword in suspicious_keywords)
        
        return {
            "target_domain": domain,
            "flagged_as_suspicious": is_suspicious,
            "risk_score": 85 if is_suspicious else 10,
            "enrichment_source": "Internal Domain Reputation Engine"
        }
    except Exception as e:
        return {"error": f"Failed to parse domain metrics: {str(e)}"}

def inspect_file_attachment(file_name: str) -> dict:
    """
    Evaluates file attachment extensions for unsafe structures (like double extensions or executables).
    """
    if not file_name:
        return {"file_present": False, "verdict": "Clean", "risk_score": 0}
        
    unsafe_extensions = [".zip", ".exe", ".scr", ".bat", ".vbs"]
    file_lower = file_name.lower()
    
    # Check if file matches high-risk execution signatures
    is_unsafe = any(file_lower.endswith(ext) for ext in unsafe_extensions)
    
    return {
        "file_present": True,
        "file_name": file_name,
        "flagged_extension": is_unsafe,
        "risk_score": 90 if is_unsafe else 15,
        "verdict": "Suspicious Activity Detected" if is_unsafe else "Passed Extension Scan"
    }
