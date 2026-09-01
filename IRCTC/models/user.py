class User:
    
    def __init__(self,name,email,age,password):
        self.name=name
        self.email=email
        self.__age=age
        self.password=password
        
    def show_profile(self):
        print("\n========== PROFILE ==========")
        print("Name:", self.name)
        print("Email:", self.email)
        print("Age:", self.age)
        print("=============================")
    
    @property
    def age(self):
        return self.__age
        
    @age.setter
    def set_age(self, value):

        if value < 0:
            print("Age cannot be negative.")
            return

        self.__age = value
    
    
        
    
    def greet(self):
        print(f"Welcome {self.name} to IRCTC!")
        
    def search_train(self,source,destination):
        print(f"Searching trains from {source} to {destination}")
        
    