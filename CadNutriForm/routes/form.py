from flask import Blueprint, render_template

formRoute = Blueprint("Form", __name__)


@formRoute.route("/form")
def formPage():
  return render_template('form.html')
