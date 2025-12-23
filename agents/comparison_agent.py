from typing import Dict, Any
import random


class ComparisonAgentError(Exception):
    """Raised when comparison processing fails."""


class ComparisonAgent:
    """
    Generates a comparison context between the primary product
    and a system-generated fictional alternative.
    """

    def run(self, product: Any) -> Dict[str, Any]:
        """
        Create comparison payload.

        Args:
            product: Parsed primary product (ProductData)

        Returns:
            Dictionary containing both products for comparison
        """
        if product is None:
            raise ComparisonAgentError("Primary product input is missing")

        fictional_product = self._create_fictional_product(product)

        return {
            "primary_product": product,
            "comparison_product": fictional_product
        }

    def _create_fictional_product(self, product: Any) -> Dict[str, Any]:
        """
        Generate a fictional product based on the structure
        of the primary product (without copying facts).

        Returns:
            Fictional product dictionary
        """
        name_variants = [
            "RadiantGlow C Serum",
            "LumiSkin Vitamin C",
            "PureAura C Boost"
        ]

        return {
            "name": random.choice(name_variants),
            "ingredients": ["Vitamin C"],
            "benefits": ["Skin radiance enhancement"],
            "price": product.price + 100
        }
