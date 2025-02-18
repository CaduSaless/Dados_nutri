import cv2
import numpy as np

def calcular_media_escala_cinza(imagem):
    # Converte a imagem para um array numpy
    imagem_array = np.array(imagem)

    # Calcula a média dos valores de cinza
    media_cinza = np.mean(imagem_array)

    return media_cinza

def processar_imagem(img):
    media = calcular_media_escala_cinza(img)

    _, bin = cv2.threshold(img, int(media * 0.8), 255, cv2.THRESH_BINARY_INV)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(1,5))
    opening = cv2.morphologyEx(bin,cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(opening,cv2.MORPH_CLOSE, kernel)
    return closing


dict_digitos = {
    (1, 1, 1, 0, 1, 1, 1): 0,
    (0, 0, 1, 0, 0, 1, 0): 1,
    (1, 0, 1, 1, 1, 0, 1): 2,
    (1, 0, 1, 1, 0, 1, 1): 3,
    (0, 1, 1, 1, 0, 1, 0): 4,
    (1, 1, 0, 1, 0, 1, 1): 5,
    (1, 1, 0, 1, 1, 1, 1): 6,
    (0, 1, 0, 1, 1, 1, 1): 6,
    (1, 0, 1, 0, 0, 1, 0): 7,
    (1, 1, 1, 0, 0, 1, 0): 7,
    (1, 1, 1, 1, 1, 1, 1): 8,
    (1, 1, 1, 1, 0, 1, 1): 9,
    (1, 1, 1, 1, 0, 1, 0): 9}

def descobre_digito(img_digito):
    h_img, w_img = img_digito.shape
    corte_w1 = int(w_img * 0.2)
    corte_w2 = int(w_img * 0.8)
    corte_h1 = int(h_img * 0.1)
    corte_h2 = int(h_img * 0.45)
    corte_h3 = int(h_img * 0.55)
    corte_h4 = int(h_img * 0.9)
    segmentos = [
        ((corte_w1, 0), (corte_w2, corte_h1)),
        ((0, corte_h1), (corte_w1, corte_h2)),
        ((corte_w2, corte_h1), (w_img, corte_h2)),
        ((corte_w1, corte_h2), (corte_w2, corte_h3)),
        ((0, corte_h3), (corte_w1, corte_h4)),
        ((corte_w2, corte_h3), (w_img, corte_h4)),
        ((corte_w1, corte_h4), (corte_w2, h_img)),
    ]
    classificacao = [0]*7
    for(i, ((xA, yA), (xB, yB))) in enumerate(segmentos):
        #cv2.rectangle(img_digito, (xA, yA),(xB,yB), (255,0,0), 5)
        barra = img_digito[yA: yB, xA: xB]

        total = cv2.countNonZero(barra)
        area = (xB - xA) * (yB - yA)
        if float(area) != 0 and total / float(area) > 0.15:
            classificacao[i] = 1
            #cv2.putText(img_digito, '1', (xA + int((xB-xA)/2), yA + int((yB-yA)/2)),cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    if tuple(classificacao) in dict_digitos.keys() :
        digit = dict_digitos[tuple(classificacao)]
        return digit
    else:
        return "?"

def encontra_fim_digito(img, x, y, w, h):
    for i in range(len(img)-1, len(img)//2,-1):
        for j in range(x, w+x, 1):
            if img[i][j] == 255:
                return i-y
    return h



def processar_imagem2(img):
    media = calcular_media_escala_cinza(img)

    _, bin = cv2.threshold(img, int(media*0.8), 255, cv2.THRESH_BINARY_INV)
    #_, bin = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY_INV)
    return bin

def pegar_retangulos(img, original):
    contornos= cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    copia_img = img
    #Dimensões da imagem:
    alt, larg = img.shape
    larg15 = larg * 0.1
    alt15 = alt * 0.15
    range_in = (alt/2) - alt15
    range_fim = (alt/2) + alt15
    lista = []
    digitos = []
    for c in contornos[0]:
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(copia_img,(x,y),(x+y,w+h),(255,0,0),5)
        if h > alt15 and w > larg15:

            linhainf = y + h
            if (linhainf > range_in) and (linhainf < range_fim):
                h = encontra_fim_digito(img, x, y, w, h)
            if y < range_in:
                lista.append([x,y,w,h])
                digitos.append(original[y: y + h, x: x + w])
    cv2.imshow('copia',copia_img)
    cv2.waitKey()
    return lista, digitos

def recorte(img):
    alt, larg = img.shape
    per_total = alt*2+larg*2
    contornos, hierarquia = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    valor_balanca = 0
    perimetro_maior=0
    for c in contornos:
        perimetro = cv2.arcLength(c, True)
        if perimetro > perimetro_maior and perimetro < per_total*0.9:
            perimetro_maior = perimetro
            (x, y, alt, lar) = cv2.boundingRect(c)
            cv2.rectangle(img, (x, y), (x + alt, y + lar), (0, 255, 0), 2)
            valor_balanca = img[y:y + lar, x:x + alt]

    return valor_balanca

def encontra_borda(imagem, x, y, passo, cor_ideal):

    encontrou_borda = False
    i = 0
    mx, my = int(x/2), int(y/2)
    while i < mx and not encontrou_borda:
        cor_pixel = imagem[my, mx + i*passo]
        if cor_pixel[0] < cor_ideal[0] and cor_pixel[1] < cor_ideal[1] and cor_pixel[2] > cor_ideal[2]:
            encontrou_borda = True
        i += 1
    px = mx + i * passo
    encontrou_borda = False
    i = 0
    while i < my and not encontrou_borda:
        cor_pixel = imagem[my + i * passo, mx]
        if cor_pixel[0] < cor_ideal[0] and cor_pixel[1] < cor_ideal[1] and cor_pixel[2] > cor_ideal[2]:
            encontrou_borda = True
        i += 1
    py = my + i * passo
    return px, py

def encontra_borda_especifico(imagem, x, y, passo, cor_ideal):
    erro = 20
    encontrou_borda = False
    i = 0
    mx, my = int(x/2), int(y/2)
    while i < mx and not encontrou_borda:
        cor_pixel = imagem[my, mx + i*passo]
        if (cor_pixel[0] < cor_ideal[0] + erro and cor_pixel[0] > cor_ideal[0] - erro
                and cor_pixel[1] < cor_ideal[1] + erro and cor_pixel[1] > cor_ideal[1] - erro
                and cor_pixel[2] < cor_ideal[2] + erro and cor_pixel[2] > cor_ideal[2] - erro):
            encontrou_borda = True
        i += 1
    px = mx + i * passo
    encontrou_borda = False
    i = 0
    while i < my and not encontrou_borda:
        cor_pixel = imagem[my + i * passo, mx]
        if (cor_pixel[0] < cor_ideal[0] + erro and cor_pixel[0] > cor_ideal[0] - erro
                and cor_pixel[1] < cor_ideal[1] + erro and cor_pixel[1] > cor_ideal[1] - erro
                and cor_pixel[2] < cor_ideal[2] + erro and cor_pixel[2] > cor_ideal[2] - erro):
            encontrou_borda = True
        i += 1
    py = my + i * passo
    return px, py

def contorna_borda(imagem):
    gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    gray = cv2.blur(gray, (3, 3))
    canny = cv2.Canny(gray, 150, 20)
    canny = cv2.dilate(canny, None, iterations=1)
    cnts, _ = cv2.findContours(canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    lx, ly = 0, 0
    ry, rx = canny.shape
    for c in cnts:
        area = cv2.contourArea(c)
        x, y, w, h = cv2.boundingRect(c)
        epsilon = 0.09 * cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, epsilon, True)
        if len(approx) == 4 and area > 9000:
            aspect_ratio = float(w) / h
            if aspect_ratio > 2.4:
                cv2.rectangle(imagem, (x, y), (x + w, y + h), (0, 255, 0), 3)
                lx, ly, rx, ry = x, y, x + w, y + h
    return lx, ly, rx, ry

def pegar_visor(imagem=None, cor=None, borda_com_cor = True, diretorio = None):
    if cor is None:
        cor = [120, 120, 120]
    if imagem is None:
        imagem = cv2.imread(diretorio)
    y, x, z = imagem.shape
    l_x, l_y, r_x, r_y = 0, 0, 0, 0
    if borda_com_cor:
        l_x, l_y = encontra_borda(imagem, x, y, passo=-1, cor_ideal=cor)
        r_x, r_y = encontra_borda(imagem, x, y, passo=1, cor_ideal=cor)
    else:
        l_x, l_y, r_x, r_y = contorna_borda(imagem)

    #Pega a imagem dos dígitos
    recorte = imagem[l_y:r_y, l_x:r_x]
    recorte = cv2.resize(recorte, (800, 350), interpolation=cv2.INTER_AREA)

    digitos = []
    d1_lx, d1_ly, d1_rx, d1_ry = 235, 25, 335, 305
    d2_lx, d2_ly, d2_rx, d2_ry = 360, 25, 460, 305
    d3_lx, d3_ly, d3_rx, d3_ry = 480, 25, 580, 305
    d4_lx, d4_ly, d4_rx, d4_ry = 600, 25, 700, 305
    digitos.append(recorte[d1_ly:d1_ry, d1_lx:d1_rx])
    digitos.append(recorte[d2_ly:d2_ry, d2_lx:d2_rx])
    digitos.append(recorte[d3_ly:d3_ry, d3_lx:d3_rx])
    digitos.append(recorte[d4_ly:d4_ry, d4_lx:d4_rx])

    #Descobre os dígitos
    valores = []
    for d in digitos:
        d = cv2.cvtColor(d, cv2.COLOR_BGR2GRAY)
        d = processar_imagem(d)
        valores.append(descobre_digito(d))

    #Desenha o centro da imagem
    cv2.rectangle(imagem, (int(x / 2), int(y / 2) - 5), (int(x / 2) + 1, int(y / 2) + 5), (0, 255, 255), 2)
    cv2.rectangle(imagem, (int(x / 2) - 5, int(y / 2)), (int(x / 2) + 5, int(y / 2) + 1), (0, 255, 255), 2)

    #Desenha a região dos dígitos na imagem
    cv2.rectangle(imagem, (l_x, l_y), (r_x, r_y), (0, 255, 0), 2)
    altura, largura = r_y - l_y, r_x - l_x
    # Digito 1
    cv2.rectangle(imagem, (l_x + int(largura * d1_lx/800), l_y + int(altura * d1_ly/350)),
                  (l_x + int(largura * d1_rx/800), l_y + int(altura * d1_ry/350)), (255, 0, 0), 2)
    cv2.putText(imagem, str(valores[0]), (l_x + int(largura * d1_lx/800), l_y + int(altura * d1_ly/350)-10),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    # Digito 2
    cv2.rectangle(imagem, (l_x + int(largura * d2_lx / 800), l_y + int(altura * d2_ly / 350)),
                  (l_x + int(largura * d2_rx / 800), l_y + int(altura * d2_ry / 350)), (255, 0, 0), 2)
    cv2.putText(imagem, str(valores[1]), (l_x + int(largura * d2_lx / 800), l_y + int(altura * d2_ly / 350) - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    # Digito 3
    cv2.rectangle(imagem, (l_x + int(largura * d3_lx / 800), l_y + int(altura * d3_ly / 350)),
                  (l_x + int(largura * d3_rx / 800), l_y + int(altura * d3_ry / 350)), (255, 0, 0), 2)
    cv2.putText(imagem, str(valores[2]), (l_x + int(largura * d3_lx / 800), l_y + int(altura * d3_ly / 350) - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    # Digito 4
    cv2.rectangle(imagem, (l_x + int(largura * d4_lx / 800), l_y + int(altura * d4_ly / 350)),
                  (l_x + int(largura * d4_rx / 800), l_y + int(altura * d4_ry / 350)), (255, 0, 0), 2)
    cv2.putText(imagem, str(valores[3]), (l_x + int(largura * d4_lx / 800), l_y + int(altura * d4_ly / 350) - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    return valores

def pegar_digito_fixo(imagem):
    digitos = []
    digitos.append(imagem[40:310, 250:350])
    digitos.append(imagem[40:310, 370:470])
    digitos.append(imagem[40:310, 490:590])
    digitos.append(imagem[40:310, 605:705])
    return digitos
'''
img = cv2.imread("imagemteste.jpg")

img = cv2.resize(img, (600,300), interpolation=cv2.INTER_AREA)


bin = processar_imagem(img,60)
cv2.imshow('',bin)
cv2.waitKey()
lista, dig = pegar_retangulos(bin,img)

numeros = descobre_digito(img, lista)



cv2.waitKey(0)
cv2.destroyAllWindows()
'''