import threading
import json
import os
import logging
from concurrent.futures import ThreadPoolExecutor

# Configuración de logging
logging.basicConfig(
    filename='data_processing.log',
    level=logging.INFO,
    format='%(asctime)s - %(threadName)s - %(levelname)s - %(message)s'
)

# Función para procesar cada elemento del JSON
def process_element(element_id, element_data):
    data_lines = element_data['data']
    flat_data = [int(num) for line in data_lines for num in line.split()]
    
    # Calcular promedio antes de la normalización
    avg_before = sum(flat_data) / len(flat_data)
    
    # Normalización
    max_value = max(flat_data)
    normalized_data = [x / max_value for x in flat_data]
    
    # Calcular promedio después de la normalización
    avg_after = sum(normalized_data) / len(normalized_data)
    
    # Log y print de los resultados
    logging.info(f"Element ID: {element_id}, Average Before: {avg_before}, Average After: {avg_after}, Size: {len(flat_data)}")
    print(f"Element ID: {element_id}, Average Before: {avg_before}, Average After: {avg_after}, Size: {len(flat_data)}")

# Función principal que lee el JSON y crea threads
def main(folder_path, json_filename):
    json_file_path = os.path.join(folder_path, json_filename)
    
    with open(json_file_path, 'r') as file:
        data = json.load(file)
    
    # Limitar a 4 threads concurrentes
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = []
        for element_id, element_data in data.items():
            futures.append(executor.submit(process_element, element_id, element_data))
        
        # Esperar a que todos los threads terminen
        for future in futures:
            future.result()

# Llamada a la función principal con la ruta de la carpeta y el nombre del archivo JSON
main('./', 'sample-03-00-json.json')
