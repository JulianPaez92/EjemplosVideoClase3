import threading

contador = 0

lock = threading.Lock()

def funcion():
    global contador
    for i in range(1000000):
        contador += 1

def hilo1():
    lock.acquire()
    try:
        funcion()
    finally:
        lock.release()

def hilo2():
    lock.acquire()
    try:
        funcion()
    finally:
        lock.release()

def hilo3():
    lock.acquire()
    try:
        funcion()
    finally:
        lock.release()
print("Inicio programa principal")
print("Valor Inicial: " + str(contador))

thread_1=threading.Thread(target=hilo1)
thread_2=threading.Thread(target=hilo2)
thread_3=threading.Thread(target=hilo3)



thread_1.start()
thread_2.start()
thread_3.start()

thread_1.join()
thread_2.join()
thread_3.join()

print("Valor Final: " + str(contador))




