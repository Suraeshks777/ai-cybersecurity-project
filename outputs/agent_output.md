## Risk Ranking

1. **R6. Public cloud storage containing customer data**
2. **R1. No MFA on remote-access VPN**
3. **R2. Unpatched internet-facing servers**
4. **R7. Secrets stored in source code and CI/CD systems**
5. **R5. No offline or immutable backups**
6. **R3. Over-privileged administrator accounts**
7. **R8. Limited internal network segmentation**
8. **R10. Third-party access is not regularly reviewed**
9. **R4. EDR missing on some corporate endpoints**
10. **R9. Security logs are not centrally monitored**

## Top 3 Risk Analysis

### 1. R6. Public Cloud Storage Containing Customer Data

**Likelihood:** High. The data is directly exposed to the internet and may be discoverable through scanning or misconfiguration searches.

**Business Impact:** Critical. Potential customer-data disclosure, regulatory penalties, breach notification costs, reputational damage, and loss of customer trust.

**Exploitability:** Very high. If the container permits anonymous listing or download, no credentials or advanced skills may be required.

**Estimated Remediation Time:** Immediate containment within hours; full remediation in **1–2 weeks**.

**Remediation Steps:**

1. Disable public access immediately and preserve access logs for investigation.  
   **Effort:** 2–4 hours

2. Identify the exposed data, exposure duration, access activity, and affected customers.  
   **Effort:** 1–2 person-days

3. Rotate exposed access keys, signed URLs, and service credentials associated with the storage container.  
   **Effort:** 0.5–1 person-day

4. Implement least-privilege IAM, deny-public-access controls, encryption, and appropriate retention policies.  
   **Effort:** 1–3 person-days

5. Scan other cloud storage resources for similar exposure.  
   **Effort:** 2–4 person-days

6. Complete legal/privacy assessment and implement continuous cloud-configuration monitoring.  
   **Effort:** 2–5 person-days

---

### 2. R1. No MFA on Remote-Access VPN

**Likelihood:** High. Passwords can be stolen through phishing, password reuse, credential stuffing, or malware.

**Business Impact:** High. A compromised VPN account could provide direct internal access, enable ransomware deployment, data theft, and lateral movement.

**Exploitability:** High. Attackers can automate password attacks or use harvested credentials. VPN access is often an attractive initial-access target.

**Estimated Remediation Time:** **2–4 weeks**, depending on VPN and identity-provider integration.

**Remediation Steps:**

1. Inventory VPN users, contractors, authentication methods, and emergency access accounts.  
   **Effort:** 1–2 person-days

2. Configure MFA integration with the corporate identity provider and test with IT users.  
   **Effort:** 2–4 person-days

3. Pilot MFA with a small employee and contractor group; resolve compatibility and recovery issues.  
   **Effort:** 2–3 person-days

4. Enforce MFA for all VPN users and disable password-only access.  
   **Effort:** 1–3 person-days

5. Review and remove inactive accounts; require approval and expiration dates for contractor access.  
   **Effort:** 1–2 person-days

6. Monitor VPN authentication logs and investigate failed-login spikes or unusual locations.  
   **Effort:** 1–2 person-days

---

### 3. R2. Unpatched Internet-Facing Servers

**Likelihood:** High. Public-facing systems are continuously scanned, and critical vulnerabilities are frequently weaponized.

**Business Impact:** High to critical. Exploitation could result in web-shell installation, data theft, service disruption, ransomware, or compromise of internal systems.

**Exploitability:** High. The systems are internet-facing, more than 45 days behind on critical patches, and may be vulnerable to publicly documented exploits.

**Estimated Remediation Time:** **1–2 weeks** for the initial backlog; ongoing patch compliance should be established afterward.

**Remediation Steps:**

1. Validate the server inventory, operating systems, exposed services, vulnerabilities, and available patches.  
   **Effort:** 1 person-day

2. Apply emergency compensating controls, such as restricting access through a firewall or WAF, where immediate patching is not possible.  
   **Effort:** 0.5–1 person-day

3. Back up configurations and verify recovery procedures before patching.  
   **Effort:** 1–2 person-days

4. Test and deploy critical patches, prioritizing internet-facing services and known exploited vulnerabilities.  
   **Effort:** 2–5 person-days

5. Conduct vulnerability rescanning and review logs for signs of prior exploitation.  
   **Effort:** 1–2 person-days

6. Establish a patching SLA, maintenance schedule, exception process, and executive reporting.  
   **Effort:** 1–2 person-days