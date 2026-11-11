import io
import csv
from typing import List, Dict, Any

def generate_csv_artifact(headers: List[str], rows: List[List[Any]]) -> str:
    """
    Produces clean, downloadable CSV text for Nonilion attachments or copy blocks.
    """
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(headers)
    for row in rows:
        writer.writerow(row)
    return output.getvalue().strip()

def format_csv_code_block(csv_content: str, filename: str = "allocation_model.csv") -> str:
    """Wraps CSV in markdown code block with downloadable labeling."""
    return f"```csv\n# Filename: {filename}\n{csv_content}\n```"
