import time
from typing import List, Callable, Any

# Handle both notebook and package imports
try:
    from ..models.apartment import Apartment
except ImportError:
    from models.apartment import Apartment


class SortingAlgorithms:
    
    @staticmethod
    def bubble_sort(apartments: List[Apartment], 
                   key_func: Callable[[Apartment], Any], 
                   reverse: bool = False) -> List[Apartment]:
        """
        Bubble sort implementation for apartments.
        
        Args:
            apartments: List of Apartment objects to sort
            key_func: Function to extract sort key from apartment
            reverse: If True, sort in descending order
            
        Returns:
            Sorted list of apartments
        """
        sorted_apartments = apartments.copy()
        n = len(sorted_apartments)
        
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                value1 = key_func(sorted_apartments[j])
                value2 = key_func(sorted_apartments[j + 1])
                
                # Handle None values by treating them as very large or very small
                if value1 is None:
                    value1 = float('inf') if not reverse else float('-inf')
                if value2 is None:
                    value2 = float('inf') if not reverse else float('-inf')
                
                should_swap = value1 > value2 if not reverse else value1 < value2
                
                if should_swap:
                    sorted_apartments[j], sorted_apartments[j + 1] = sorted_apartments[j + 1], sorted_apartments[j]
                    swapped = True
            
            if not swapped:
                break
        
        return sorted_apartments
    
    @staticmethod
    def insertion_sort(apartments: List[Apartment], 
                      key_func: Callable[[Apartment], Any], 
                      reverse: bool = False) -> List[Apartment]:
        """
        Insertion sort implementation for apartments.
        
        Args:
            apartments: List of Apartment objects to sort
            key_func: Function to extract sort key from apartment
            reverse: If True, sort in descending order
            
        Returns:
            Sorted list of apartments
        """
        sorted_apartments = apartments.copy()
        
        for i in range(1, len(sorted_apartments)):
            current_apartment = sorted_apartments[i]
            current_value = key_func(current_apartment)
            
            # Handle None values
            if current_value is None:
                current_value = float('inf') if not reverse else float('-inf')
            
            j = i - 1
            
            while j >= 0:
                compare_value = key_func(sorted_apartments[j])
                if compare_value is None:
                    compare_value = float('inf') if not reverse else float('-inf')
                
                should_move = compare_value > current_value if not reverse else compare_value < current_value
                
                if should_move:
                    sorted_apartments[j + 1] = sorted_apartments[j]
                    j -= 1
                else:
                    break
            
            sorted_apartments[j + 1] = current_apartment
        
        return sorted_apartments
    
    @staticmethod
    def sort_by_price(apartments: List[Apartment], 
                     algorithm: str = "bubble", 
                     reverse: bool = False) -> List[Apartment]:
        """Sort apartments by price using specified algorithm."""
        if algorithm.lower() == "bubble":
            return SortingAlgorithms.bubble_sort(apartments, lambda apt: apt.price, reverse)
        elif algorithm.lower() == "insertion":
            return SortingAlgorithms.insertion_sort(apartments, lambda apt: apt.price, reverse)
        else:
            raise ValueError("Algorithm must be 'bubble' or 'insertion'")
    
    @staticmethod
    def sort_by_square_feet(apartments: List[Apartment], 
                           algorithm: str = "bubble", 
                           reverse: bool = False) -> List[Apartment]:
        """Sort apartments by square feet using specified algorithm."""
        if algorithm.lower() == "bubble":
            return SortingAlgorithms.bubble_sort(apartments, lambda apt: apt.square_feet, reverse)
        elif algorithm.lower() == "insertion":
            return SortingAlgorithms.insertion_sort(apartments, lambda apt: apt.square_feet, reverse)
        else:
            raise ValueError("Algorithm must be 'bubble' or 'insertion'")
    
    @staticmethod
    def sort_by_bathrooms(apartments: List[Apartment], 
                         algorithm: str = "bubble", 
                         reverse: bool = False) -> List[Apartment]:
        """Sort apartments by number of bathrooms using specified algorithm."""
        if algorithm.lower() == "bubble":
            return SortingAlgorithms.bubble_sort(apartments, lambda apt: apt.bathrooms, reverse)
        elif algorithm.lower() == "insertion":
            return SortingAlgorithms.insertion_sort(apartments, lambda apt: apt.bathrooms, reverse)
        else:
            raise ValueError("Algorithm must be 'bubble' or 'insertion'")
    
    @staticmethod
    def compare_sorting_performance(apartments: List[Apartment], 
                                  key_func: Callable[[Apartment], Any],
                                  sample_size: int = 1000) -> dict:
        """
        Compare performance of different sorting algorithms.
        
        Args:
            apartments: List of apartments to sort
            key_func: Function to extract sort key
            sample_size: Number of apartments to use for comparison
            
        Returns:
            Dictionary with timing results
        """
        # Use a sample for performance comparison to avoid long wait times
        sample_apartments = apartments[:sample_size]
        
        results = {}
        
        # Bubble sort timing
        start_time = time.time()
        bubble_sorted = SortingAlgorithms.bubble_sort(sample_apartments, key_func)
        bubble_time = time.time() - start_time
        
        # Insertion sort timing
        start_time = time.time()
        insertion_sorted = SortingAlgorithms.insertion_sort(sample_apartments, key_func)
        insertion_time = time.time() - start_time
        
        # Built-in sort timing
        start_time = time.time()
        builtin_sorted = sorted(sample_apartments, key=lambda apt: key_func(apt) if key_func(apt) is not None else float('inf'))
        builtin_time = time.time() - start_time
        
        results = {
            'sample_size': len(sample_apartments),
            'bubble_sort': {
                'time': bubble_time,
                'time_per_item': bubble_time / len(sample_apartments) if sample_apartments else 0
            },
            'insertion_sort': {
                'time': insertion_time,
                'time_per_item': insertion_time / len(sample_apartments) if sample_apartments else 0
            },
            'builtin_sort': {
                'time': builtin_time,
                'time_per_item': builtin_time / len(sample_apartments) if sample_apartments else 0
            }
        }
        
        # Calculate relative performance
        fastest_time = min(bubble_time, insertion_time, builtin_time)
        results['relative_performance'] = {
            'bubble_sort': bubble_time / fastest_time,
            'insertion_sort': insertion_time / fastest_time,
            'builtin_sort': builtin_time / fastest_time
        }
        
        return results