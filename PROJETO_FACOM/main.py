from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Vinicius123'

from database.db import db
db.init_app(app)

from routes.home import home_route
from routes.dados import dados_route
from routes.marcadores_alimentar import marcadores_route

app.register_blueprint(home_route)
app.register_blueprint(dados_route)
app.register_blueprint(marcadores_route)

app.run(debug=True, port = 5000)