"""
Benefits Logic Block

Transforms raw benefit attributes into
a human-readable benefits statement.
"""

from typing import List


def build_benefits_text(benefits: List[str]) -> str:
    """
    Convert a list of benefits into a formatted text string.

    Args:
        benefits: List of benefit phrases

    Returns:
        A readable benefits description
    """
    if not benefits:
        return "No specific benefits information available."

    return ", ".join(benefits)
