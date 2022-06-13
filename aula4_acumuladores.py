repeticoes = 1 
soma = 0 
while repeticoes <= 5:
    n = int(input(f"{repeticoes} Digite o número: "))
    soma += n
    repeticoes += 1
print(f"Média: {soma/5:5.2f}")
