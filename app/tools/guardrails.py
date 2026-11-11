import re
from typing import Tuple, List

# Patterns indicative of unrealistic or overly vague requests
IMPOSSIBLE_TIME_PATTERNS = [
    r"\btomorrow\b",
    r"\bby tomorrow\b",
    r"\bin 24 hours\b",
    r"\bovernight\b",
    r"\binstant(ly)?\b"
]

ZERO_BUDGET_EXTREME_PROFIT = [
    r"(\$0|zero|no)\s*(budget|money|cost).*profitable",
    r"profitable.*(\$0|zero|no)\s*(budget|money|cost)",
    r"make (me|us) (rich|millionaire)",
    r"10x.*in (a day|24h|a week)"
]

def evaluate_guardrails(prompt: str) -> Tuple[bool, str, List[str]]:
    """
    Checks if a prompt is an edge-case or impossible request.
    Returns: (is_edge_case, reason, suggested_questions)
    """
    prompt_lower = prompt.lower()

    for pattern in ZERO_BUDGET_EXTREME_PROFIT:
        if re.search(pattern, prompt_lower):
            return (
                True,
                "Unrealistic timeline or zero-budget profitability claim",
                [
                    "What is your current monthly recurring revenue (MRR) and active user base?",
                    "What is your current gross margin and baseline customer retention rate?",
                    "Are you willing to focus on organic founder-led sales or referral loops first?"
                ]
            )

    for pattern in IMPOSSIBLE_TIME_PATTERNS:
        if ("profit" in prompt_lower or "scale" in prompt_lower or "1m" in prompt_lower) and re.search(pattern, prompt_lower):
            return (
                True,
                "Hyper-compressed timeline without operational baseline",
                [
                    "What is your existing product-market fit signal (NPS, churn)?",
                    "Do you have an existing email waitlist or client pipeline we can activate today?",
                    "Can we define a phased 30-60-90 day horizon for sustainable unit economics?"
                ]
            )

    return (False, "Standard strategic request", [])
