import numpy as np
import math
from typing import List, Dict, Tuple
from .dataset_manager import DatasetManager
from ..models.apartment import Apartment


class LocationAnalysis(DatasetManager):
    def __init__(self, data_path: str = None):
        super().__init__(data_path)
    
    def get_summary(self) -> str:
        if not self.apartments:
            return "No apartments loaded for location analysis"
        
        cities = set(apt.cityname for apt in self.apartments if apt.cityname)
        states = set(apt.state for apt in self.apartments if apt.state)
        
        valid_coords = [(apt.latitude, apt.longitude) for apt in self.apartments 
                       if apt.latitude is not None and apt.longitude is not None]
        
        return f"""Location Analysis Summary:
        Total Apartments: {len(self.apartments)}
        Unique Cities: {len(cities)}
        Unique States: {len(states)}
        Valid Coordinates: {len(valid_coords)}
        Top Cities: {self._get_top_cities(5)}"""
    
    def _get_top_cities(self, n: int = 10) -> List[Tuple[str, int]]:
        city_counts = {}
        for apt in self.apartments:
            if apt.cityname:
                city_counts[apt.cityname] = city_counts.get(apt.cityname, 0) + 1
        
        return sorted(city_counts.items(), key=lambda x: x[1], reverse=True)[:n]
    
    def filter_by_city(self, city_name: str) -> List[Apartment]:
        return [apt for apt in self.apartments 
                if apt.cityname and apt.cityname.lower() == city_name.lower()]
    
    def filter_by_state(self, state: str) -> List[Apartment]:
        return [apt for apt in self.apartments 
                if apt.state and apt.state.lower() == state.lower()]
    
    def calculate_distance(self, lat1: float, lon1: float, lat2: float, lon2: float) -> float:
        R = 6371.0
        
        lat1_rad = math.radians(lat1)
        lon1_rad = math.radians(lon1)
        lat2_rad = math.radians(lat2)
        lon2_rad = math.radians(lon2)
        
        dlat = lat2_rad - lat1_rad
        dlon = lon2_rad - lon1_rad
        
        a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        
        return R * c
    
    def filter_by_proximity(self, target_lat: float, target_lon: float, 
                           radius_km: float) -> List[Apartment]:
        nearby_apartments = []
        
        for apt in self.apartments:
            if apt.latitude is not None and apt.longitude is not None:
                distance = self.calculate_distance(target_lat, target_lon, 
                                                 apt.latitude, apt.longitude)
                if distance <= radius_km:
                    nearby_apartments.append(apt)
        
        return nearby_apartments
    
    def get_city_statistics(self) -> Dict[str, Dict[str, any]]:
        city_stats = {}
        
        for apt in self.apartments:
            if apt.cityname:
                city = apt.cityname
                if city not in city_stats:
                    city_stats[city] = {
                        'count': 0,
                        'prices': [],
                        'avg_bedrooms': [],
                        'state': apt.state
                    }
                
                city_stats[city]['count'] += 1
                
                if apt.price is not None:
                    city_stats[city]['prices'].append(apt.price)
                
                if apt.bedrooms is not None:
                    city_stats[city]['avg_bedrooms'].append(apt.bedrooms)
        
        for city, stats in city_stats.items():
            if stats['prices']:
                stats['avg_price'] = np.mean(stats['prices'])
                stats['median_price'] = np.median(stats['prices'])
            else:
                stats['avg_price'] = None
                stats['median_price'] = None
            
            if stats['avg_bedrooms']:
                stats['avg_bedrooms'] = np.mean(stats['avg_bedrooms'])
            else:
                stats['avg_bedrooms'] = None
            
            del stats['prices']
        
        return city_stats
    
    def get_state_statistics(self) -> Dict[str, Dict[str, any]]:
        state_stats = {}
        
        for apt in self.apartments:
            if apt.state:
                state = apt.state
                if state not in state_stats:
                    state_stats[state] = {
                        'count': 0,
                        'prices': [],
                        'cities': set()
                    }
                
                state_stats[state]['count'] += 1
                
                if apt.price is not None:
                    state_stats[state]['prices'].append(apt.price)
                
                if apt.cityname:
                    state_stats[state]['cities'].add(apt.cityname)
        
        for state, stats in state_stats.items():
            if stats['prices']:
                stats['avg_price'] = np.mean(stats['prices'])
                stats['median_price'] = np.median(stats['prices'])
            else:
                stats['avg_price'] = None
                stats['median_price'] = None
            
            stats['unique_cities'] = len(stats['cities'])
            del stats['prices']
            del stats['cities']
        
        return state_stats