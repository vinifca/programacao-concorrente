# programacao-concorrente
Esse projeto explora três problemas centrais da programação concorrente: o Jantar dos Filósofos, condições de corrida controladas por semáforos e o tratamento de deadlock.

Integrantes: Gabriel Tomé dos Santos, Pedro Pimentel Moura e Vinícius Felde Caetano Alves
Linguagem: Python

## Parte 1 (Vinícius)
N filósofos em uma mesa redonda alternam entre pensar e comer, cada um com dois garfos em cada lado. O deadlock ocorre se todos pegarem o garfo esquerdo juntos e esperarem eternamente pelo direito.

A solução implementada é a de hierarquia de recursos e a condição de Coffman que ela nega é espera circular. Exigir que cada garfo receba um número diferente e fazer com que o filósofo sempre pegue o menor garfo primeiro evita o ciclo vicioso.

O progresso é garantido uma vez que sempre terá um filósofo que não comerá enquanto os outros 4 comem. A justiça é garantida pois um filósofo que tenta pegar um garfo ocupado garante seu lugar na fila para usá-lo depois.

```text
procedimento filosofo(p):
    primeiro <- min(p, (p + 1) mod N);  segundo <- max(p, (p + 1) mod N)
    enquanto verdadeiro:
        pensar()
        adquirir(garfos[primeiro]);  adquirir(garfos[segundo])
        comer()
        liberar(garfos[segundo]);    liberar(garfos[primeiro])

```

## Parte 2 (Pimentel)

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

## Parte 2 (Gabriel)

## Objetivo

Demonstrar um deadlock entre duas threads que utilizam dois locks compartilhados e apresentar uma correção por meio de uma hierarquia global de aquisição de recursos.

### Condições de Coffman


Exclusão mútua: cada lock só pode ser utilizado por uma thread.

Manter-e-esperar: cada thread mantém um lock enquanto espera pelo outro.

Não preempção: os locks só são liberados pelas próprias threads.

Espera circular: cada thread espera pelo lock que está com a outra.

### Versão corrigida

No arquivo parte 3/sem_deadlock.py, as duas threads adquirem os locks na mesma ordem: primeiro LOCK_A e depois LOCK_B.

Essa solução quebra a condição de espera circular, evitando o deadlock.
