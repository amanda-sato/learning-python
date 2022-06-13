salario = float(input("Digite o valor do salário: "))

if salario > 1250:
    aumento = salario * 0.10
    
else: 
    aumento = salario * 0.15

print(f"Salário é {salario} e o aumento é {aumento}. Valor do novo salário: {salario + aumento}")


