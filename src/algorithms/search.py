import time
from typing import List, Any, Optional, Callable
from ..models.apartment import Apartment


class SearchAlgorithms:
    
    @staticmethod
    def linear_search(apartments: List[Apartment], 
                     key_func: Callable[[Apartment], Any], 
                     target_value: Any) -> List[int]:
        """
        Linear search algorithm to find apartments matching a target value.
        
        Args:
            apartments: List of Apartment objects
            key_func: Function to extract the search key from an apartment
            target_value: Value to search for
            
        Returns:
            List of indices where matches are found
        """
        matches = []
        for i, apartment in enumerate(apartments):
            if key_func(apartment) == target_value:
                matches.append(i)
        return matches
    
    @staticmethod
    def binary_search(apartments: List[Apartment], 
                     key_func: Callable[[Apartment], Any], 
                     target_value: Any) -> Optional[int]:
        """
        Binary search algorithm (requires sorted list).
        
        Args:
            apartments: Sorted list of Apartment objects
            key_func: Function to extract the search key from an apartment
            target_value: Value to search for
            
        Returns:
            Index of first match found, or None if not found
        """
        left, right = 0, len(apartments) - 1
        
        while left <= right:
            mid = (left + right) // 2
            mid_value = key_func(apartments[mid])
            
            if mid_value == target_value:
                return mid
            elif mid_value < target_value:
                left = mid + 1
            else:
                right = mid - 1
        
        return None
    
    @staticmethod
    def search_by_price(apartments: List[Apartment], target_price: float) -> List[Apartment]:
        """Search for apartments with a specific price using linear search."""
        indices = SearchAlgorithms.linear_search(
            apartments, 
            lambda apt: apt.price, 
            target_price
        )
        return [apartments[i] for i in indices]
    
    @staticmethod
    def search_by_city(apartments: List[Apartment], city_name: str) -> List[Apartment]:
        """Search for apartments in a specific city using linear search."""
        indices = SearchAlgorithms.linear_search(
            apartments, 
            lambda apt: apt.cityname.lower() if apt.cityname else "", 
            city_name.lower()
        )
        return [apartments[i] for i in indices]
    
    @staticmethod
    def binary_search_by_price(sorted_apartments: List[Apartment], target_price: float) -> Optional[Apartment]:
        """Binary search for apartment with specific price (requires sorted list)."""
        index = SearchAlgorithms.binary_search(
            sorted_apartments,
            lambda apt: apt.price,
            target_price
        )
        return sorted_apartments[index] if index is not None else None
    
    @staticmethod
    def time_search_comparison(apartments: List[Apartment], 
                              target_price: float) -> dict:
        """
        Compare performance of linear vs binary search for price.
        Note: Binary search requires sorting first.
        """
        # Linear search timing
        start_time = time.time()
        linear_results = SearchAlgorithms.search_by_price(apartments, target_price)
        linear_time = time.time() - start_time
        
        # Sort apartments by price for binary search
        start_time = time.time()
        sorted_apartments = sorted(apartments, key=lambda apt: apt.price if apt.price else 0)
        sort_time = time.time() - start_time
        
        # Binary search timing
        start_time = time.time()
        binary_result = SearchAlgorithms.binary_search_by_price(sorted_apartments, target_price)
        binary_time = time.time() - start_time
        
        return {
            'linear_search': {
                'time': linear_time,
                'results_count': len(linear_results),
                'results': linear_results
            },
            'binary_search': {
                'sort_time': sort_time,
                'search_time': binary_time,
                'total_time': sort_time + binary_time,
                'result': binary_result
            }
        }