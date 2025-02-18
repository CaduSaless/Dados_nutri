A API foi integrada no arquivo main.py, pois estava dando erro segmentada em outro arquivo. 

Apenas rode o main.py e entre em 'localhost:5000/'. 

A rota 'dados/medir_peso' inicia a webcam com a variável cap, tira uma foto e salva com caracteres aleatórios dentro do caminho da variável image_path. 
Como a foto ainda não vai ser da balança, o valor da image_path é trocado para uma imagem da balança preexistente. 
A partir disso consome a API e salva em uma variável temporária cliente

Há alguns tratamentos de erro, no caso da câmera, e do retorno da API. 
Além disso foi implementado com JavaScript uma interface simples de espera para o usuário quando começar o processo de captar a imagem
