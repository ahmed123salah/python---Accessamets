class  Person:
    def __init__(self, name:str, age:int):
        
        self.name = name
        self.age = age
    def view_info(self):
        '''
        this function takes nothing from users and returns the name and age of the person in a formatted string.
        '''
        
        return f"Name: {self.name}, Age: {self.age}"
    





