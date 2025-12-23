import json
from pathlib import Path

from agents.data_parser_agent import DataParserAgent
from agents.question_generation_agent import QuestionGenerationAgent
from agents.content_logic_agent import ContentLogicAgent
from agents.comparison_agent import ComparisonAgent
from agents.page_assembly_agent import PageAssemblyAgent


class PipelineError(Exception):
    """Raised when pipeline execution fails."""


class ContentGenerationPipeline:
    """
    Orchestrates the full multi-agent content generation flow.
    """

    def __init__(
        self,
        data_path: str = "data/product_data.json",
        output_dir: str = "output"
    ) -> None:
        self.data_path = data_path
        self.output_dir = Path(output_dir)

        self.output_dir.mkdir(parents=True, exist_ok=True)

        # Initialize agents
        self.data_parser = DataParserAgent(self.data_path)
        self.question_generator = QuestionGenerationAgent()
        self.content_logic = ContentLogicAgent()
        self.comparison_agent = ComparisonAgent()
        self.page_assembler = PageAssemblyAgent()

    def run(self) -> None:
        """
        Execute the full pipeline.
        """
        try:
            # -------------------------------
            # STEP 1: Parse product data
            # -------------------------------
            parsed_data = self.data_parser.run()
            product = parsed_data["product"]

            # -------------------------------
            # STEP 2: Generate user questions
            # -------------------------------
            questions = self.question_generator.run(product)

            # -------------------------------
            # STEP 3: Apply content logic blocks
            # -------------------------------
            content_fragments = self.content_logic.run(product)

            # -------------------------------
            # STEP 4: Generate comparison data
            # -------------------------------
            comparison_data = self.comparison_agent.run(product)

            # -------------------------------
            # STEP 5: Assemble pages
            # -------------------------------
            pages = self.page_assembler.run(
                product=product,
                questions=questions,
                content_fragments=content_fragments,
                comparison_data=comparison_data
            )

            # -------------------------------
            # STEP 6: Persist outputs
            # -------------------------------
            self._write_output("faq.json", pages["faq_page"])
            self._write_output("product_page.json", pages["product_page"])
            self._write_output("comparison_page.json", pages["comparison_page"])

            print("✅ Pipeline executed successfully.")
            print("📁 Output files written to:", self.output_dir.resolve())

        except Exception as exc:
            raise PipelineError("Pipeline execution failed") from exc

    def _write_output(self, filename: str, payload: dict) -> None:
        """
        Write JSON output to disk.

        Args:
            filename: Output file name
            payload: JSON-serializable dictionary
        """
        output_path = self.output_dir / filename
        with output_path.open("w", encoding="utf-8") as file:
            json.dump(payload, file, indent=2)