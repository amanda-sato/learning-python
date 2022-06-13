fim = int(input("Digite o último número a imprimir: "))
x = 1

while x <= fim:
    print(x)
    x += 2


fim = int(input("Digite o último número a imprimir: "))
x = 0

while x <= fim:
    if x % 2 != 0:
        print(x)
    x += 1