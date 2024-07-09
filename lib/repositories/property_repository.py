from lib.models.property import *

class PropertyRepository:
    
    def __init__(self, connection) -> None:
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute("SELECT * FROM properties")
        properties = []
        for row in rows:
            item = Property(row['id'], row['name'], row['description'], row['price'], row['available_from'], row['available_to'], row['owner_id'])
            properties.append(item)
        return properties
    
    def add(self, new_property):
        self._connection.execute('INSERT INTO properties (name, description, price, available_from, available_to, owner_id) VALUES (%s, %s, %s, %s, %s, %s)', [new_property.name, new_property.description, new_property.price, new_property.available_from, new_property.available_to, new_property.owner_id])

    def find(self, id):
        rows = self._connection.execute('SELECT * FROM properties WHERE id = %s', [id])
        if rows:
            print(rows)
            row = rows[0]
            return Property(row['id'], row['name'], row['description'], row['price'], row['available_from'], row['available_to'], row['owner_id'])
        return False