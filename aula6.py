nota1 = float(input('Digite sua 1ª nota: '))
nota2 = float(input('Digite sua 2° nota: '))

media = (nota1 + nota2) / 2

if media >= 7 and media < 10:     
    print("Você foi Aprovado!")
elif media == 10:
    print("Você foi aprovado com Distinção!")
elif nota1 > 10 or nota2 > 10:
    print("Adicione uma nota válida!")
elif nota1 <= 0 or nota2 <= 0:
    print("Adicione uma nota válida!")
else:
    print("Infelizmente você foi reprovado")




