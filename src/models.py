from typing import Literal
from pydantic import BaseModel, Field


class RankedRisk(BaseModel):
    rank: int = Field(ge=1, le=10)
    risk_id: str
    title: str
    priority: Literal["Critical", "High", "Medium", "Low"]
    baseline_score: float = Field(ge=1.0, le=5.0)
    summary_reason: str


class RemediationStep(BaseModel):
    order: int = Field(ge=1)
    action: str
    owner: str
    effort: str
    dependency_or_note: str


class TopRiskPlan(BaseModel):
    risk_id: str
    title: str
    likelihood_reason: str
    business_impact_reason: str
    exploitability_reason: str
    immediate_containment: str
    estimated_total_duration: str
    remediation_steps: list[RemediationStep]


class CyberRiskAssessment(BaseModel):
    executive_summary: str
    ranking: list[RankedRisk]
    top_three: list[TopRiskPlan]
    assumptions: list[str]
