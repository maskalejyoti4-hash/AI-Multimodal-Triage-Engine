from app.schemas import PriorityEnum
from typing import Dict, Any, Tuple

class DecisionEngine:
    """Evaluates features and routes tickets to appropriate support queues."""

    @staticmethod
    def evaluate(features: Dict[str, Any]) -> Tuple[PriorityEnum, str, float]:
        score = 0.0

        if features.get("is_urgent_keyword"):
            score += 0.6
        if features.get("has_attachment"):
            score += 0.2
        if features.get("text_length", 0) > 300:
            score += 0.2

        if score >= 0.6:
            priority = PriorityEnum.URGENT
            queue = "Tier-3-Emergency-Support"
        elif score >= 0.4:
            priority = PriorityEnum.HIGH
            queue = "Tier-2-Technical-Support"
        elif score >= 0.2:
            priority = PriorityEnum.MEDIUM
            queue = "Tier-1-General-Support"
        else:
            priority = PriorityEnum.LOW
            queue = "Automated-Self-Service"

        return priority, queue, round(score, 2)