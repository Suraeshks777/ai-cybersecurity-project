# AI Cybersecurity Project

This project is a simple AI-powered cybersecurity risk prioritization prototype.

The application takes 10 cybersecurity risks for a fictional mid-size company and asks an AI model acting as a Cybersecurity Project Manager to:

1. Rank all 10 risks.
2. Identify the top 3.
3. Explain the top 3 based on:
   - likelihood
   - business impact
   - exploitability
4. Estimate remediation time.
5. Create ordered remediation steps.
6. Estimate effort for each remediation step.

## Architecture

The prototype intentionally uses a simple architecture:

10 Cybersecurity Risks
        |
   risks.json
        |
     Python
        |
   OpenAI API
        |
AI Cybersecurity Project Manager
        |
Risk Ranking + Remediation Plan
        |
 Streamlit UI + Markdown Output


## Technology

- Python
- OpenAI API
- Streamlit
- JSON
