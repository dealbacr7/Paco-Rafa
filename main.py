import threading
import random
import time

aforo = threading.Semaphore(5)

def madrileno(id):

    seguir = True

    while seguir:

        print(f"Madrileño {id} intenta entrar")

        aforo.acquire()

        print(f"Madrileño {id} HA ENTRADO")

        tiempo = random.randint(1, 5)
        time.sleep(tiempo)

        print(f"Madrileño {id} ha salido")

        aforo.release()

        # 75% probabilidad
        if random.random() > 0.75:
            seguir = False
            print(f"Madrileño {id} se va definitivamente")

        time.sleep(1)


hilos = []

for i in range(1, 11):
    t = threading.Thread(target=madrileno, args=(i,))
    hilos.append(t)
    t.start()
