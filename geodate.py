# Zrób wirtualne środowisko i plik requirements.txt z potrzebnymi libami
# uruchom virtual enva i poinstaluj wszystko
#  python -m venv test_env
# .\test_env\Scripts\activate
#  deactivate
# zrób git-a na githubie i je połącz 

# Zadanie: Napisać klasę GeoData, która będzie przechowywać dane geoprzestrzenne w formacie GeoJSON. 
# Klasa powinna mieć metody:
# __init__(self, data): Konstruktor klasy, który przyjmuje dane GeoJSON w postaci słownika i przypisuje je do atrybutu data.
# get_type(self): Metoda zwracająca typ geometrii obiektu GeoJSON.
# get_coordinates(self): Metoda zwracająca współrzędne obiektu GeoJSON.
# get_bbox(self): Metoda zwracająca bbox (ang. bounding box) obiektu GeoJSON.
# to_string(self): Metoda zwracająca dane obiektu GeoJSON w postaci ciągu znaków.

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
print(geo.get_type()) # Wypisze "Feature"
print(geo.get_coordinates()) # Wypisze [125.6, 10.1]
print(geo.get_bbox()) # Zwróci None, ponieważ bbox nie jest zdefiniowane w danych wejściowych
print(geo.to_string()) # Wypisze '{"type": "Feature", "geometry": {"type": "Point", "coordinates": [125.6, 10.1]}, "properties": {"name": "Dinagat Islands"}}'