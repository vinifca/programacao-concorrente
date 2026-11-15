import threading
import time

qtd_filosofos = 5

garfos = []
for i in range(qtd_filosofos):
    garfos.append(threading.Lock())

lock_tela = threading.Lock()


def escrever(mensagem):
    lock_tela.acquire()
    print(mensagem)
    lock_tela.release()


def filosofo(numero):
    esquerda = numero
    direita = (numero + 1) % qtd_filosofos

    comeu = 0
    while comeu < 3:
        escrever(f"Filosofo {numero} esta pensando")
        time.sleep(1)

        escrever(f"Filosofo {numero} esta com fome")

        garfos[esquerda].acquire()
        escrever(f"Filosofo {numero} pegou o garfo {esquerda} e espera o garfo {direita}")

        garfos[direita].acquire()

        escrever(f"Filosofo {numero} esta comendo")
        time.sleep(1)

        garfos[direita].release()
        garfos[esquerda].release()

        comeu += 1

    escrever(f"Filosofo {numero} terminou")


threads = []
for i in range(qtd_filosofos):
    t = threading.Thread(target=filosofo, args=(i,))
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()

print("Todos os filosofos terminaram.")