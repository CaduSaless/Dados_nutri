from flask import Blueprint, jsonify, request
from services import testes as t

api_route = Blueprint("Api", __name__)


@api_route.route("/api/processa_arquivo")
def classificar():
    param = request.args.get('file_url')
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