import json
import os
from pathlib import Path

import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

RISK_FILE = Path("data/risks.json")
OUTPUT_FILE = Path("outputs/agent_output.md")


def load_risks():
    with open(RISK_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def build_prompt(risks):
    risk_text = ""

    for risk in risks:
        risk_text += (
            f"{risk['id']}. {risk['risk']}\n"
            f"Context: {risk['context']}\n\n"
        )

    return f"""
You are a Cybersecurity Project Manager for a mid-size company.

Review these 10 cybersecurity risks:

{risk_text}

Tasks:

1. Rank all 10 risks from highest to lowest priority.

2. For the top 3 risks, explain:
- likelihood
- business impact
- exploitability

3. Estimate remediation time for each top 3 risk.

4. Give remediation steps in order.

5. Include an effort estimate for every step.

Keep the response concise and practical.

Use this format:

## Risk Ranking

1. ...
2. ...
3. ...
...
10. ...

## Top 3 Risk Analysis

### 1. Risk Name

Likelihood:
...

Business Impact:
...

Exploitability:
...

Estimated Remediation Time:
...

Remediation Steps:

1. ...
Effort: ...

2. ...
Effort: ...

Repeat for the remaining top risks.
"""


def run_agent(risks):
    client = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY")
    )

    response = client.responses.create(
        model=os.getenv(
            "OPENAI_MODEL",
            "gpt-5.6-luna"
        ),
        input=build_prompt(risks),
    )

    return response.output_text


st.title("AI Cybersecurity Project Manager")

st.write(
    "This prototype ranks cybersecurity risks and creates "
    "remediation plans for the top three."
)

risks = load_risks()

st.subheader("Risk Register")

st.dataframe(
    [
        {
            "ID": risk["id"],
            "Risk": risk["risk"],
            "Context": risk["context"],
        }
        for risk in risks
    ],
    hide_index=True,
)


if st.button("Analyze Risks"):

    if not os.getenv("OPENAI_API_KEY"):
        st.write("OPENAI_API_KEY is missing.")

    else:

        try:

            result = run_agent(risks)

            OUTPUT_FILE.parent.mkdir(
                exist_ok=True
            )

            OUTPUT_FILE.write_text(
                result,
                encoding="utf-8",
            )

            st.subheader("Agent Output")

            st.markdown(result)

        except Exception as error:

            st.write(
                f"Error: {error}"
            )