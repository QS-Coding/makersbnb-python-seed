from lib.models.user import *
class UserRepository():
    
    def __init__(self, connection) -> None:
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute('SELECT * FROM users')
        users = []
        for row in rows:
            user = User(row['id'], row['email'], row['name'], row['password'])
            users.append(user)
        return users
    
    def create(self, user):
        self._connection.execute("INSERT INTO users (name, email, password) VALUES (%s, %s, crypt(%s, gen_salt(%s)))", [user.name, user.email, user.password, 'bf'])
    
    def login(self, email, password):
        rows = self._connection.execute("SELECT (password = crypt(%s, password)) as match from users WHERE email = %s", [password, email])
        if rows and rows[0]['match']:
            return self.find_by_email(email)
        return False
    
    def find_by_email(self, email):
        rows = self._connection.execute("SELECT * FROM users WHERE email = %s", [email])
        if rows:
            row = rows[0]
            return User(row['id'], row['email'], row['name'], None)
        return False
    
    def find_by_id(self, id):
        rows = self._connection.execute("SELECT * FROM users WHERE id = %s", [id])
        if rows:
            print(rows)
            row = rows[0]
            return User(row['id'], row['email'], row['name'], None)
        return False