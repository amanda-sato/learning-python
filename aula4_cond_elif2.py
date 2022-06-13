valor_casa = float(input("Qual o valor do imóvel que pretende comprar? "))
salario = float(input("Qual o seu salário mensal? "))
anos_pagamento = int(input("Qual a quantidade de anos que deseja efetuar o pagamento total?"))
meses = anos_pagamento*12
prestacao = valor_casa/meses

if prestacao > (salario*0.30):
    print("O valor da prestação não pode ser maior que 30% do salário mensal! Refaça a simulação!")

else:
    print(f"O valor da sua prestação mensal é R$ {prestacao:8.2f}")
