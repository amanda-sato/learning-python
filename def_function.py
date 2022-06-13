def soma(a, b):
    print(a+b)
soma(2,9)
soma(7,8)
soma(10,15)

def soma(a, b):
    return a + b #Se alguém atribuir a chamada de função à alguma variável ou usar alguma expressão, 
                 #o valor disso será o valor retornado pela função.
print(soma(2,9))

def épar(x):
    return x % 2 == 0
print(épar(2))
print(épar(3))
print(épar(10)) #retorna boolean por ser o resultado de uma comparação

def épar(x):
    return x % 2 == 0
def par_ou_ímpar(x):
    if épar(x):
        return "par"
    else:
        return "ímpar"
print(par_ou_ímpar(4))
print(par_ou_ímpar(5))



def maior(a , b):
    if a > b:
        return a

    else:
        return b
print(maior(5,6))
print(maior(2,1))
print(maior(7,7))


def multiple(a, b):
    return a % b == 0
    
print(multiple(8,4))
print(multiple(7,3))
print(multiple(5,5))


