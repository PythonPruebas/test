import threading
import time

def print_even_numbers():
    for i in range(2, 201, 2):
        print(f"Even: {i}")
        time.sleep(0.5)

def print_odd_numbers():
    for i in range(1, 200, 2):
        print(f"Odd: {i}")
        time.sleep(0.5)

# Crear threads para números pares e impares
even_thread = threading.Thread(target=print_even_numbers)
odd_thread = threading.Thread(target=print_odd_numbers)

# Iniciar los threads
even_thread.start()
odd_thread.start()

# Esperar a que los threads finalicen
even_thread.join()
odd_thread.join()
