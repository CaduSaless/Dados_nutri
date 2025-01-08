from flask import Flask
from routes.home import home_route
from routes.dados import dados_route

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Cadu'

app.register_blueprint(home_route)
app.register_blueprint(dados_route)

if __name__ = '__main__':
  app.run(debug=True)
