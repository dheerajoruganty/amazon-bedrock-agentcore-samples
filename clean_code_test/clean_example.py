"""Clean Python code that should pass all linting checks."""

from typing import List, Optional, Dict, Any
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


class DataProcessor:
    """Process data with various transformations."""

    def __init__(self, name: str, batch_size: int = 100):
        """Initialize the processor.

        Args:
            name: Name of the processor.
            batch_size: Size of processing batches.
        """
        self.name = name
        self.batch_size = batch_size
        self.processed_count = 0

    def process_batch(self, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Process a batch of data.

        Args:
            data: List of data items to process.

        Returns:
            Processed data items.
        """
        results = []
        for item in data:
            processed = self._transform_item(item)
            results.append(processed)
            self.processed_count += 1

        logger.info(f"Processed {len(data)} items")
        return results

    def _transform_item(self, item: Dict[str, Any]) -> Dict[str, Any]:
        """Transform a single data item.

        Args:
            item: Data item to transform.

        Returns:
            Transformed data item.
        """
        return {
            "id": item.get("id", ""),
            "processed": True,
            "processor": self.name,
            "data": item,
        }

    def get_statistics(self) -> Dict[str, Any]:
        """Get processing statistics.

        Returns:
            Dictionary containing processing statistics.
        """
        return {
            "processor_name": self.name,
            "batch_size": self.batch_size,
            "total_processed": self.processed_count,
        }


def calculate_average(numbers: List[float]) -> Optional[float]:
    """Calculate the average of a list of numbers.

    Args:
        numbers: List of numbers.

    Returns:
        Average value or None if list is empty.
    """
    if not numbers:
        return None
    return sum(numbers) / len(numbers)


def filter_valid_items(
    items: List[Dict[str, Any]], required_fields: List[str]
) -> List[Dict[str, Any]]:
    """Filter items that have all required fields.

    Args:
        items: List of items to filter.
        required_fields: List of required field names.

    Returns:
        Filtered list of valid items.
    """
    valid_items = []
    for item in items:
        if all(field in item for field in required_fields):
            valid_items.append(item)

    logger.debug(f"Filtered {len(valid_items)} valid items from {len(items)}")
    return valid_items


if __name__ == "__main__":
    # Example usage
    processor = DataProcessor("example_processor")

    sample_data = [
        {"id": "1", "value": 100},
        {"id": "2", "value": 200},
        {"id": "3", "value": 300},
    ]

    processed = processor.process_batch(sample_data)
    stats = processor.get_statistics()

    print(f"Processing complete: {stats}")
    print(f"Average value: {calculate_average([100.0, 200.0, 300.0])}")
