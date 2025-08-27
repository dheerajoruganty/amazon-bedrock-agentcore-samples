"""Sample clean Python file that should pass all linting checks."""

from typing import List, Optional


def calculate_sum(numbers: List[int]) -> int:
    """Calculate the sum of a list of numbers.
    
    Args:
        numbers: A list of integers to sum.
        
    Returns:
        The sum of all numbers in the list.
    """
    total = 0
    for num in numbers:
        total += num
    return total


def find_maximum(values: List[float], default: Optional[float] = None) -> Optional[float]:
    """Find the maximum value in a list.
    
    Args:
        values: List of float values.
        default: Default value if list is empty.
        
    Returns:
        Maximum value or default if list is empty.
    """
    if not values:
        return default
    
    max_val = values[0]
    for val in values:
        if val > max_val:
            max_val = val
    
    return max_val


class DataProcessor:
    """Process data with various transformations."""
    
    def __init__(self, name: str):
        """Initialize the processor.
        
        Args:
            name: Name of the processor.
        """
        self.name = name
        self.processed_count = 0
    
    def process(self, data: List[str]) -> List[str]:
        """Process a list of strings.
        
        Args:
            data: List of strings to process.
            
        Returns:
            Processed list of strings.
        """
        result = []
        for item in data:
            processed_item = item.strip().lower()
            result.append(processed_item)
            self.processed_count += 1
        
        return result
    
    def get_stats(self) -> dict:
        """Get processing statistics.
        
        Returns:
            Dictionary containing stats.
        """
        return {
            "name": self.name,
            "processed_count": self.processed_count
        }


if __name__ == "__main__":
    # Test the functions
    numbers = [1, 2, 3, 4, 5]
    print(f"Sum: {calculate_sum(numbers)}")
    
    values = [3.14, 2.71, 1.41, 4.0]
    print(f"Maximum: {find_maximum(values)}")
    
    processor = DataProcessor("test_processor")
    data = ["  Hello  ", "  WORLD  ", "  Python  "]
    processed = processor.process(data)
    print(f"Processed data: {processed}")
    print(f"Stats: {processor.get_stats()}")