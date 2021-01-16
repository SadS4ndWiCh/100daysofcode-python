# Project Euler - Problem 1

def sumMultiplesOf3And5(below: int) -> int:
    """ Encontra a soma dos multiplos de 3 ou 5 abaixo de um valor especificado. """

    return sum([x for x in range(below) if x % 3 == 0 or x % 5 == 0])

answer = sumMultiplesOf3And5(1000)
print(answer)
