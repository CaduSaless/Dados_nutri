from flask import Flask, jsonify, request
from routes.home import home_route
from routes.dados import dados_route
from services import testes as t

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Cadu'

app.register_blueprint(home_route)
app.register_blueprint(dados_route)

@app.route("/api/processa_arquivo")
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

    return jsonify(response_data)

app.run(debug=True)