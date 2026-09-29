# AI Cybersecurity Project

A simple AI prototype that reviews cybersecurity risks for a mid-size company and creates a prioritized remediation plan.

## What It Does

The application takes 10 cybersecurity risks and asks an AI model acting as a Cybersecurity Project Manager to:

1. Rank all 10 risks from highest to lowest priority.
2. Explain why the top 3 are the most important based on:
   - likelihood
   - business impact
   - exploitability
3. Estimate remediation time for each top risk.
4. Create ordered remediation steps.
5. Estimate the effort required for each step.

## Tech Used

- Python
- OpenAI API
- Streamlit
- JSON