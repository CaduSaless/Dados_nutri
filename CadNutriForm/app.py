from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SecretKey123'


from routes.form import formRoute
from routes.peso import PesoRoute

app.register_blueprint(formRoute)
app.register_blueprint(PesoRoute)


if '__main__' == __name__:
  app.run(debug=True, port=3000)