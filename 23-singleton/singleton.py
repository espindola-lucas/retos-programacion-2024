class Singleton:
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance
    
    def __init__(self, value=None):
        # esto evita la reinicialización de la clase
        if not hasattr(self, 'initialized'):
            self.value = value
            self.initialized = True

# Uso del Singleton
singleton1 = Singleton(10)
# print(singleton1.value)

singleton2 = Singleton(20)
# print(singleton2.value)

# print(singleton1 is singleton2)

class UserSession:
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(UserSession, cls).__new__(cls)
        return cls._instance
    
    def __init__(self, value=None):
        if not hasattr(self, 'initialized'):
            self.value = value
            self.initialized = True
    
    def assign_user(self, id, username, name, email):
        self.user_data = {
            "user_id": id,
            "username": username,
            "name": name,
            "email": email
        }
    
    def get_data_user(self):
        return self.user_data
    
    def clear_session(self):
        self.user_data = None
        

session = UserSession()
session.assign_user(1, 'lucas-username', 'lucas', 'lucas@gmail.com')
user_data = session.get_data_user()
print(user_data)

session.clear_session()
print(session.get_data_user())

another_session = UserSession()
print(session is another_session) 

print(another_session.get_data_user())