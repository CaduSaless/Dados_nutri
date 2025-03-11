import random

def verifica_cpf(n):
    i = n
    n_aux = int(n/10)
    ultimo = i%10
    i = 1
    soma12 = ultimo
    soma11 = 0
    while i < 11:
        soma11 += (n_aux%10)*i
        i += 1
        soma12 += (n_aux%10)*i
        n_aux = int(n_aux/10)
    if soma12%11 == 0 and soma11%11 == 0:
        return True
    
    return False


def gerador_de_link():
    lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
    uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    symbols = "_-=;^~"
    variaveis = [lowercase_letters, uppercase_letters, symbols]
    i = 0
    senha = ''
    while i < 8:
        type = random.randint(0,2)
        digit = random.randint(0,len(variaveis[type])-1)

        senha += variaveis[type][digit]
        i += 1

    return senha