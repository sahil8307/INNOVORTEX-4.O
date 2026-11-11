import urllib.parse
import json
from typing import List, Dict, Any

def generate_quickchart_url(
    chart_type: str = "bar",
    labels: List[str] = None,
    datasets: List[Dict[str, Any]] = None,
    title: str = "OmniChief Executive Analysis"
) -> str:
    """
    Generates a high-resolution, embeddable QuickChart.io URL for instant image rendering.
    """
    if labels is None:
        labels = ["Option A", "Option B", "Option C"]
    if datasets is None:
        datasets = [{"label": "Score", "data": [75, 90, 60]}]

    chart_config = {
        "type": chart_type,
        "data": {
            "labels": labels,
            "datasets": datasets
        },
        "options": {
            "title": {
                "display": True,
                "text": title,
                "fontSize": 16
            },
            "legend": {
                "position": "top"
            }
        }
    }

    config_str = json.dumps(chart_config)
    encoded_config = urllib.parse.quote(config_str)
    return f"https://quickchart.io/chart?c={encoded_config}&w=600&h=350&bkg=white"

def format_markdown_image(title: str, chart_url: str) -> str:
    """Formats an image URL as markdown."""
    return f"![{title}]({chart_url})"
