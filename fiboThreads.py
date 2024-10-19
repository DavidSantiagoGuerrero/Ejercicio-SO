#Jhonier Mendez Bravo - 2372226
#David Santiago Guerrero Delgado - 2324594
#Cristian Daniel Guaza Mejia - 2372225

from time import time
import threading

def calcular_fibonacci(numero):
    if numero == 0:
        return 0
    elif numero == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, numero + 1):
            a, b = b, a + b
        return b

class HiloFibonacci(threading.Thread):
    def __init__(self, elementos, id_hilo):
        threading.Thread.__init__(self)
        self.elementos = elementos
        self.id_hilo = id_hilo

    def run(self):
        resultados = [calcular_fibonacci(n) for n in self.elementos]
        print(f"[Hilo {self.id_hilo}]: {resultados}")

def dividir_vector(vector, num_partes):
    tamaño_parte = len(vector) // num_partes
    return [vector[i:i + tamaño_parte] for i in range(0, len(vector), tamaño_parte)]

def lanzar_hilos():
    vector = [33] * 144
    num_hilos = 8
    particiones = dividir_vector(vector, num_hilos)

    hilos = []
    tiempos_ejecucion = []

    print(f"Calculando Fibonacci de cada elemento del vector de tamaño {len(vector)}.")

    for i in range(num_hilos):
        print(f"Hilo {i} con {len(particiones[i])} elementos.")
        tiempo_inicial = time()
        hilo = HiloFibonacci(particiones[i], i)
        hilo.start()
        hilos.append(hilo)
        hilo.join()
        tiempo_final = time() - tiempo_inicial
        tiempos_ejecucion.append(tiempo_final)
        print(f"Se tardó: {tiempo_final}")

    mayor = max(tiempos_ejecucion)
    menor = min(tiempos_ejecucion)
    promedio = sum(tiempos_ejecucion) / len(tiempos_ejecucion)

    print(f"Mayor tiempo: {mayor}")
    print(f"Menor tiempo: {menor}")
    print(f"Promedio: {promedio:.8f}")

if __name__ == "__main__":
    lanzar_hilos()
