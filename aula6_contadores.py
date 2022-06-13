nota = -1

while nota < 0 or nota > 10:
    nota = float(input("Digite uma nota entre zero e dez: "))

    if nota < 0 or nota > 10:
        print("O valor digitado é inválido. Digite uma nota entre zero e dez!!!")

print(f"A nota digitada é {nota}")