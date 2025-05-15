from flask import Blueprint, render_template, request, redirect, flash
import time
import sqlite3

image_path = r'/home/vinicius/Imagens/webcam-python/b80.jpg'
cliente = {
    'CPF': 0,
    'nome': '',
    'altura': 0,
    'peso': 0,
    }

marcadores_route = Blueprint("Marcadores", __name__)



@marcadores_route.route("/marcadores/consumiu01")
def consumiu01():
    return render_template('consumiu01.html')

@marcadores_route.route("/marcadores/consumiu01", methods=['POST'])
def consumiu01_verify():
    data = request.form['consumiu']
    return redirect('/marcadores/consumiu02')

@marcadores_route.route("/marcadores/consumiu02")
def consumiu02():
    return render_template('consumiu02.html')

@marcadores_route.route("/marcadores/consumiu02", methods=['POST'])
def consumiu02_verify():
    try:
        data = request.form['consumiu']
        return redirect('/marcadores/marcadores01')
    except KeyError:
        flash("Erro: Campo 'consumiu' não foi enviado.")
        return redirect('/marcadores/consumiu02')

@marcadores_route.route("/marcadores/marcadores01")
def marcadores01():
    return render_template('marcadores_alimentar01.html')

@marcadores_route.route("/marcadores/marcadores01", methods=['POST'])
def marcadores01_verify():
    data = request.form['refeicao1']
    return redirect('/marcadores/marcadores02')

@marcadores_route.route("/marcadores/marcadores02")
def marcadores02():
    return render_template('marcadores_alimentar02.html')

@marcadores_route.route("/marcadores/marcadores02", methods=['POST'])
def marcadores02_verify():
    data = request.form['refeicao02']
    return redirect('/marcadores/marcadores03')

@marcadores_route.route("/marcadores/marcadores03")
def marcadores03():
    return render_template('marcadores_alimentar03.html')

@marcadores_route.route("/marcadores/marcadores03", methods=['POST'])
def marcadores03_verify():
    data = request.form['refeicao03']
    return redirect('/marcadores/marcadores04')

@marcadores_route.route("/marcadores/marcadores04")
def marcadores04():
    return render_template('marcadores_alimentar04.html')

@marcadores_route.route("/marcadores/marcadores04", methods=['POST'])
def marcadores04_verify():
    data = request.form['refeicao04']
    return redirect('/marcadores/marcadores05')

@marcadores_route.route("/marcadores/marcadores05")
def marcadores05():
    return render_template('marcadores_alimentar05.html')

@marcadores_route.route("/marcadores/marcadores05", methods=['POST'])
def marcadores05_verify():
    data = request.form['refeicao05']
    return redirect('/marcadores/marcadores06')

@marcadores_route.route("/marcadores/marcadores06")
def marcadores06():
    return render_template('marcadores_alimentar06.html')

@marcadores_route.route("/marcadores/marcadores06", methods=['POST'])
def marcadores06_verify():
    data = request.form['refeicao06']
    return redirect('/marcadores/marcadores07')

@marcadores_route.route("/marcadores/marcadores07")
def marcadores07():
    return render_template('marcadores_alimentar07.html')

@marcadores_route.route("/marcadores/marcadores07", methods=['POST'])
def marcadores07_verify():
    data = request.form['refeicao07']
    return redirect('/marcadores/marcadores08')

@marcadores_route.route("/marcadores/marcadores08")
def marcadores08():
    return render_template('marcadores_alimentar08.html')

@marcadores_route.route("/marcadores/marcadores08", methods=['POST'])
def marcadores08_verify():
    data = request.form['refeicao08']
    return redirect('/marcadores/marcadores09')

@marcadores_route.route("/marcadores/marcadores09")
def marcadores09():
    return render_template('marcadores_alimentar09.html')

@marcadores_route.route("/marcadores/marcadores09", methods=['POST'])
def marcadores09_verify():
    data = request.form['refeicao09']
    return redirect('/marcadores/marcadores10')

@marcadores_route.route("/marcadores/marcadores10")
def marcadores10():
    return render_template('marcadores_alimentar10.html')

@marcadores_route.route("/marcadores/marcadores10", methods=['POST'])
def marcadores10_verify():
    data = request.form['refeicao10']
    return redirect('/')

@marcadores_route.route('/fim')
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


##### TERMINAR DE EDITAR OS FORMS DE CONSUMIU E MARCADORES #####