from flask import Blueprint, render_template, request, flash, session, redirect, url_for
from database.cadastros import cadastros
from database.cadastro import user
from static.functions import encontra_user, deleta_user, retorna_user

bd_bp = Blueprint('bd', __name__)

@bd_bp.route('/')
def bd_home():
    return render_template('home-bd.html', cad= cadastros)

@bd_bp.route('/delete', methods=['DELETE'])
def delete():
    data = request.get_json()
    print(data)
    ind = encontra_user(data['codigo'])
    deleta_user(ind)
    return {'ok': 'ok'}

@bd_bp.route('/content')
def content():
    return render_template('itens-table.html', cad= cadastros)

@bd_bp.route('/detail')
def detail_user():
    return render_template('detail.html')

@bd_bp.route('/get_user/<cod>')
def details(cod):
    ind = encontra_user(str(cod))
    data = retorna_user(ind)
    return render_template('detail.html', dados=data)

@bd_bp.before_request
def authentication():
    if not 'email' in session:
        flash('Faça o login para acessar esta página')
        return redirect(url_for('homepage'))
    if session['email'] != user['email'] or session['senha'] != user['senha']:
        flash('Faça o login para acessar esta página')
        return redirect(url_for('homepage'))
    
