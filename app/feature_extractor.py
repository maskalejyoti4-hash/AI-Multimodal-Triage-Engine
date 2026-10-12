import asyncio
from typing import Dict, Any, List

class FeatureExtractor:
    """Asynchronous feature extraction for unstructured support data."""
    
    URGENT_KEYWORDS = ["outage", "broken", "fraud", "security", "urgent", "down", "crash"]

    @classmethod
    async def extract_features(cls, text: str, attachment_type: str | None) -> Dict[str, Any]:
        # Simulate non-blocking asynchronous execution/feature parsing latency
        await asyncio.sleep(0.01)

        text_lower = text.lower()
        contains_urgent_keyword = any(kw in text_lower for kw in cls.URGENT_KEYWORDS)
        has_attachment = attachment_type is not None

        detected_features: List[str] = []
        if contains_urgent_keyword:
            detected_features.append("urgent_keyword_detected")
        if has_attachment:
            detected_features.append(f"multimodal_attachment_{attachment_type}")

        return {
            "is_urgent_keyword": contains_urgent_keyword,
            "has_attachment": has_attachment,
            "detected_features": detected_features,
            "text_length": len(text)
        }