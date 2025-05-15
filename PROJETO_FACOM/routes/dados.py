from flask import Blueprint, render_template, request, redirect, flash
import sqlite3
import cv2
import time
import requests
from services.functions import verifica_cpf, gerador_de_link

image_path = r'C:/Users/Carlos Sales/Pictures/webcam-python/picture'
cliente = {
    'CPF': 0,
    'nome': '',
    'altura': 0,
    'peso': 0,
    }

dados_route = Blueprint("Dados", __name__)


#==================================#
  ###data = request.form.get('cpf')
    ###valor_cpf = data.split('.')
    ###final_cpf = valor_cpf[2].split('-')
    ###valor_cpf[2] = ''.join(final_cpf)
    ###cpf_inteiro = ''.join(valor_cpf)
    ###if (cpf_inteiro.isdigit() == True):
        ###if verifica_cpf(int(cpf_inteiro)):
            ##cliente['CPF'] = cpf_inteiro
            ###return redirect('/dados/altura')
        ##else:
            ##flash('Digite um CPF válido')
    ##else:
        ##flash("Digite apenas números")
    ##return redirect('/dados/cpf')

@dados_route.route('/dados/cpf')
def cpf():
    return render_template('cpf.html')

@dados_route.route('/dados/cpf', methods=['POST'])
def cpf_verif():
    data = request.form.get('cpf')  # Obtém o CPF enviado pelo formulário
    if not data:
        flash("O campo CPF está vazio. Por favor, insira um CPF.")
        return redirect('/dados/cpf')

    # Remove caracteres especiais (pontos e traços) do CPF
    cpf = ''.join(filter(str.isdigit, data))

    # Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11:
        flash("CPF inválido. Por favor, insira um CPF válido.")
        return redirect('/dados/cpf')

    # Validação do CPF
    if not valida_cpf(cpf):
        flash("CPF inválido. Por favor, insira um CPF válido.")
        return redirect('/dados/cpf')

    # CPF válido, salva no cliente e redireciona
    cliente['CPF'] = cpf
    return redirect('/dados/altura')


def valida_cpf(cpf):
    """
    Função para validar o CPF.
    Retorna True se o CPF for válido, caso contrário, False.
    """
    # Verifica se todos os dígitos são iguais (ex.: 111.111.111-11)
    if cpf == cpf[0] * len(cpf):
        return False

    # Cálculo do primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = (soma * 10 % 11) % 10

    # Cálculo do segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = (soma * 10 % 11) % 10

    # Verifica se os dígitos calculados correspondem aos dígitos fornecidos
    return cpf[-2:] == f"{digito1}{digito2}"

  

@dados_route.route('/dados/altura')
def altura():
    return render_template('altura.html')

@dados_route.route('/dados/medir_altura')
def medir_altura():
    return render_template('medir_altura.html')

@dados_route.route('/dados/altura_verif', methods=['POST'])
def altura_verif():
    data = request.form.get('altura')
    print(data)
    '''Verificar se tem letras'''
    if data.isnumeric():
        cliente['altura'] = int(data)
        return redirect('/dados/peso')
    flash('Ocorreu um problema, podemos repetir?')
    return redirect('/dados/altura')

@dados_route.route('/dados/peso')
def peso():
    return render_template('peso.html')

@dados_route.route('/dados/medir_peso')
def peso_medir():
    image_path = r'/home/vinicius/AreaTrabalho/webcam-python'
    cap = cv2.VideoCapture(0)
    if cap.isOpened():
        time.sleep(3)
        _, frame = cap.read()
        image_path += f'picture{gerador_de_link()}.png'
        cv2.imwrite(image_path, frame)
        cap.release()
        cv2.destroyAllWindows()
        image_path = r'/home/vinicius/AreaTrabalho/webcam-python/b80.jpg'
    else:
        flash('Ocorreu um problema, podemos repetir?')
        return redirect('/dados/peso')
    
    data = requests.get(f"http://127.0.0.1:5000/api/processa_arquivo?file_url={image_path}")
    digitos = data.json()
    if data.status_code == 200:
        try:
            valor = f'{digitos["digito1"]}{digitos["digito2"]}.{digitos["digito3"]}{digitos["digito4"]}'
            valor = float(valor)
            cliente['peso'] = valor
            return redirect('/marcadores/consumiu01')
        except:
            flash('Ocorreu um problema, podemos repetir?')
            return redirect('/dados/peso')
    else:
        flash('Ocorreu um problema, podemos repetir?')
        return redirect('/dados/peso')

@dados_route.route('/dados/error')
def peso_erro():
   return render_template('erro_peso.html')


