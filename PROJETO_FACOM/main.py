from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Vinicius123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5001/facom_nutri'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from database.db import db
db.init_app(app)

from routes.home import home_route
from routes.dados import dados_route
from routes.marcadores_alimentar import marcadores_route
from services import testes as t

app.register_blueprint(home_route)
app.register_blueprint(dados_route)
app.register_blueprint(marcadores_route)

""" @app.route("/api/processa_arquivo")
def classificar():
    param = request.args.get('file_url')
    print('Esta é a pasta pega: ',param)
    if not param:
        return jsonify({'erro': 'Parâmetro obrigatório'}), 400
    #file = request.files['file']
    #file.save('/leituras/leitura.png')
    valores = t.pegar_visor(diretorio=param, borda_com_cor=True)

    response_data = {
        "digito1": valores[0],
        "digito2": valores[1],
        "digito3": valores[2],
        "digito4": valores[3]
    }

    return jsonify(response_data)"""
@app.route('/criar_tabelas')
def criar_tabelas():
    from database.db import db
    db.create_all()
    return 'Tabelas criadas com sucesso!'

app.run(debug=True, port = 5005)