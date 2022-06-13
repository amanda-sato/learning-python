n1 = int(input("Digite um número inteiro - 1º número: "))
n2= int(input("Digite um número inteiro - 2º número: "))
x = n2
y = n1
contador = 0
z = 0

if x < 0 and y > 0:
    x, y = y, x

elif y < 0 and x < 0:
    y = -y 
    x = -x

while contador < x:
    contador += 1
    z += y

print(f"{n1} x {n2} = {z}")