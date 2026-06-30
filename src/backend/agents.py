from src.backend.tools import verify_email_domain, inspect_file_attachment

class IncidentResponseAgent:
    def __init__(self, model_name: str = "Llama-3"):
        self.model_name = model_name
        print(f"[⚙] Initializing Threat Investigation Agent using engine: {self.model_name}")

    def evaluate_phishing_incident(self, event_type: str, sender: str, subject: str, attachment: str = None) -> dict:
        """
        Executes forensic data gathering tools and forms an analytical remediation profile.
        """
        # 1. Coordinate investigation tools to gather technical context data
        domain_report = verify_email_domain(sender)
        file_report = inspect_file_attachment(attachment)
        
        # 2. Determine an aggregate priority metric based on tool outputs
        max_tool_score = max(domain_report.get("risk_score", 0), file_report.get("risk_score", 0))
        
        if max_tool_score >= 80:
            calculated_severity = "High"
            containment_action = (
                f"CRITICAL: Isolate targeted user workspace. Block external inbound SMTP traffic from domain "
                f"'{domain_report.get('target_domain')}'. Delete attachment '{attachment}' from email caches."
            )
        elif max_tool_score >= 40:
            calculated_severity = "Medium"
            containment_action = "WARNING: Flag target mailbox account for active credential monitoring. Route attachment to inspection sandbox."
        else:
            calculated_severity = "Low"
            containment_action = "INFO: Log transaction to telemetry database. No immediate network isolation necessary."

        # 3. Compile the structural analytical summary payload (Later sent to your frontend dashboard)
        analysis_summary = (
            f"Automated AI threat intelligence scan completed for vector matching '{event_type}'. "
            f"Sender assessment marked as suspicious: {domain_report.get('flagged_as_suspicious')}. "
            f"Attachment compliance check marked unsafe: {file_report.get('flagged_extension')}."
        )

        return {
            "threat_assessment": analysis_summary,
            "calculated_severity": calculated_severity,
            "remediation_playbook": containment_action,
            "forensics": {
                "domain_lookup": domain_report,
                "file_lookup": file_report
            }
        }
