from typing import Dict, List, Any


class QuestionGenerationError(Exception):
    """Raised when question generation fails."""


class QuestionGenerationAgent:
    """
    Generates categorized user questions based on product attributes.

    Responsibilities:
    - Analyze product fields
    - Apply reusable question patterns
    - Produce categorized question sets
    """

    def run(self, product: Any) -> Dict[str, List[str]]:
        """
        Generate categorized questions for a product.

        Args:
            product: Parsed product object (ProductData)

        Returns:
            Dictionary mapping category -> list of questions
        """
        if product is None:
            raise QuestionGenerationError("Product input is missing")

        name = product.name

        questions = {
            "informational": self._informational_questions(name, product),
            "usage": self._usage_questions(name, product),
            "safety": self._safety_questions(name, product),
            "purchase": self._purchase_questions(name, product),
            "comparison": self._comparison_questions(name),
        }

        total_questions = sum(len(qs) for qs in questions.values())
        if total_questions < 15:
            raise QuestionGenerationError(
                f"Insufficient questions generated: {total_questions}"
            )

        return questions

    # ---------- Question Category Builders ----------

    def _informational_questions(self, name: str, product: Any) -> List[str]:
        return [
            f"What is {name}?",
            f"What are the main benefits of {name}?",
            f"Which skin types is {name} designed for?",
            f"What ingredients are used in {name}?",
        ]

    def _usage_questions(self, name: str, product: Any) -> List[str]:
        return [
            f"How should {name} be applied?",
            f"When is the best time to use {name}?",
            f"Can {name} be used daily?",
        ]

    def _safety_questions(self, name: str, product: Any) -> List[str]:
        return [
            f"Does {name} cause any side effects?",
            f"Is {name} suitable for sensitive skin?",
            f"What should I expect after the first application of {name}?",
        ]

    def _purchase_questions(self, name: str, product: Any) -> List[str]:
        return [
            f"What is the price of {name}?",
            f"Is {name} worth its price?",
            f"Who should consider buying {name}?",
        ]

    def _comparison_questions(self, name: str) -> List[str]:
        return [
            f"How does {name} compare to other Vitamin C serums?",
            f"Is {name} better than Product B?",
            f"What makes {name} different from similar products?",
        ]
