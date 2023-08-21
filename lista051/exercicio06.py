"""
6) Desenvolver um programa que leia um número n qualquer menor ou igual a 50 e apresente o valor obtido da
multiplicação sucessiva de n por 3 enquanto o produto for menor que 250. (n x 3; n x 3 x 3; n x 3 x 3 x 3 etc...).
"""

num = int(input("Digite um número menor ou igual que 50:\n"))

if num <= 50:
    while num < 250:
        num = num * 3
        if num < 250:
            print(num)
else:
    print("Seu número não é menor ou igual a 50")
