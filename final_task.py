# 1. Base Class: Person
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def view_info(self) -> str:
        return f"Name: {self.name}, Age: {self.age}"


# 2. Derived Class: Patient (inherits from Person)
class Patient(Person):
    def __init__(self, name: str, age: int, medical_record: str):
        super().__init__(name, age)
        self.medical_record = medical_record

    def view_record(self) -> str:
        return f"Medical Record for {self.name}: {self.medical_record}"



class Staff(Person):
    def __init__(self, name: str, age: int, position: str):
        super().__init__(name, age)
        self.position = position

    
    def view_info(self) -> str:
        return f"Staff Name: {self.name}, Age: {self.age}, Position: {self.position}"


# 4. Class: Department
class Department:
    def __init__(self, name: str):
        self.name = name
        self.patients = []  
        self.staff_members = []  
    def add_patient(self, patient: Patient) -> None:
        self.patients.append(patient)

    def add_staff(self, staff_member: Staff) -> None:
        self.staff_members.append(staff_member)



class Hospital:
    def __init__(self, name: str, location: str):
        self.name = name
        self.location = location
        self.departments = []  

    def add_department(self, department: Department) -> None:
        self.departments.append(department)
        

hospital = Hospital(name="Grand Hospital", location="Cairo, Egypt")


cardiology = Department(name="Cardiology")       
neurology = Department(name="Neurology")         


hospital.add_department(cardiology)
hospital.add_department(neurology)


doc1 = Staff(name="Dr. Ahmed", age=40, position="Cardiologist")
doc2 = Staff(name="Dr. Sarah", age=35, position="Neurologist")


cardiology.add_staff(doc1)
neurology.add_staff(doc2)


patient1 = Patient(name="Ali Hassan", age=28, medical_record="Recovers from surgery")
patient2 = Patient(name="Mona Mohamed", age=50, medical_record="High blood pressure")


cardiology.add_patient(patient1)
cardiology.add_patient(patient2)

print(f"=== Hospital: {hospital.name} ({hospital.location}) ===")

for dept in hospital.departments:
    print(f"\n--- Department: {dept.name} ---")
    
    print("Staff Members:")
    for staff in dept.staff_members:
        print(f"  - {staff.view_info()}")  
        
    print("Patients:")
    for patient in dept.patients:
        print(f"  - {patient.view_info()}")     
        print(f"    {patient.view_record()}")    