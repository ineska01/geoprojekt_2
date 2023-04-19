data = {
    "type": "Feature",
    "geometry": {
    "type": "Point",
    "coordinates": [125.6, 10.1]
    },
    "properties": {
    "name": "Dinagat Islands"
    }
}

class GeoData:
    
    def __init__(self, data):
        self.data = data
    
    def get_type(self):
        return self.data['type']
    
    def get_coordinates(self):
        return self.data['geometry']['coordinates']
    
    def get_bbox(self):
        if 'bbox' in self.data:
            return self.data['bbox']
        else:
            return None
 
    def to_string(self):
        return self.data  

geo = GeoData(data)
print(geo.get_type()) 
print(geo.get_coordinates()) 
print(geo.get_bbox()) 
print(geo.to_string()) 