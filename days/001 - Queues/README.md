# Queue First In First Out

![Queue](https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Data_Queue.svg/300px-Data_Queue.svg.png)

## Definição na [Wikipédia](https://pt.wikipedia.org/wiki/FIFO)
Ciência da Computação, algoritmo de fila simples, FIFO (do inglês: first in, first out , "primeiro a entrar, primeiro a sair", "PEPS") ou FCFS (do inglês: first come, first served , "primeiro a chegar, primeiro a ser servido") é um algoritmo de escalonamento para estruturas de dados do tipo fila. Apresenta o seguinte critério: o primeiro elemento a ser retirado é o primeiro que tiver sido inserido, é um algoritmo de escalonamento não preemptivo que entrega a CPU os processos pela ordem de chegada. Ele executa o processo como um todo do inicio ao fim não interrompendo o processo executado até ser finalizado, então quando um novo processo chega e existe um ainda em execução ele vai para uma fila de espera. Esta fila de espera nada mais é do que uma fila que organiza os processos que chegam até eles serem atendidos pela CPU.

## O que entendi
Seria apenas um tipo de algoritmo de fila, no qual **o primeiro valor a ser inserido na fila, seria o primeiro a sair** ( Só imaginar uma fila normal que nós fazemos, como uma fila de banco. O primeiro que chegar na fila será o primeiro a ser atendido ). Dependendo do tipo de uso, não seria o melhor de se usar, já que é muito sensível a ordem de chegada de cada processo, não garantindo um tempo de resposta muito rápido.

```python
'''
Exemplo:

Vamos fingir que essa lista representa a fila:
    Atrás -> [] <- Frente

É adicionado ( enqueue ) um valor x:
    [x]

Em seguida é adicionado ( enqueue ) outro valor y:
    [y, x]

Quando retirarmos ( dequeue ) um valor da fila, o primeiro que entrou será retirado:
    [y] -> x

Quando retirarmos ( dequeue ) outro valor, irá retirar o seguinte:
    [] -> y
'''
```