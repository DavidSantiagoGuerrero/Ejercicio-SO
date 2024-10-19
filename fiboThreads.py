#Jhonier Mendez Bravo - 2372226
#David Santiago Guerrero Delgado - 2324594
#Cristian Daniel Guaza Mejia - 2372225

from time import time
import threading

def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

class FiboThread(threading.Thread):
    def __init__(self, nums, pid):
        threading.Thread.__init__(self)
        self.nums = nums
        self._pid = pid

    def run(self):
        resultado = []
        for n in self.nums:
            resultado.append(fibo(n))
        print(f"[Thread {self._pid}] Resultados: {resultado}")

def dividir_en(secuencia, divisiones):
    intervalos = []
    for i in range(0, len(secuencia), divisiones):
        chunk = secuencia[i:i+divisiones]  
        intervalos.append(chunk)
    return intervalos

def main_threads():
    secuencia = [i for i in range(144)]  

    num_hilos = 8  
    divisiones = len(secuencia) // num_hilos

    particion = dividir_en(secuencia, divisiones)

    print(f"Calculando el Fibonacci de {len(secuencia)} 

    hilos = []
    ts = time()

    for x in range(num_hilos):
        print(f"Iniciando hilo {x} con {len(particion[x])} elementos.")
        hilo = FiboThread(particion[x], x)
        hilo.start()
        hilos.append(hilo)

    for x in range(num_hilos):
        print(f"Esperando por hilo {x}")
        hilos[x].join()

    print(f"Tomo {time() - ts} segundos")

if __name__ == "__main__":
    main_threads()
