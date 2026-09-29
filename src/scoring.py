from __future__ import annotations

from typing import Any

WEIGHTS = {
    "likelihood": 0.30,
    "business_impact": 0.30,
    "exploitability": 0.25,
    "exposure": 0.15,
}


def calculate_baseline_score(risk: dict[str, Any]) -> float:
    """Return a transparent 1-5 weighted risk score."""
    score = sum(float(risk[key]) * weight for key, weight in WEIGHTS.items())
    return round(score, 2)


def score_risk_register(risks: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Add baseline_score and baseline_rank to each risk."""
    scored = []
    for risk in risks:
        row = dict(risk)
        row["baseline_score"] = calculate_baseline_score(risk)
        scored.append(row)

    scored.sort(key=lambda x: x["baseline_score"], reverse=True)
    for rank, risk in enumerate(scored, start=1):
        risk["baseline_rank"] = rank
    return scored
