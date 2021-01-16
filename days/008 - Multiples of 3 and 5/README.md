# Multiples of 3 and 5 - Project Euler ( Problem 1 )

Primeiramente dizendo que, nesses 100DaysOfCode irei também resolver alguns problemas do [Project Euler](https://projecteuler.net/). Não irei colocar todos aqui, talvez faça apenas um repositório apenas para eles. Mas para começar, fazerei esse mais simples primeiro, e outros colocados aqui poderão ser aqueles no qual tive mais dificuldade - ou não também.

## Enunciado
**Se tivermos uma lista de números naturais abaixo de 10 sendo eles multiplos de 3 ou 5, teremos o número 3, 5, 6 e 9. A soma deles resulta em 23. Encontre a soma dos multiplos 3 ou 5 abaixo de 1000**

### Código
```python
def sumMultiplesOf3And5(below: int) -> int:
    return sum([x for x in range(below) if x % 3 == 0 or x % 5 == 0])
```

### Explicação
```python
sum([x for x in range(below) if x % 3 == 0 or x % 5 == 0])
```
Com apenas esse código é possível já pegar todos os múltiplos de 3 ou 5 abaixo de um valor especificado e soma-los.  

A parte `x for x in range(below)` vai iternar por cada número como se fosse:
```python
for x in range(below):
    ...
```
Entretanto, como é em uma compressão de lista, o valor `x` já é adicionado na lista. Porém, dá para fazer condições passando um `if` ao lado, como está em `if x % 3 == 0 or x % 5 == 0`, que seria como:
```python
for x in range(below):
    if(x % 3 == 0 or x % 5 == 0):
        ...
```
Que por fim, irá apenas adicionar o valor na lista caso a condição esteja cumprida, que no caso seria: "Se o resto da divisão de x por 3 for igual a 0 ou o resto da divisão de x por 5 for 0, faça ...". Retornando assim apenas os multiplos de 3 ou 5.  

Por fim, após ser retornado na lista apenas os multiplos de 3 ou 5, ela estará como parâmetro da função [`sum()`](https://docs.python.org/3/library/functions.html#sum), que apenas retorna a soma entre os valores da lista - *dá para definir por onde começar a somar, mas ai veja mais detalhes da função* -, que no nosso caso, irá retornar a soma de todos os números multiplos de 3 ou 5.