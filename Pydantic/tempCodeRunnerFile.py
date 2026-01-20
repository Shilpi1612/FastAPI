from pydantic import BaseModel

class Patient(BaseModel):

    name : str
    age : int

def instert_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print('inserted')

def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print('updated')

patient_info = {'name': 'Shilpi', 'age': 25}

patient1 = Patient(**patient_info)

instert_patient_data(patient1)
