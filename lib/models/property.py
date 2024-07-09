class Property():
    
    def __init__(self, id, name,  description, price, available_from, available_to, owner_id) -> None:
        self.id = id
        self.name = name
        self.price = price
        self.description = description
        self.available_from = available_from
        self.available_to = available_to
        self.owner_id = owner_id
    
    def __repr__(self) -> str:
        return f'Property({self.id}, {self.name},  {self.description}, {self.price}, {self.available_from}, {self.available_to}, {self.owner_id})'
    
    def __eq__(self, value: object) -> bool:
        return self.__dict__ == value.__dict__
    
    def is_valid(self):
        if self.name == '' or self.name == None:
            return False
        if self.description == '' or self.description == None:
            return False
        if self.price == 0 or self.price == None:
            return False
        if self.available_from == None:
            return False
        if self.available_to == None:
            return False
        return True
    
    def generate_errors(self):
        errors = []
        if self.name == '' or self.name == None:
            errors.append('You must enter a name')
        if self.description == '' or self.description == None:
            errors.append('You must enter a description')
        if self.price == 0 or self.price == None:
            errors.append('You must enter a price')
        if self.available_from == None or self.available_to == None:
            errors.append('You must enter a valid date')
        return ', '.join(errors)
        