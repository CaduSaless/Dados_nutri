from flask import Blueprint, render_template

AlturaRoute = Blueprint("Altura", __name__)


@AlturaRoute.route("/altura")
def altura():
  return render_template('altura.html')
