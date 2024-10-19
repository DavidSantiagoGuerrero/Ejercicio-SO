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
    def __init__(self, numero, id_hilo):
        threading.Thread.__init__(self)
        self.numero = numero
        self.id_hilo = id_hilo

    def run(self):
        resultado = calcular_fibonacci(self.numero)
        print(f"[Hilo {self.id_hilo}] Resultado: {resultado}")

def lanzar_hilos():
    cantidad_hilos = 8
    hilos = []
    tiempos_ejecucion = []

    for i in range(cantidad_hilos):
        print(f"Iniciando hilo {i}.")
        tiempo_inicial = time()
        hilo = HiloFibonacci(33, i)
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
