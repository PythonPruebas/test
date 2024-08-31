from object_oriented_programming import *

patient = StudyRecord("John Doe", 45, "1978-04-12", "M", 75, "123456", "MRN")

# Actualizar y obtener información del paciente
patient.update_diagnosis("Hipertensión")

# Cargar información del estudio desde un archivo DICOM
patient.load_from_dicom("sample-02-dicom.dcm")

# Imprimir toda la información del paciente y del estudio
print(patient)