import os
import csv
import logging
import statistics
import pydicom
import pandas as pd

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def list_folder_contents(path):
    try:
        if not os.path.isdir(path):
            raise FileNotFoundError(f"El path '{path}' no existe o no es un directorio.")
        
        contents = os.listdir(path)
        logging.info(f"Número de elementos en '{path}': {len(contents)}")
        for item in contents:
            logging.info(item)
    except Exception as e:
        logging.error(e)

def read_csv_file(path, filename):
    try:
        file_path = os.path.join(path, filename)
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"El archivo en la ubicación '{file_path}' no existe.")
        if not file_path.endswith('.csv'):
            raise ValueError(f"el archivo'{file_path}' no tiene el formato CSV.")
        
        df = pd.read_csv(file_path)
        if df.empty:
            raise ValueError(f"El archivo '{file_path}' está vacío.")
        
            
        columns = df.columns
        logging.info(f"Número de columnas: {len(columns)}")
        logging.info(f"Nombres de las columnas: {df.columns.to_list()}")
        logging.info(f"Numero de filas: {len(df)}")
        
        for column in columns:
            if pd.api.types.is_numeric_dtype(df[column]):
                avg = df[column].mean()
                std_dev = df[column].std()
                logging.info(f"columna '{column}': Promedio={avg:.2f}, Desviación={std_dev:.2f}")
            else:
                logging.info(f"La columna '{column}' no contiene datos númericos.")
                    
    except Exception as e:
        logging.error(e)

def read_dicom_file(path, filename, *tags):
    try:
        file_path = os.path.join(path, filename)
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"El archivo '{file_path}' no existe.")
        
        ds = pydicom.dcmread(file_path)
        logging.info(f"Nombre del Paciente: {ds.get('PatientName', 'N/A')}")
        logging.info(f"Fecha del Estudio: {ds.get('StudyDate', 'N/A')}")
        logging.info(f"Modalidad: {ds.get('Modality', 'N/A')}")
        
        for tag in tags:
            try:
                tag_value = ds.get(tag, 'N/A')
                logging.info(f"Etiqueta {hex(tag)}: {tag_value}")
            except Exception as tag_error:
                logging.error(f"Error al leer la etiqueta {hex(tag)}: {tag_error}")
    
    except Exception as e:
        logging.error(f"Error al leer el archivo DICOM: {e}")



# Lista el contenido de la carpeta
list_folder_contents('./File-Handling-and-Array-Operations/test')

# Lectura de archivo CSV
read_csv_file('./', '.sample-01-csv.csv')

# Lectura de archivo DICOM
read_dicom_file('./', 'sample-02-dicom.dcm', 0x00080016, 0x00100010)
