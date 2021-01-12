# Linked List

![Linked List](https://media.geeksforgeeks.org/wp-content/cdn-uploads/gq/2013/03/Linkedlist.png)

## Definição da [Wikipédia](https://en.wikipedia.org/wiki/Linked_list#:~:text=In%20computer%20science%2C%20a%20linked,which%20together%20represent%20a%20sequence.)
Na ciência da computação, uma Linked List é uma coleção linear de elementos de dados cuja ordem não é dada por sua colocação física na memória. Em vez disso, cada elemento aponta para o próximo. É uma estrutura de dados que consiste em uma coleção de nós que juntos representam uma sequência. Em sua forma mais básica, cada nó contém: dados e uma referência (em outras palavras, um link) para o próximo nó na sequência. Essa estrutura permite a inserção ou remoção eficiente de elementos de qualquer posição na sequência durante a iteração. Variantes mais complexas adicionam links adicionais, permitindo a inserção ou remoção mais eficiente de nós em posições arbitrárias. Uma desvantagem das listas vinculadas é que o tempo de acesso é linear (e difícil de pipeline). O acesso mais rápido, como o acesso aleatório, não é viável. Os arrays têm melhor localidade de cache em comparação com listas vinculadas.

## O que entendi
Cada Nó ( Node ) **tem um valor e uma referência ao próximo Nó** ( Mesma estrutura do Nó em Queues ). Tendo uma estrutura dessa forma, é preferivel usá-la quando **você não saber o tamanho máximo da lista**; **quando você não precisa acessar aleatóriamente algum elemento do array** ou também, **quando precisa de uma remoção de elementos mais eficientes**, já que, diferente de arrays, ele não trabalha com índices, sendo assim, não precisa realocar todos os elementos da índices diferentes.

