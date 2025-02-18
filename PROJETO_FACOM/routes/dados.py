from flask import Blueprint, render_template, request, redirect, flash
import sqlite3
import cv2
import time
import requests
from services.functions import verifica_cpf, gerador_de_link

image_path = r'C:/Users/Carlos Sales/Pictures/webcam-python/picture'
cliente = {
    'CPF': 0,
    'nome': '',
    'altura': 0,
    'peso': 0,
    }


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
            cliente['CPF'] = int(data)
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
        cliente['nome'] = data
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
        cliente['altura'] = int(data)
        return redirect('/dados/peso')
    flash('Ocorreu um problema, podemos repetir?')
    return redirect('/dados/altura')

@dados_route.route('/dados/peso')
def peso():
    return render_template('peso.html')

@dados_route.route('/dados/medir_peso')
def peso_medir():
    image_path = r'C:/Users/Carlos Sales/Pictures/webcam-python/'
    cap = cv2.VideoCapture(0)
    if cap.isOpened():
        time.sleep(2)
        _, frame = cap.read()
        image_path += f'picture{gerador_de_link()}.png'
        cv2.imwrite(image_path, frame)
        cap.release()
        cv2.destroyAllWindows()
        image_path = r'C:/Users/Carlos Sales/Pictures/webcam-python/b80.jpg'
    else:
        flash('Ocorreu um problema, podemos repetir?')
        return redirect('/dados/peso')
    
    data = requests.get(f"http://127.0.0.1:5000/api/processa_arquivo?file_url={image_path}")
    digitos = data.json()
    if data.status_code == 200:
        valor = f'{digitos['digito1']}{digitos['digito2']}.{digitos['digito3']}{digitos['digito4']}'
        valor = float(valor)
        cliente['peso'] = valor
        return redirect('/fim')
    else:
        flash('Ocorreu um problema, podemos repetir?')
        return redirect('/dados/peso')

@dados_route.route('/fim')
def fim():
    print(cliente)
    if cliente['altura'] and cliente['peso'] and cliente['CPF'] and cliente['nome']:
        db = sqlite3.connect('C:/Users/Carlos Sales/Documents/CODE/PROJETO_FACOM/database/clientes.db')
        cursor = db.cursor()
        cursor.execute(f'INSERT INTO tabela_clientes (CPF, nome, altura, peso) VALUES ({cliente["CPF"]},"{cliente["nome"]}",{cliente["altura"]},{cliente["peso"]})')
        db.commit()
        db.close()
        cliente['CPF'] = 0
        cliente['altura'] = 0
        cliente['nome'] = ''
        cliente['peso'] = 0
        return render_template('final.html')
    return f'Faltam argumentos para inserir no banco de dados'
