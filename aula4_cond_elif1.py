number1 = float(input("Digite o 1º número: "))
number2 = float(input("Digite o 2º número: "))
operacao = input("Qual operação você deseja realizar (soma, subtração, divisão, multiplicação ou exponenciação)?  ")

if operacao == "soma":
    print(number1 + number2)
elif operacao == "subtração":
    print(number1-number2)
elif operacao == "divisão":
    print(number1/number2)
elif operacao == "multiplicação":
    print(number1*number2)
elif operacao == "exponenciação":
    print(number1**number2)