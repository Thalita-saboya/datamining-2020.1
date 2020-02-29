var1 = 50
var2 = 100

conta = (var1 + var2) * var1

print(conta)

def faz_conta():
    return 0

y = faz_conta()
print (y)

def soma_dois_valores(valor1, valor2):
    return valor1 + valor2

x = soma_dois_valores(3,4)
print (x)
x = soma_dois_valores(2,8)
print(x)

def raiz_quadrada(valor):
    return valor ** (1 / 2)
x = raiz_quadrada(9)
print (x)

def raiz(valor, base):
    return valor ** (1/base)
x = raiz(9,3)
print(x)

def e_par(valor):
    return (valor % 2) == 0

print(e_par(4))

def div_seis(valor):
    return ((valor % 2) == 0) and ((valor % 3) == 0)


print(div_seis(7))



def dez_mult_tres():
    ''' Imprime os primeiros 10 numeros não negativos multiplos de tres'''
    cont = 0
    numero = 1
    while cont < 10:
        if numero % 3 == 0:
            cont = cont + 1
            print(numero)
            numero = numero + 1
        else:
            numero = numero + 1

dez_mult_tres()