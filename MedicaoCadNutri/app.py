from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Vinicius123'


from routes.altura import AlturaRoute
from routes.peso import PesoRoute

app.register_blueprint(AlturaRoute)
app.register_blueprint(PesoRoute)


if '__main__' == __name__:
  app.run(debug=True, port=3000)