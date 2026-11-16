import threading
import time

LOCK_A = threading.Lock()
LOCK_B = threading.Lock()

lock_tela = threading.Lock()


def escrever(mensagem):
    lock_tela.acquire()
    print(mensagem)
    lock_tela.release()


def tarefa_1():
    escrever("Thread 1: tentando adquirir LOCK_A...")
    LOCK_A.acquire()
    escrever("Thread 1: adquiriu LOCK_A")

    time.sleep(0.05)

    escrever("Thread 1: tentando adquirir LOCK_B...")
    LOCK_B.acquire()
    escrever("Thread 1: adquiriu LOCK_B")

    escrever("T1 concluiu")

    LOCK_B.release()
    LOCK_A.release()


def tarefa_2():
    escrever("Thread 2: tentando adquirir LOCK_B...")
    LOCK_B.acquire()
    escrever("Thread 2: adquiriu LOCK_B")

    time.sleep(0.05)

    escrever("Thread 2: tentando adquirir LOCK_A...")
    LOCK_A.acquire()
    escrever("Thread 2: adquiriu LOCK_A")

    escrever("T2 concluiu")

    LOCK_A.release()
    LOCK_B.release()


t1 = threading.Thread(target=tarefa_1, name="Thread-1")
t2 = threading.Thread(target=tarefa_2, name="Thread-2")

t1.start()
t2.start()

t1.join(timeout=2)
t2.join(timeout=2)

if t1.is_alive() or t2.is_alive():
    escrever("\n[DEADLOCK DETECTADO] As threads ficaram bloqueadas esperando uma pela outra:")
    for t in threading.enumerate():
        escrever(f" - Thread ativa: {t.name} (alive={t.is_alive()})")