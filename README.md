# programacao-concorrente
Esse projeto explora três problemas centrais da programação concorrente: o Jantar dos Filósofos, condições de corrida controladas por semáforos e o tratamento de deadlock.

## Parte 2

### Objetivo

Demonstrar uma condição de corrida e como isso pode ser evitado usando um semáforo. Utilizamos 8 threads cada uma realizando 200.000 incrementos em um contador compartilhado, com um resultado esperado de 1.600.000.

### Discussão

- **Sem sincronização:** Duas threads podem ler o mesmo valor do contador e sobrescrever o incremento uma da outra, causando uma condição de corrida e perda de incrementos.

- **Com semáforo:** O `Semaphore(1)` permite que apenas uma thread por vez atualize o contador. O `try...finally` garante a liberação do semáforo, mantendo o resultado correto.

- **Throughput:** Sem sincronização o programa levou 0,2696s enquanto com semáforo levou 1,6750s. Essa diferença ocorre porque as threads precisam esperar umas pelas outras. O semáforo do Python não garante uma fila FIFO.

- **Visibilidade e ordenação:** A sincronização garante que as threads acessem os valores atualizados, em java isso ocorre pela relação *happens-before* e em Python pelos mecanismos de sincronização do semáforo.

### Resultados

| Versão | Teste | Esperado | Obtido | Tempo |
|---|---|---|---|---|
| Sem sync | 1 | 1.600.000 | 528.388 | 0,2696s |
| Sem sync | 2 | 1.600.000 | 554.788 | 0,2562s |
| Sem sync | 3 | 1.600.000 | 856.935 | 0,2646s |
| Com semáforo | 1 | 1.600.000 | 1.600.000 | 1,6750s |
| Com semáforo | 2 | 1.600.000 | 1.600.000 | 1,6642s |
| Com semáforo | 3 | 1.600.000 | 1.600.000 | 1,6636s |
