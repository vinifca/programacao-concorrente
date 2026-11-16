import threading
import time

T = 8
M = 200000

count = 0


def tarefa():
    global count
    for i in range(M):
        temp = count

        calculo = 0
        for j in range(5):
            calculo = calculo + j

        count = temp + 1


inicio = time.time()

threads = []
for i in range(T):
    t = threading.Thread(target=tarefa)
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()

fim = time.time()
tempo_total = fim - inicio

esperado = T * M
print(f"Esperado = {esperado}")
print(f"Obtido = {count}")
print(f"Incrementos perdidos = {esperado - count}")
print(f"Tempo = {tempo_total:.4f} segundos")