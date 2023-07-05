from subwayGraph.subway import Subway
from model import BorderModel

class GraphController:
    def __init__(self):
        self.subway = Subway()
        self.subway.create_stations("subway-stations.csv")
        self.subway.populate_neighbors("subway-stations.csv")

    def get_path(self, data: BorderModel):
        source = data.source
        dest = data.dest
        path = self.subway.find_path_between_stations_through_name(source, dest)
        response = {
            "status": "200 OK",
            "path": path 
        }
        return response 
    
    