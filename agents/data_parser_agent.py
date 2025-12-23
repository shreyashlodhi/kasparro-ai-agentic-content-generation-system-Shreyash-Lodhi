import json
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Any, List


class DataParserError(Exception):
    """Raised when product data parsing fails."""


@dataclass
class ProductData:
    """
    Normalized internal model used by downstream agents.
    """
    name: str
    concentration: str
    skin_types: List[str]
    ingredients: List[str]
    benefits: List[str]
    usage: str
    side_effects: str
    price: int


class DataParserAgent:
    """
    Loads and normalizes product data from a JSON file.

    Responsibilities:
    - Read product data from a file
    - Ensure all required fields exist
    - Convert raw data into a structured ProductData object
    - Return both raw and normalized representations
    """

    REQUIRED_FIELDS = {
        "product_name",
        "concentration",
        "skin_type",
        "key_ingredients",
        "benefits",
        "how_to_use",
        "side_effects",
        "price_in_inr",
    }

    def __init__(self, file_path: str = "data/product_data.json") -> None:
        self.file_path = Path(file_path)

    def run(self) -> Dict[str, Any]:
        """
        Executes the parsing process.

        Returns:
            Dict containing:
                - product (ProductData)
                - raw_data (dict)

        Raises:
            DataParserError if any validation or IO step fails
        """
        raw_data = self._load_file()
        self._validate_fields(raw_data)
        product = self._build_internal_model(raw_data)

        return {
            "product": product,
            "raw_data": raw_data
        }

    def _load_file(self) -> Dict[str, Any]:
        if not self.file_path.exists():
            raise DataParserError(
                f"Product data file not found at: {self.file_path}"
            )

        try:
            with self.file_path.open("r", encoding="utf-8") as file:
                return json.load(file)
        except json.JSONDecodeError as exc:
            raise DataParserError(
                "Product data file contains invalid JSON"
            ) from exc

    def _validate_fields(self, data: Dict[str, Any]) -> None:
        missing = self.REQUIRED_FIELDS - data.keys()
        if missing:
            raise DataParserError(
                f"Missing required fields in product data: {missing}"
            )

    def _build_internal_model(self, data: Dict[str, Any]) -> ProductData:
        try:
            return ProductData(
                name=data["product_name"],
                concentration=data["concentration"],
                skin_types=list(data["skin_type"]),
                ingredients=list(data["key_ingredients"]),
                benefits=list(data["benefits"]),
                usage=data["how_to_use"],
                side_effects=data["side_effects"],
                price=int(data["price_in_inr"]),
            )
        except (TypeError, ValueError) as exc:
            raise DataParserError(
                "Product data contains invalid field types"
            ) from exc
