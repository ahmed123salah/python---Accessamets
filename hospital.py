from department import Department

class Hospital:
    def __init__(self, name: str, location: str):
        self.name = name
        self.location = location
        self.departments_lst: list[Department] = []

    def add_department(self, department: Department) -> None:
        self.departments_lst.append(department)