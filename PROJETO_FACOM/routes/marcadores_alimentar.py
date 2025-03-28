from flask import Blueprint, render_template, request, redirect, flash
import time

image_path = r'/home/vinicius/Imagens/webcam-python/b80.jpg'
cliente = {
    'CPF': 0,
    'nome': '',
    'altura': 0,
    'peso': 0,
    }

marcadores_route = Blueprint("marcadores", __name__)

@marcadores_route.route("/marcadores/01")
def marcadores01():
    return render_template('marcadores_alimentar01.html')

@marcadores_route.route("/marcadores/02")
def marcadores02():
    return render_template('marcadores_alimentar02.html')

@marcadores_route.route("/marcadores/03")
def marcadores03():
    return render_template('marcadores_alimentar03.html')

@marcadores_route.route("/marcadores/04")
def marcadores04():
    return render_template('marcadores_alimentar04.html')

@marcadores_route.route("/marcadores/05")
def marcadores05():
    return render_template('marcadores_alimentar05.html')

@marcadores_route.route("/marcadores/06")
def marcadores06():
    return render_template('marcadores_alimentar06.html')

@marcadores_route.route("/marcadores/07")
def marcadores07():
    return render_template('marcadores_alimentar07.html')

@marcadores_route.route("/marcadores/08")
def marcadores08():
    return render_template('marcadores_alimentar08.html')

@marcadores_route.route("/marcadores/09")
def marcadores09():
    return render_template('marcadores_alimentar09.html')

@marcadores_route.route("/marcadores/10")
def marcadores10():
    return render_template('marcadores_alimentar10.html')

@marcadores_route.route("/marcadores/consumiu01")
def consumiu_ontem01():
    return render_template('consumiu01.html')

@marcadores_route.route("/marcadores/consumiu02")
def consumiu_ontem02():
    return render_template('consumiu02.html')
