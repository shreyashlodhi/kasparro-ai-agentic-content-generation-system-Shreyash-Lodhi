from typing import Dict, Any

from logic_blocks.benefits_block import build_benefits_text
from logic_blocks.usage_block import build_usage_text
from logic_blocks.safety_block import build_safety_text


class ContentLogicError(Exception):
    """Raised when content logic processing fails."""


class ContentLogicAgent:
    """
    Executes reusable content logic on parsed product data.

    Responsibilities:
    - Invoke content logic blocks
    - Produce structured content fragments
    - Remain independent of page templates
    """

    def run(self, product: Any) -> Dict[str, str]:
        """
        Apply content logic to product data.

        Args:
            product: Parsed product object (ProductData)

        Returns:
            Dictionary containing reusable content fragments
        """
        if product is None:
            raise ContentLogicError("Product input is required")

        try:
            benefits_text = build_benefits_text(product.benefits)
            usage_text = build_usage_text(product.usage)
            safety_text = build_safety_text(product.side_effects)
        except Exception as exc:
            raise ContentLogicError(
                "Failed to apply content logic blocks"
            ) from exc

        return {
            "benefits_text": benefits_text,
            "usage_text": usage_text,
            "safety_text": safety_text,
        }