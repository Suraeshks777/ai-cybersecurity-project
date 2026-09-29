## Risk Ranking

1. **R6. Public cloud storage containing customer data**
2. **R2. Unpatched internet-facing servers**
3. **R1. No MFA on remote-access VPN**
4. **R7. Secrets stored in source code and CI/CD systems**
5. **R5. No offline or immutable backups**
6. **R3. Over-privileged administrator accounts**
7. **R10. Third-party access is not regularly reviewed**
8. **R4. EDR missing on some corporate endpoints**
9. **R9. Security logs are not centrally monitored**
10. **R8. Limited internal network segmentation**

## Top 3 Risk Analysis

### 1. Public Cloud Storage Containing Customer Data

**Likelihood:** High. The storage container is currently publicly accessible and can be discovered or accessed through automated scanning.

**Business Impact:** Critical. Potential customer-data breach, regulatory notification, contractual penalties, loss of customer trust, and legal or reputational damage.

**Exploitability:** Very high. Exploitation may require only a publicly accessible URL or cloud API request, depending on the container configuration.

**Estimated Remediation Time:** Immediate exposure reduction within **1–4 hours**; full investigation and remediation within **3–5 business days**.

**Remediation Steps:**

1. Disable public access and restrict the container to approved identities and networks.  
   **Effort:** 1–2 hours

2. Preserve access logs and determine what data was exposed and for how long.  
   **Effort:** 4–8 hours

3. Review cloud permissions, access policies, sharing links, and service accounts; remove unnecessary access.  
   **Effort:** 4–8 hours

4. Assess whether data was accessed or exfiltrated and escalate to legal, privacy, and incident response teams as required.  
   **Effort:** 8–24 hours

5. Rotate exposed credentials and implement preventive controls, including public-access policies, configuration monitoring, and alerting.  
   **Effort:** 1–3 business days

---

### 2. Unpatched Internet-Facing Servers

**Likelihood:** High. Public-facing systems more than 45 days behind on critical patches are likely targets for automated exploitation and vulnerability scanning.

**Business Impact:** Critical. Successful exploitation could result in ransomware, data theft, service disruption, unauthorized access, or use of the servers as a foothold into the internal network.

**Exploitability:** High. The systems are internet-facing, and critical vulnerabilities often have public proof-of-concept code or active exploitation.

**Estimated Remediation Time:** Emergency patching within **24–48 hours**; complete validation and process improvements within **1–2 weeks**.

**Remediation Steps:**

1. Identify the missing patches, affected services, exploit status, and system owners.  
   **Effort:** 2–4 hours

2. Apply critical patches using an emergency change process, beginning with the most exposed or vulnerable server.  
   **Effort:** 4–8 hours

3. If immediate patching is not possible, apply temporary controls such as restricting access, disabling vulnerable services, or adding WAF/IPS rules.  
   **Effort:** 2–6 hours

4. Validate service functionality, rescan for vulnerabilities, and review logs for indicators of compromise.  
   **Effort:** 4–8 hours

5. Establish patch SLAs, automated vulnerability scanning, maintenance ownership, and exception tracking.  
   **Effort:** 1–2 weeks

---

### 3. No MFA on Remote-Access VPN

**Likelihood:** High. Passwords can be stolen through phishing, credential stuffing, malware, or reuse from third-party breaches.

**Business Impact:** High to critical. A compromised VPN account could provide direct access to internal systems, sensitive data, and administrative pathways, potentially enabling ransomware or major data theft.

**Exploitability:** High. An attacker needs only valid credentials and VPN access; no endpoint compromise may be required.

**Estimated Remediation Time:** Initial protection within **3–5 business days**; full deployment and cleanup within **1–2 weeks**.

**Remediation Steps:**

1. Select and configure the MFA method integrated with the VPN and identity provider.  
   **Effort:** 4–8 hours

2. Enroll employees and contractors, prioritize administrators and remote-access users, and define support procedures.  
   **Effort:** 2–5 business days

3. Enforce MFA for all VPN users and disable password-only and legacy authentication methods.  
   **Effort:** 2–4 hours

4. Secure and test break-glass accounts, recovery codes, and help-desk identity verification procedures.  
   **Effort:** 4–8 hours

5. Review VPN accounts, disable inactive or unnecessary accounts, rotate compromised credentials, and monitor failed MFA and VPN logins.  
   **Effort:** 1–2 business days