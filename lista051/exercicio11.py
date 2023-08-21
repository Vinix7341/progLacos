"""
11) Elaborar um programa que apresente o valor de uma potência de uma base qualquer (Variável b) elevada a um
expoente qualquer (Variável e), ou seja, de be. (Sem usar Math.pow();)
"""

b = int(input("Digite um valor para ser a base da potência:\n"))
e = int(input("Digite um valor para ser o expoente da potência:\n"))

print(f"A potência de {b} elevado à {e} é igual à {b ** e}")