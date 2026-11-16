# programacao-concorrente
Esse projeto explora três problemas centrais da programação concorrente: o Jantar dos Filósofos, condições de corrida controladas por semáforos e o tratamento de deadlock.

## Parte 1
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

