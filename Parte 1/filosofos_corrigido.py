import threading
import time

N = 5

garfos = []
for i in range(N):
    garfos.append(threading.Lock())

estado = []
for i in range(N):
    estado.append("pensando")

lock_tela = threading.Lock()


def escrever(mensagem):
    lock_tela.acquire()
    print(mensagem)
    lock_tela.release()


def filosofo(p):
    garfo_esquerda = p
    garfo_direita = (p + 1) % N

    left = min(garfo_esquerda, garfo_direita)
    right = max(garfo_esquerda, garfo_direita)

    comeu = 0
    while comeu < 3:
        estado[p] = "pensando"
        escrever(f"Filosofo {p} esta pensando")
        time.sleep(1)

        estado[p] = "com fome"
        escrever(f"Filosofo {p} esta com fome")

        garfos[left].acquire()
        escrever(f"Filosofo {p} pegou o garfo {left} e espera o garfo {right}")

        garfos[right].acquire()

        estado[p] = "comendo"
        escrever(f"Filosofo {p} esta COMENDO com os garfos {left} e {right}")
        time.sleep(1)

        garfos[right].release()
        garfos[left].release()

        estado[p] = "pensando"
        comeu += 1

    escrever(f"Filosofo {p} terminou")


filosofos = []
for p in range(N):
    t = threading.Thread(target=filosofo, args=(p,))
    filosofos.append(t)

for t in filosofos:
    t.start()

for t in filosofos:
    t.join()

print("Todos os filosofos terminaram.")