from hospital import Hospital
from department import Department
from Patient import Patient
from staff import Staff

if __name__ == "__main__":
    # 1. إنشاء المستشفى
    hospital = Hospital("City Hospital", "Cairo")

    # 2. إنشاء الأقسام
    cardiology = Department("Cardiology")
    pediatrics = Department("Pediatrics")

    # 3. إنشاء الموظفين
    doctor = Staff("Dr. Ahmed", 40, "Cardiologist")
    nurse = Staff("Mona", 28, "Pediatric Nurse")

    # 4. إنشاء المرضى
    patient1 = Patient("Ali", 55, "Hypertension")
    patient2 = Patient("Omar", 7, "Flu")

    # 5. إضافة الموظفين والمرضى للأقسام
    cardiology.add_staff(doctor)
    cardiology.add_patient(patient1)

    pediatrics.add_staff(nurse)
    pediatrics.add_patient(patient2)

    # 6. إضافة الأقسام للمستشفى
    hospital.add_department(cardiology)
    hospital.add_department(pediatrics)

    # 7. طباعة البيانات لاختبار التجربة
    print(f"=== Hospital: {hospital.name} ({hospital.location}) ===\n")

    for dept in hospital.departments_lst:
        print(f"--- Department: {dept.dept_name} ---")

        print("Staff:")
        for staff in dept.staff_lst:
            print(f"  • {staff.view_info()}")

        print("Patients:")
        for pt in dept.patient_lst:
            print(f"  • {pt.view_info()} | {pt.view_record()}")

        print()