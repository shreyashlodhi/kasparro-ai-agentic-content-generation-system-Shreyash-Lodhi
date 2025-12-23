from typing import Dict, Any

from templates.faq_template import build_faq_page
from templates.product_template import build_product_page
from templates.comparison_template import build_comparison_page


class PageAssemblyError(Exception):
    """Raised when page assembly fails."""


class PageAssemblyAgent:
    """
    Responsible for assembling final page structures.

    Responsibilities:
    - Invoke page templates
    - Combine structured agent outputs
    - Return machine-readable page payloads
    """

    def run(
        self,
        product: Any,
        questions: Dict[str, list],
        content_fragments: Dict[str, str],
        comparison_data: Dict[str, Any],
    ) -> Dict[str, Dict]:
        """
        Assemble all required pages.

        Args:
            product: Parsed product object
            questions: Categorized user questions
            content_fragments: Reusable content blocks
            comparison_data: Output from ComparisonAgent

        Returns:
            Dictionary containing all generated pages
        """
        if not product:
            raise PageAssemblyError("Product data is missing")

        try:
            faq_page = build_faq_page(
                questions_by_category=questions,
                content_fragments=content_fragments
            )

            product_page = build_product_page(
                product=product,
                content_fragments=content_fragments
            )

            comparison_page = build_comparison_page(
                primary_product=comparison_data["primary_product"],
                comparison_product=comparison_data["comparison_product"]
            )

        except Exception as exc:
            raise PageAssemblyError(
                "Failed to assemble pages"
            ) from exc

        return {
            "faq_page": faq_page,
            "product_page": product_page,
            "comparison_page": comparison_page
        }