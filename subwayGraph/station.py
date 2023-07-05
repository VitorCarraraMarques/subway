from typing import List

class Station:
    def __init__(self, name, lane):
        self.name: str = name
        self.lane: List[int] = lane
        self.neighbors: List[Station] = None

    def __str__(self):
        name = self.name 
        answer = f'Conexões da Estação {self.name.upper()}: \n'
        for neighbor in self.neighbors:
            nei_name = neighbor.name 
            answer += f"{name} <-> {nei_name} \n"
        return answer


