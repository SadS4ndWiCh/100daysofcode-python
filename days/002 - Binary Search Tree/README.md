# Binary Search Tree ( Árvore Binária de Busca )


<a title="No machine-readable author provided. Dcoetzee assumed (based on copyright claims)., Public domain, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Binary_search_tree.svg">
<img
    width="256"
    alt="Binary search tree"
    src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Binary_search_tree.svg/256px-Binary_search_tree.svg.png"
    style="background-color: white;">
</a>

## Definição na [Wikipédia](https://pt.wikipedia.org/wiki/%C3%81rvore_bin%C3%A1ria_de_busca)
Em Ciência da computação, uma **árvore binária de busca** (ou árvore binária de pesquisa) é uma estrutura de dados de árvore binária **baseada em nós**, onde todos os **nós da sub-árvore esquerda possuem um valor numérico inferior ao nó raiz** e todos os **nós da sub-árvore direita possuem um valor superior ao nó raiz** (esta é a forma padrão, podendo as subárvores serem invertidas, dependendo da aplicação).

## O que entendi
Basicamente, uma estrutura de dados onde **cada valor representa um nó**, no qual **cada nó há uma sub-árvore na esquerda e na direita**. Se o **valor do nó for inferior ao valor do nó anterior - ou melhor, o 'pai' do nó -, será adicionado ao lado esquerdo**, caso contrário, **se for maior que o valor do nó anterior, será adicionado ao lado direito**.

```python
'''
Exemplo:

Temos uma árvore que o valor raiz é 2.
 - Ao adicionar o valor 1, por ele ser menor que 2, logo ele vai para a esquerda:
  
  2 -> Raiz da árvore ( Pai do 1 )
 /
1

 - Ao Adicionar o valor 5, por ele ser maior que 2, logo ele vai para a direita:

  2 -> Raiz da árvore ( Pai do 1 e 5 )
 / \
1   5

 - Ao adicionar o valor 4, por ele ser maior que 2, logo ele vai para a direira.
 Mas na direita já há um valor ( 5 ) que é uma sub-árvore, ai apenas fazemos a mesma lógica que fizemos com a raiz.
 O valor 4 é menor que o valor 5, então ele vai para a esquerda:

  2 -> Raiz da árvore ( Pai do 1 e 5 )
 / \
1   5 ( Pai do 4 )
   /
  4
'''
```

## <a name='uses'></a> Alguns usos do Binary Tree

 - [Binary Space Partition](http://en.wikipedia.org/wiki/Binary_space_partitioning): Usado em quase todos jogos 3D para determinar quais objetos precisam ser renderizados
 - [Binary Tries](http://en.wikipedia.org/wiki/Radix_tree): Usado em quase todos roteadores de alta largura de banda para armazenar tabelas de roteadores.
 - [Huffman Coding Tree (Chip Uni)](http://en.wikipedia.org/wiki/Huffman_coding): Usado em algoritimos de comprenssão, como aqueles usados pelos formatos de arquivo .jpeg e .mp3
 - Entre outros...

### Credito
 - A parte de [**Alguns usos do Binary Tree**](#uses) foi retidado de uma [respota](https://stackoverflow.com/a/2200588/14038725) no Stack Overflow.