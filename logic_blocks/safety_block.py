"""
Safety Logic Block

Responsible for generating safety and
side-effect related information.
"""


def build_safety_text(side_effects: str) -> str:
    """
    Create safety information from side-effect data.

    Args:
        side_effects: Side effects description

    Returns:
        Safety notice text
    """
    if not side_effects:
        return "No known side effects have been reported."

    return side_effects.strip()
