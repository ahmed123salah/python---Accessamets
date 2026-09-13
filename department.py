from Patient import Patient
from staff import Staff
class Department:
    '''
    
    
    '''
    def __init__(self, dept_name:str):
        self.dept_name = dept_name
        self.patient_lst: list[Patient]=[]
        self.staff_lst: list[Staff] = []
        
    def add_patient(self,patient:Patient):
        self.patient_lst.append(patient)

    def add_staff(self, staff: Staff):
        self.staff_lst.append(staff)
        