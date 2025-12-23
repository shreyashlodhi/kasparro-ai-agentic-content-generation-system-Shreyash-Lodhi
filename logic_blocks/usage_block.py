"""
Usage Logic Block

Handles transformation of usage instructions
into standardized user-facing text.
"""


def build_usage_text(usage_instruction: str) -> str:
    """
    Normalize product usage instructions.

    Args:
        usage_instruction: Raw usage description

    Returns:
        Clean usage guidance text
    """
    if not usage_instruction:
        return "Usage instructions are not provided."

    return usage_instruction.strip()
