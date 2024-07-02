# uso incorrecto del SRP

class UserWithoutSRP:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        
    def save_user(self):
        print(f"El usuario {self.name} se guardo exitosamente.")
        
    def print_report(self):
        print(f"Imprimiendo reporte para {self.name} con mail {self.email}")

user = UserWithoutSRP('Lucas', 'lucas@gmail.com')
# user.save_user()
# user.print_report()

# uso correcto del SRP

class CreateUserWithSRP:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        
class SaveUserWithSRP():
    def __init__(self, user):
        self.name = user.name
        self.email = user.email
        
    def save_user(self):
        print(f"El usuario {self.name} se guardo exitosamente.")

class PrintUserWithSRP():  
    def __init__(self, user):
        self.name = user.name
        self.email = user.email

    def print_report(self):
        print(f"Imprimiendo reporte para {self.name} con mail {self.email}")

user = CreateUserWithSRP('Lucas', 'lucas@gmail.com')
save = SaveUserWithSRP(user)
save.save_user()
showUser = PrintUserWithSRP(save)
showUser.print_report()