import logging
import pydicom
from datetime import datetime

# Configuración del logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

class PatientRecord:
    def __init__(self, name, age, birth_date, sex, weight, patient_id, id_type):
        self.name = name
        self.age = age
        self.birth_date = birth_date
        self.sex = sex
        self.weight = weight
        self.patient_id = patient_id
        self.id_type = id_type
        self.diagnosis = None

    # Métodos para establecer y obtener información
    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_age(self, age):
        self.age = age

    def get_age(self):
        return self.age

    def set_birth_date(self, birth_date):
        self.birth_date = birth_date

    def get_birth_date(self):
        return self.birth_date

    def set_sex(self, sex):
        self.sex = sex

    def get_sex(self):
        return self.sex

    def set_weight(self, weight):
        self.weight = weight

    def get_weight(self):
        return self.weight

    def set_patient_id(self, patient_id):
        self.patient_id = patient_id

    def get_patient_id(self):
        return self.patient_id

    def set_id_type(self, id_type):
        self.id_type = id_type

    def get_id_type(self):
        return self.id_type

    # Método para actualizar el diagnóstico
    def update_diagnosis(self, new_diagnosis):
        self.diagnosis = new_diagnosis
        logging.info(f"Diagnostico actualizado a: {new_diagnosis}")

    def __str__(self):
        return (f"PatientRecord(Name: {self.name}, Age: {self.age}, Birth Date: {self.birth_date}, "
                f"Sex: {self.sex}, Weight: {self.weight}, Patient ID: {self.patient_id}, ID Type: {self.id_type})")


class StudyRecord(PatientRecord):
    def __init__(self, name, age, birth_date, sex, weight, patient_id, id_type):
        super().__init__(name, age, birth_date, sex, weight, patient_id, id_type)
        self.modality = None
        self.study_date = None
        self.study_time = None
        self.study_instance_uid = None
        self.series_number = None
        self.number_of_frames = None

    # Métodos para establecer y obtener información del estudio
    def set_modality(self, modality):
        self.modality = modality

    def get_modality(self):
        return self.modality

    def set_study_date(self, study_date):
        self.study_date = study_date

    def get_study_date(self):
        return self.study_date

    def set_study_time(self, study_time):
        self.study_time = study_time

    def get_study_time(self):
        return self.study_time

    def set_study_instance_uid(self, study_instance_uid):
        self.study_instance_uid = study_instance_uid

    def get_study_instance_uid(self):
        return self.study_instance_uid

    def set_series_number(self, series_number):
        self.series_number = series_number

    def get_series_number(self):
        return self.series_number

    def set_number_of_frames(self, number_of_frames):
        self.number_of_frames = number_of_frames

    def get_number_of_frames(self):
        return self.number_of_frames

    # Método para cargar detalles de un archivo DICOM
    def load_from_dicom(self, dicom_file_path):
        dicom_data = pydicom.dcmread(dicom_file_path)
        self.modality = dicom_data.Modality
        self.study_date = dicom_data.StudyDate
        self.study_time = dicom_data.StudyTime
        self.study_instance_uid = dicom_data.StudyInstanceUID
        self.series_number = dicom_data.SeriesNumber
        self.number_of_frames = getattr(dicom_data, 'NumberOfFrames', 'N/A')

    # Sobreescribir __str__ para mostrar toda la información del paciente y del estudio
    def __str__(self):
        return (super().__str__() +
                f"\nStudyRecord(Modality: {self.modality}, Study Date: {self.study_date}, "
                f"Study Time: {self.study_time}, Study Instance UID: {self.study_instance_uid}, "
                f"Series Number: {self.series_number}, Number of Frames: {self.number_of_frames})")
