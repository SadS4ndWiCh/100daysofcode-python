class Node:
    """ Valores guardados na árvore """

    def __init__(self, value: int) -> None:
        self.value = value
        self.left: Node = None
        self.right: Node = None

class BinarySearchTree:
    def __init__(self) -> None:
        self.root: Node = None

    @property
    def height(self) -> int:
        """ Tamanho da árvore """

        if(self.root == None): return 0
        
        return self._height(self.root, 0)

    def _height(self, node: Node, height: int):
        if(node == None): return height

        leftHeight = self._height(node.left, height + 1)
        rightHeight = self._height(node.right, height + 1)

        return max(leftHeight, rightHeight)

    def insert(self, value: int):
        """ Insere um valor na árvore """

        if(self.root == None):
            self.root = Node(value)
        
        else:
            self._insert(self.root, value)

    def _insert(self, node: Node, value: int):
        """ Metodo recursivo para a inserção do valor """

        if(node == None):
            return Node(value)

        if(node.value > value):
            if(node.left == None):
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        
        elif(node.value < value):
            if(node.right == None):
                node.right = Node(value)
            else:
                self._insert(node.right, value)

    def print_in_order(self):
        """ Printa os valores árvore em order crescente """

        self._print_in_order(self.root)

    def _print_in_order(self, node: Node):
        """ Metodo recursivo para printar os valores em ordem crescente """

        if(node == None): return

        self._print_in_order(node.left)
        print(node.value)
        self._print_in_order(node.right)

    def print_pre_order(self):
        """ Printa os valores da árvore em sequência """

        if(self.root == None): return

        self._print_pre_order(self.root)

    def _print_pre_order(self, node: Node):
        """ Metodo recursivo para printar os valores na sequência """

        if(node == None): return

        print(node.value)
        self._print_pre_order(node.left)
        self._print_pre_order(node.right)

    def search(self, value: int) -> bool:
        """ Busca por um valor na árvore e retorna um True se encontrar, caso contrário, retorna False """

        if(self.root == None): return False

        return self._search(self.root, value)

    def _search(self, node: Node, value: int):
        """ Metodo recursivo para fazer a busca de um valor """

        if(node == None): return False

        if(node.value == value): return True

        if(node.value > value):
            return self._search(node.left, value)
        
        elif(node.value < value):
            return self._search(node.right, value)

        return False