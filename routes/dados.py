from flask import Blueprint, render_template, request, redirect, flash

def verifica_cpf(n):
    i = n
    n_aux = int(n/10)
    ultimo = i%10
    penultimo = n_aux%10
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
    



dados_route = Blueprint("Dados", __name__)

@dados_route.route('/dados/cpf')
def cpf():
    return render_template('cpf.html')

@dados_route.route('/dados/cpf', methods=['POST'])
def cpf_verif():
    data = request.form.get('cpf')
    print(type(data))
    if (data.isdigit() == True):
        if verifica_cpf(int(data)):
            return redirect('/dados/nome')
        else:
            flash('Digite um CPF válido')
    else:
        flash("Digite apenas números")
    return redirect('/dados/cpf')

@dados_route.route('/dados/nome')
def nome():
    return render_template('nome.html')

@dados_route.route('/dados/nome', methods=['POST'])
def nome_verif():
    data = request.form.get('nome')
    print(data)
    bool = True
    for i in data:
        if (i.isalpha() or i.isspace()) == False:
            bool = False
    if bool:
        return redirect('/dados/altura')
    flash("Digite apenas letras")
    return redirect('/dados/nome')

@dados_route.route('/dados/altura')
def altura():
    return render_template('altura.html')

@dados_route.route('/dados/medir_altura')
def medir_altura():
    return render_template('medir_altura.html')

@dados_route.route('/dados/altura_verif', methods=['POST'])
def altura_verif():
    data = request.form.get('altura')
    print(data)
    '''Verificar se tem letras'''
    if data.isnumeric():
        return redirect('/dados/peso')
    flash('Ocorreu um problema, podemos repetir?')
    return redirect('/dados/altura')

@dados_route.route('/dados/peso')
def peso():
    return render_template('peso.html')

@dados_route.route('/dados/medir_peso')
def peso_medir():
    return render_template('medir_peso.html')

@dados_route.route('/dados/peso_verif', methods=['POST'])
def peso_verif():
    data = request.form.get('peso')
    print(data)
    if data.isnumeric():
        return render_template('final.html')
    flash('Ocorreu um problema, podemos repetir?')
    return redirect('/dados/peso')