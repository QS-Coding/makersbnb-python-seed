class User():
    def __init__(self, id, email, name, password) -> None:
        self.id = id
        self.email = email
        self.name = name
        self.password = password
    
    def __repr__(self) -> str:
        return f'User({self.id}, {self.email}, {self.name}, {self.password})'
    
    def __eq__(self, value: object) -> bool:
        return self.__dict__ == value.__dict__