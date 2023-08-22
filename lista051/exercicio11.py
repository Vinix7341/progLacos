"""
11) Elaborar um programa que apresente o valor de uma potência de uma base qualquer (Variável b) elevada a um
expoente qualquer (Variável e), ou seja, de be. (Sem usar Math.pow();)
"""

b = int(input("Digite um valor para ser a base da potência:\n"))
e = int(input("Digite um valor para ser o expoente da potência:\n"))
contador = 1
ant = 1

while contador <= e:
    result = b * ant
    ant = result
    contador = contador + 1

print(f"A potência de {b} elevado à {e} é igual à {ant}")