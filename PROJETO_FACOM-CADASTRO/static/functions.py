import random
from database.cadastros import cadastros

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


def formata_cpf(data):
    aux = data.split('.')
    final = aux[2].split('-')
    aux[2] = f'{final[0]}{final[1]}'
    for i in aux:
        if i.isdigit() == False:
            return ''
    final = ''.join(aux)
    return final

def encontra_user(cod):
    i = 0
    while i < len(cadastros):
        if cod == cadastros[i]['codigo']:
            break
        i += 1

    return i

def deleta_user(ind):
    del cadastros[ind]

def retorna_user(ind):
    return cadastros[ind]

#{'nome': 'Carlos Eduardo de Souza Sales', 'CPF': '03973457123', 'genero': 'masculino', 'raca': 'branco', 'etnia': 'Guaicurus', 'nascimento': '2006-11-06', 'escolaridade': 'EM', 'email': 'cadubss2@gmail.com'}

def verifica_user(user):
    try:
        aux = {
        'nome': user['nome'],
        'CPF': user['CPF'],
        'email': user['email'],
        'raca': user['raca'],
        'etnia': user['etnia'],
        'escolaridade': user['escolaridade'],
        'nascimento': user['nascimento'],
        'genero': user['genero'],
        'codigo': user['codigo']
        }
    except:
        return 0
    return aux

def user_code(users):
    finish = 0
    code = ''

    while not finish:
        code = ''
        finish = 1
        for i in range(5):
            code += str(random.randint(0,9))

        for i in users:
            if i['codigo'] == code:
                finish = 0
                break
    return code
