from flask import Blueprint, render_template

PesoRoute = Blueprint("Peso", __name__)


@PesoRoute.route("/peso")
def peso():
  return render_template('peso.html')
