from __future__ import annotations

import json
import os
from pathlib import Path

from agents import Agent, Runner
from agents.decorators import tool
from dotenv import load_dotenv

from .models import CyberRiskAssessment
from .scoring import score_risk_register

load_dotenv()

BASE_DIR = Path(__file__).resolve().parents[1]
RISK_FILE = BASE_DIR / "data" / "risks.json"


@tool
def get_scored_risk_register() -> str:
    """Retrieve the 10 company cybersecurity risks with transparent baseline scores.

    The score is a decision aid, not an automatic final ranking. It uses:
    likelihood 30%, business impact 30%, exploitability 25%, exposure 15%.
    Every factor is scored from 1 (low) to 5 (very high).
    """
    risks = json.loads(RISK_FILE.read_text(encoding="utf-8"))
    return json.dumps(score_risk_register(risks), indent=2)


INSTRUCTIONS = """
You are an AI Cybersecurity Project Manager for a mid-size company.

Your job is to turn a cyber risk register into an actionable remediation portfolio.

MANDATORY PROCESS
1. Call get_scored_risk_register before making any decision.
2. Rank all 10 risks from 1 through 10.
3. Treat the deterministic baseline score as an anchor, not as unquestionable truth.
   You may change the baseline order when business context justifies it, but explain
   the final prioritization in summary_reason.
4. For the final top 3, separately explain:
   - likelihood,
   - business impact,
   - exploitability.
5. For each top-3 risk, estimate a realistic elapsed remediation duration.
6. For each top-3 risk, create ordered remediation steps with:
   - responsible owner or team,
   - hands-on effort for that step,
   - dependency or implementation note.
7. Include a short immediate containment action for every top-3 risk.

DECISION PRINCIPLES
- Prioritize externally exposed, easily exploitable conditions that can lead to
  material compromise or sensitive-data loss.
- Consider attack-path reduction, blast radius, recoverability, and time-to-exploit.
- Do not invent vulnerabilities, assets, controls, or regulatory obligations that
  are not present in the risk register.
- Use realistic ranges instead of false precision.
- Distinguish hands-on engineering effort from elapsed remediation duration.
- Remediation should be practical for a mid-size company with a small security team.
- Top-three plans must correspond exactly to risks ranked 1, 2, and 3.
- The ranking must contain exactly 10 unique risks and top_three exactly 3 unique risks.

OUTPUT STYLE
Be concise, defensible, and implementation-oriented. The result will be reviewed
by a cybersecurity consulting founder, so make tradeoffs and sequencing clear.
"""


def build_agent() -> Agent:
    model = os.getenv("OPENAI_MODEL", "gpt-5.6-luna")
    return Agent(
        name="Cybersecurity Project Manager",
        instructions=INSTRUCTIONS,
        model=model,
        tools=[get_scored_risk_register],
        output_type=CyberRiskAssessment,
    )


def run_assessment() -> CyberRiskAssessment:
    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError(
            "OPENAI_API_KEY is not set. Copy .env.example to .env and add your API key."
        )

    agent = build_agent()
    result = Runner.run_sync(
        agent,
        (
            "Assess the current cybersecurity risk register. Produce the complete "
            "ranked portfolio and detailed remediation project plan for the top 3."
        ),
        max_turns=6,
    )

    assessment = result.final_output
    if not isinstance(assessment, CyberRiskAssessment):
        raise RuntimeError("Agent returned an unexpected output type.")

    validate_assessment(assessment)
    return assessment


def validate_assessment(assessment: CyberRiskAssessment) -> None:
    """Fail loudly if the LLM violates core assignment constraints."""
    if len(assessment.ranking) != 10:
        raise ValueError("Expected exactly 10 ranked risks.")
    if len(assessment.top_three) != 3:
        raise ValueError("Expected exactly 3 detailed remediation plans.")

    ranked_ids = [risk.risk_id for risk in assessment.ranking]
    if len(set(ranked_ids)) != 10:
        raise ValueError("Ranking contains duplicate risk IDs.")

    ranks = sorted(risk.rank for risk in assessment.ranking)
    if ranks != list(range(1, 11)):
        raise ValueError("Ranks must be exactly 1 through 10.")

    top_ids = [risk.risk_id for risk in sorted(assessment.ranking, key=lambda x: x.rank)[:3]]
    plan_ids = [plan.risk_id for plan in assessment.top_three]
    if set(top_ids) != set(plan_ids):
        raise ValueError("Top-three remediation plans do not match ranks 1-3.")
