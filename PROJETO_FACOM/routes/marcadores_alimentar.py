from flask import Blueprint, render_template, request, redirect, flash
import time

image_path = r'C:/Users/Carlos Sales/Pictures/webcam-python/picture'
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

@marcadores_route.route("/marcadores/consumiu01")
def consumiu_ontem01():
    return render_template('consumiu01.html')

@marcadores_route.route("/marcadores/consumiu02")
def consumiu_ontem02():
    return render_template('consumiu02.html')
