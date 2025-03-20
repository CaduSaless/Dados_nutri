from flask import Blueprint, session, request, redirect, url_for, render_template, flash, jsonify
from database.cadastro import user
from database.cadastros import cadastros
from static.functions import formata_cpf, verifica_cpf, verifica_user, user_code

cadastro_bp = Blueprint('cadastro', __name__)

etnia_var = ['Kadiwéls', 'Guaraní', 'Guaicurus', 'Outro']

user_atual = {}

@cadastro_bp.route('/cadastro/')
def homepage_cad():
    return render_template('home-cad.html')

@cadastro_bp.route('/cadastro/nome')
def nome():
    return render_template('nome.html')

@cadastro_bp.route('/cadastro/nome', methods=['POST'])
def nome_v():
    nome = request.form.get('nome')
    v_nome = nome.split(' ')
    for i in v_nome:
        if not i.isalpha():
            flash('Digite apenas letras')
            return redirect(url_for('cadastro.nome'))
    user_atual.update({'nome': nome}) 
    print(user_atual)
    return redirect(url_for('cadastro.cpf'))


@cadastro_bp.route('/cadastro/cpf')
def cpf():
    return render_template('cpf.html')

@cadastro_bp.route('/cadastro/cpf', methods=['POST'])
def cpf_v():
    cpf = request.form.get('cpf')
    if len(cpf) == 14:
        cpf = formata_cpf(cpf)
        if cpf:
            if verifica_cpf(int(cpf)):
                user_atual.update({'CPF': cpf}) 
                print(user_atual)
                return redirect(url_for('cadastro.genero'))
            flash('Digite um CPF válido')    
            return redirect(url_for('cadastro.cpf'))
        flash('Digite apenas os números')
    else:
        flash('Digite ao menos 11 dígitos')
    return redirect(url_for('cadastro.cpf'))


@cadastro_bp.route('/cadastro/genero')
def genero():
    return render_template('sexo.html')

@cadastro_bp.route('/cadastro/genero', methods=['POST'])
def genero_v():
    try:
        data = request.form['gender']
        print(data)
    except:
        flash('Selecione uma das opções')
        return redirect(url_for('cadastro.genero'))
    user_atual.update({'genero': data}) 
    return redirect(url_for('cadastro.raca'))


@cadastro_bp.route('/cadastro/raca')
def raca():
    return render_template('raca.html')

@cadastro_bp.route('/cadastro/raca', methods=['POST'])
def raca_v():
    data = request.form['raca']
    print(data)
    user_atual.update({'raca': data}) 
    return redirect(url_for('cadastro.etnia'))


@cadastro_bp.route('/cadastro/etnia')
def etnia():
    return render_template('etnia.html')

@cadastro_bp.route('/cadastro/etnia', methods=['POST'])
def etnia_v():
    data = request.form['etnia']
    
    if(data.lower() == 'outro'):
        return redirect(url_for('cadastro.etnia_add'))
    user_atual.update({'etnia': data}) 
    
    return redirect(url_for('cadastro.nasc'))

@cadastro_bp.route('/cadastro/etnia/add')
def etnia_add():
    return render_template('etnia_add.html')

@cadastro_bp.route('/cadastro/etnia/add', methods=['POST'])
def etnia_add_v():
    data = request.form['etnia']
    print(data)
    user_atual.update({'etnia': data}) 
    etnia_var.append(data)
    return redirect(url_for('cadastro.nasc'))

@cadastro_bp.route('/get/etnia')
def etnia_get():
    dict = {
        'etnia': etnia_var
    }
    var = jsonify(dict)
    return var

@cadastro_bp.route('/cadastro/nascimento')
def nasc():
    return render_template('datetime.html')

@cadastro_bp.route('/cadastro/nascimento', methods=['POST'])
def nasc_v():
    data = request.form.get('data')
    print(data)
    user_atual.update({'nascimento': data}) 
    return redirect(url_for('cadastro.escolaridade'))


@cadastro_bp.route('/cadastro/escolaridade')
def escolaridade():
    return render_template('escolaridade.html')

@cadastro_bp.route('/cadastro/escolaridade', methods=['POST'])
def escolaridade_v():
    data = request.form['esc']
    print(data)
    user_atual.update({'escolaridade': data}) 
    return redirect(url_for('cadastro.email'))


@cadastro_bp.route('/cadastro/email')
def email():
    return render_template('email.html')

@cadastro_bp.route('/cadastro/email', methods=['POST'])
def email_v():
    data = request.form.get('email')
    print(data)
    user_atual.update({'email': data}) 
    return redirect(url_for('cadastro.fim'))

@cadastro_bp.route('/cadastro/fim')
def fim():
    user_atual.update({'codigo': user_code(cadastros)})
    print(user_atual)
    aux = verifica_user(user_atual)
    print(aux)
    user_atual.clear()
    print(user_atual)
    if not aux:
        flash('Ocorreu um erro ao realizar o seu cadastro, por favor refaça-o!')
        return redirect(url_for('cadastro.homepage_cad'))
    cadastros.append(aux)
    return render_template('fim.html', codigo=aux['codigo'])

@cadastro_bp.before_request
def authentication():
    if not 'email' in session:
        flash('Faça o login para acessar esta página')
        return redirect(url_for('homepage'))
    if session['email'] != user['email'] or session['senha'] != user['senha']:
        flash('Faça o login para acessar esta página')
        return redirect(url_for('homepage'))
    

