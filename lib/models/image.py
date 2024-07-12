class Image():
    def __init__(self, id, property_id, image) -> None:
        self.id = id
        self.property_id = property_id
        self.image = image
    
    def __repr__(self) -> str:
        return f'Image({self.id}, {self.property_id}, {self.image})'
    
    def __eq__(self, value: object) -> bool:
        return self.__dict__ == value.__dict__