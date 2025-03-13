from flask import Blueprint, render_template, request
from database.cadastros import cadastros

bd_bp = Blueprint('bd', __name__)

@bd_bp.route('/')
def bd_home():
    return render_template('home-bd.html', cad= cadastros)

@bd_bp.route('/delete', methods=['POST'])
def delete():
    data = request.get_json()
    print(data)
    return {'ok': 'ok'}

@bd_bp.route('/content')
def content():
    return render_template('itens-table.html', cad= cadastros)