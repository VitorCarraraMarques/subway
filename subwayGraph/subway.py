import csv
from typing import List
from collections import deque

from subwayGraph.station import Station 


class Subway: 
    def __init__(self):
        self.stations: List[Station] = []

    def _find_station_by_name(self, name): 
        for station in self.stations:
            if station.name == name:
                return station 

    def _parse_lanes(self,lanes_str:str) -> List[int]:
        lanes = []
        current_lane = ''
        for char in lanes_str:
            if char == ';':
                lanes.append(int(current_lane))
                current_lane = ''
                continue
            current_lane += char 
        return lanes 

    def _parse_neighbors(self,neighbors_str:str) -> List[str]:
        neighbors = []
        current_name = ''
        for char in neighbors_str: 
            if char == ';':
                neighbors.append(current_name)
                current_name = ''
                continue
            current_name += char
        return neighbors
   
    def create_stations(self, path:str) -> None:
        with open(path, encoding="utf8") as file: 
            reader = csv.reader(file)
            next(reader, None)
            for row in reader:
                station = Station(row[0], self._parse_lanes(row[1]))
                self.stations.append(station)

    def populate_neighbors(self,path:str) -> None:
        with open(path, encoding="utf8") as file: 
            reader = csv.reader(file)
            next(reader, None)  
            for row in reader: 
                station = self._find_station_by_name(row[0])
                station.neighbors = []
                neighbors = self._parse_neighbors(row[2])
                for neighbor in neighbors: 
                    for s in self.stations:
                        if s.name == neighbor:
                            station.neighbors.append(s)
                            break
        
        return None 

    def find_path_between_stations_through_name(self, source_name: str, dest_name: str) -> List[str]:
        path = [] 
        source = self._find_station_by_name(source_name)        
        
        visited = set()
        queue = deque() 
        queue.append([source, [(source.name,source.lane)]])
        visited.add(source.name)
        while queue: 
            cur_stat, cur_path = queue.popleft()
            for neighbor in cur_stat.neighbors: 
                if neighbor.name == dest_name:
                    return cur_path + [(neighbor.name, neighbor.lane)]
                if neighbor.name not in visited:
                    queue.append([neighbor, cur_path + [(neighbor.name, neighbor.lane)]]) 
                    visited.add(neighbor.name)

        return path 


