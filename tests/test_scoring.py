import json
from pathlib import Path

from src.scoring import calculate_baseline_score, score_risk_register


def load_risks():
    path = Path(__file__).resolve().parents[1] / "data" / "risks.json"
    return json.loads(path.read_text(encoding="utf-8"))


def test_exactly_ten_unique_risks():
    risks = load_risks()
    assert len(risks) == 10
    assert len({r["risk_id"] for r in risks}) == 10


def test_score_is_in_expected_range():
    for risk in load_risks():
        score = calculate_baseline_score(risk)
        assert 1.0 <= score <= 5.0


def test_known_high_exposure_risks_rank_near_top():
    ranked = score_risk_register(load_risks())
    top_three = {r["risk_id"] for r in ranked[:3]}
    assert {"R-01", "R-02", "R-06"} == top_three
