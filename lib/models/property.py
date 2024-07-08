class Property():
    
    def __init__(self, id, address, price, description, user_id) -> None:
        self.id = id
        self.address = address
        self.price = price
        self.description = description
        self.user_id = user_id
    
    def __repr__(self) -> str:
        return f'Property({self.id}, {self.address}, {self.price}, {self.description}, {self.user_id})'
    
    def __eq__(self, value: object) -> bool:
        return self.__dict__ == value.__dict__