from __future__ import annotations

import json
from pathlib import Path

from src.agent import run_assessment

OUTPUT = Path("outputs/latest_assessment.json")


def main() -> None:
    assessment = run_assessment()
    payload = assessment.model_dump()

    OUTPUT.parent.mkdir(exist_ok=True)
    OUTPUT.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    print("\n=== AI CYBERSECURITY PROJECT MANAGER ===\n")
    print(assessment.executive_summary)
    print("\nRANKED RISKS")
    print("-" * 88)

    for risk in sorted(assessment.ranking, key=lambda x: x.rank):
        print(
            f"{risk.rank:>2}. {risk.risk_id} | {risk.priority:<8} | "
            f"baseline={risk.baseline_score:.2f} | {risk.title}"
        )
        print(f"    {risk.summary_reason}")

    print("\nTOP 3 REMEDIATION PLANS")
    print("=" * 88)

    for plan in assessment.top_three:
        print(f"\n{plan.risk_id}: {plan.title}")
        print(f"Likelihood:     {plan.likelihood_reason}")
        print(f"Business impact:{plan.business_impact_reason}")
        print(f"Exploitability: {plan.exploitability_reason}")
        print(f"Containment:    {plan.immediate_containment}")
        print(f"Total duration: {plan.estimated_total_duration}")
        for step in sorted(plan.remediation_steps, key=lambda x: x.order):
            print(
                f"  {step.order}. {step.action}\n"
                f"     Owner: {step.owner} | Effort: {step.effort}\n"
                f"     Note: {step.dependency_or_note}"
            )

    print(f"\nSaved structured output to {OUTPUT}")


if __name__ == "__main__":
    main()
