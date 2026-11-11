from typing import Dict, Any, List

def calculate_channel_efficiency(
    budget: float,
    channels: List[Dict[str, Any]]
) -> Dict[str, Any]:
    """
    Computes ROI, expected conversions, and blended CAC across acquisition channels.
    Each channel dictionary should have: 'name', 'allocation_pct', 'est_cac', 'cycle_days'.
    """
    results = []
    total_conversions = 0
    total_allocated = 0.0

    for ch in channels:
        alloc_amount = budget * (ch.get("allocation_pct", 0) / 100.0)
        est_cac = ch.get("est_cac", 100.0)
        conversions = int(alloc_amount / est_cac) if est_cac > 0 else 0
        total_conversions += conversions
        total_allocated += alloc_amount

        results.append({
            "channel": ch.get("name"),
            "allocated_budget": round(alloc_amount, 2),
            "est_cac": est_cac,
            "expected_customers": conversions,
            "sales_cycle_days": ch.get("cycle_days", 30),
            "risk_profile": ch.get("risk", "Medium")
        })

    blended_cac = round(total_allocated / total_conversions, 2) if total_conversions > 0 else 0.0

    return {
        "total_budget": budget,
        "total_expected_customers": total_conversions,
        "blended_cac": blended_cac,
        "breakdown": results
    }
