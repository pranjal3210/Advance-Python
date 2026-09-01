from models.user import User

class AuthService:

    def __init__(self):
        self.users = []

    def register(self):
        print("\n========== REGISTER ==========")

        name = input("Enter your name: ")
        email = input("Enter your email: ")
        
        for user in self.users:
            if user.email == email:
                print("Email already registered.")
                return
        
        age = int(input("Enter your age: "))
        password = input("Enter your password: ")
        
        user=User(name,email,age,password)
        self.users.append(user)

        print("\nRegistration successful!")
        
        
    def login(self):

        print("\n========== LOGIN ==========")

        email = input("Enter your email: ")
        password = input("Enter your password: ")

        for user in self.users:

            if user.email == email and user.password == password:
                print(f"\nWelcome, {user.name}!")
                return user

        print("\nInvalid email or password.")
        return None