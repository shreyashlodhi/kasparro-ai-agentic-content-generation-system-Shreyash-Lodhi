"""
Product Page Template

Creates a structured product detail page
from normalized product data and content fragments.
"""

from typing import Dict, Any


def build_product_page(
    product: Any,
    content_fragments: Dict[str, str]
) -> Dict:
    """
    Assemble a product page.

    Args:
        product: Parsed product object
        content_fragments: Reusable content blocks

    Returns:
        Product page dictionary
    """
    return {
        "page_type": "product",
        "product_name": product.name,
        "concentration": product.concentration,
        "skin_types": product.skin_types,
        "ingredients": product.ingredients,
        "benefits": content_fragments.get("benefits_text"),
        "usage": content_fragments.get("usage_text"),
        "safety_information": content_fragments.get("safety_text"),
        "price_inr": product.price
    }
