from lib.models.image import Image
from psycopg import Binary

class ImageRepository:
    def __init__(self, connection) -> None:
        self._connection = connection

    def find_by_property_id(self, property_id):
            rows = self._connection.execute("SELECT * FROM images WHERE property_id = %s", [property_id])
            if rows:
                print(rows)
                row = rows[0]
                return Image(row['id'], row['property_id'], row['image'])
            return False
    
    def insert_image(self,property_id,image_data):
        self._connection.execute("INSERT INTO images (property_id,image) VALUES (%s,%s)",[property_id,Binary(image_data)])
