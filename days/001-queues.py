from typing import Any

class QueueEmpty(Exception):
    """ Lista está vazia """

class Node:
    """ Elemento da lista onde será guardado o valor e o elemento seguinte """

    def __init__(self, value: Any):
        self.value = value
        self.next: Node = None

    def __str__(self) -> str:
        return str(self.value)

class Queue:
    """ Lista First In First Out (FIFO), no qual o primeiro valor adicionado será o primeiro a sair """

    def __init__(self) -> None:
        self.first = None
        self.last = None
        self.count = 0

    def __len__(self) -> int:
        return self.count

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if(not self.first): raise QueueEmpty
        elif(self.n > self.count): raise StopIteration

        toReturn = self.first
        for i in range(self.n):
            if(not toReturn.next): raise StopIteration
            toReturn = toReturn.next

        self.n += 1
        return toReturn

    def enqueue(self, value: Any):
        """ Adiciona um novo elemento de qualquer valor na lista """

        newNode = Node(value)

        if(not self.first):
            self.first = newNode
            self.last = newNode
        else:
            self.last.next = newNode
            self.last = newNode

        self.count += 1

    def dequeue(self):
        """ Retira o primeiro elemento da lista """

        if(not self.first): raise QueueEmpty

        temp = self.first
        self.first = self.first.next

        self.count -= 1
        return temp