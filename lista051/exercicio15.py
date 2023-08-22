"""
15) Desenvolver um programa que apresente a série de Fibonacci até o décimo quinto termo. A série de Fibonacci é
formada pela sequência 1,1,2,3,5,8,13,21,34, ... etc. Ela se caracteriza pela soma de um termo posterior com seu
anterior subsequente
"""

"""
0+1=1
1+1=2
1+2=3
2+3=5
3+5=8
"""

v1 = 0
v2 = 1
rept = 1

print(v2)

while rept < 15:
    v3 = v1 + v2
    print(v3)
    v1 = v2
    v2 = v3
    rept = rept + 1