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
    
    def is_valid(self):
        if self.email == None or self.email == '':
            return False
        if self.name == None or self.name == '':
            return False
        if self.password == None or self.password == '':
            return False
        return True
    
    def generate_errors(self):
        errors = []
        if self.email == None or self.email == '':
            errors.append('You need to enter a name')
        if self.name == None or self.name == '':
            errors.append('You need to enter an email')
        if self.password == None or self.password == '':
            errors.append('You need to enter a password')
        return ', '.join(errors)