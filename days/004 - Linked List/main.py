from typing import Any

class EmptyLinkedList(Exception):
    ...

class Node:
    def __init__(self, data: Any) -> None:
        self.data = data
        self.next: Node = None

    def __str__(self) -> str:
        return str(self.data)

class LinkedList:
    def __init__(self) -> None:
        self.head: Node = None
        self.length = 0

    def __len__(self) -> int:
        return self.length

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if(not self.head): raise EmptyLinkedList

        currentNode = self.head
        for _ in range(self.n):
            if(not currentNode.next): raise StopIteration
            currentNode = currentNode.next

        self.n += 1
        return currentNode

    def push(self, data: Any):
        """ Adiciona um novo Node """

        if(not self.head):
            self.head = Node(data)

        else:
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode

        self.length += 1

    def insertAfter(self, prevNode: Node, data: Any):
        """ Adiciona um novo Node depois em seguida de outro já especificado """

        if(not self.head): raise EmptyLinkedList

        if(prevNode == None): raise ValueError('Previous Node can\'t be None')

        newNode = Node(data)
        newNode.next = prevNode.next
        prevNode.next = newNode

        self.length += 1

    def deleteNode(self, key: Any):
        """ Deleta um Node passando seu valor """

        if(not self.head): raise EmptyLinkedList
        if(self.head.data == key):
            self.head = self.head.next

        else:
            temp = self.head
            prev = None
            while(temp != None and temp.data != key):
                prev = temp
                temp = temp.next

            if(temp == None): return

            prev.next = temp.next

        self.length -= 1

    def deleteNodeInPosition(self, position: int):
        """ Deleta um Node passando sua posição """

        if(not self.head): raise EmptyLinkedList
        if(position == 0):
            self.head = self.head.next

            self.length -= 1

        else:
            prev = None
            for i, node in enumerate(self):
                if(i == position):
                    prev.next = node.next

                    self.length -= 1
                    return
                    
                prev = node

    def deleteList(self):
        """ Deleta toda a lista """

        self.head = None
        self.length = 0

    def search(self, data: Any) -> Node:
        """ Busca por um valor na lista """

        if(not self.head): raise EmptyLinkedList

        return self.__search(self.head, data)

    def __search(self, currentNode: Node, data: Any):
        """ Busca pelo valor de maneira recursiva """

        if(currentNode == None): return
        elif(currentNode.data == data): return currentNode

        return self.__search(currentNode.next, data)

    def inPosition(self, position: int) -> Node:
        """ Pega o Node que está na posição especificada """

        if(not self.head): raise EmptyLinkedList
        elif(position > self.length - 1): raise IndexError

        for i, v in enumerate(self):
            if(i == position): return v

    def hasLoop(self) -> bool:
        """ Detecta se a lista tem loop """

        if(not self.head or not self.head.next): return False

        fast = self.head
        slow = self.head
        while(fast.next != None and fast.next.next != None):
            fast = fast.next.next
            slow = slow.next

            if(slow == fast): return True
        return False