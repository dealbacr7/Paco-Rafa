import threading
import random
import time

aforo = threading.Semaphore(5)
paciencia_portero = True
dentro = 0
lock_datos = threading.Lock()
consumo = {i: 0 for i in range(1, 11)}

def madrileno(id):
    global paciencia_portero, dentro
    quiere_rebujito = True

    while quiere_rebujito and paciencia_portero:
        print(f"Madrileño {id} intenta entrar")
        time.sleep(1)
        
        aforo.acquire()
        
        if not paciencia_portero:
            aforo.release()
            break

        with lock_datos:
            dentro += 1
            consumo[id] += 1
            print(f"Madrileño {id} HA ENTRADO (Rebujito nro {consumo[id]}). Personas dentro: {dentro}")
        
        time.sleep(1)
        tiempo_bebiendo = random.randint(1, 5)
        time.sleep(tiempo_bebiendo)

        with lock_datos:
            dentro -= 1
            print(f"Madrileño {id} ha salido. Personas dentro: {dentro}")
        
        aforo.release()
        time.sleep(1)

        if random.random() <= 0.75:
            print(f"Madrileño {id} tiene sed y hara cola de nuevo")
            time.sleep(1.5)
        else:
            print(f"Madrileño {id} ya ha tenido suficiente y se va")
            quiere_rebujito = False

def portero_cansado():
    global paciencia_portero
    time.sleep(35)
    print("\n--- EL PORTERO SE HA HARTADO Y HA ECHADO LA LLAVE ---\n")
    paciencia_portero = False

hilos = []
threading.Thread(target=portero_cansado, daemon=True).start()

for i in range(1, 11):
    t = threading.Thread(target=madrileno, args=(i,))
    hilos.append(t)
    t.start()
    time.sleep(1)

for t in hilos:
    t.join()

print("\nESTADISTICAS DE LA FERIA:")
print("--------------------------")
for m_id, cantidad in consumo.items():
    print(f"Madrileño {m_id}: {cantidad} rebujitos")
print("--------------------------")
print("Fin de la simulacion")