"""
FAQ Page Template

Assembles a structured FAQ page using
generated questions and reusable content fragments.
"""

from typing import Dict, List


def build_faq_page(
    questions_by_category: Dict[str, List[str]],
    content_fragments: Dict[str, str],
    minimum_items: int = 10
) -> Dict:
    """
    Build a FAQ page structure.

    Args:
        questions_by_category: Categorized user questions
        content_fragments: Reusable content blocks
        minimum_items: Minimum number of FAQ entries

    Returns:
        FAQ page as a machine-readable dictionary
    """
    faq_entries = []

    for category, questions in questions_by_category.items():
        for question in questions:
            if len(faq_entries) >= minimum_items:
                break

            faq_entries.append({
                "category": category,
                "question": question,
                "answer": content_fragments.get(
                    "benefits_text",
                    "Information will be available soon."
                )
            })

        if len(faq_entries) >= minimum_items:
            break

    return {
        "page_type": "faq",
        "total_items": len(faq_entries),
        "items": faq_entries
    }
