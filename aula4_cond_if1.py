number1 = float(input("1º número: "))
number2 = float(input("2º número: "))

if number1 > number2:
    print("O primeiro número é maior!")
elif number1 < number2:
    print("O segundo número é maior!")
else:
    print("Os números são iguais!")

velocidade = int(input("Qual a velocidade do seu carro? "))
multa = (velocidade - 80) * 5

if velocidade > 80:
    print("Você foi multado!")
    print(f"Sua multa é: {multa}")

salario = float(input("Qual o seu salário (para cálculo do IR)? "))
base = salario
imposto = 0

if base > 3000:
    imposto = imposto + ((base-3000) * 0.35)
    base = 3000

if base > 1000:
    imposto = imposto + ((base-1000) * 0.20)
    base = 1000

print(f"Seu salário é R$ {salario:6.2f} e seu IR a pagar é R$ {imposto:6.2f}")


