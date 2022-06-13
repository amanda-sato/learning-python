n1 = int(input("Digite um número inteiro - 1º número: "))
n2= int(input("Digite um número inteiro - 2º número: "))
x = n1
y = n2
contador = 0
sinal = 1

if x < 0 and y < 0:
    x, y = -x, -y 

elif y < 0:
    y = -y
    sinal = -1

elif x < 0:
    x = -x
    sinal = -1

while (x - y) >= 0: 
    contador += 1
    x -= y

print(f"{n1} / {n2} = {sinal * contador}. O  resto é {x}")
