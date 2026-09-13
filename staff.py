from person import Person

class Staff(Person):
    def __init__(self, name: str, age: int, position: str):
        super().__init__(name, age)
        self.position = position

    def view_info(self) -> str:
        '''
        this function overrides the parent method to return person info along with position
        '''
        return f"{super().view_info()}, Position: {self.position}"