number1 = float(input("Digite o 1º número:"))
number2 = float(input("Digite o 2º número:"))

if number1 > number2:
    print("O primeiro número é maior!")
else:
    if number1 < number2:
        print("O segundo número é maior!")
    else:
        print("Os números são iguais!")