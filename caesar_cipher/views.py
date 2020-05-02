from flask import request, jsonify, Blueprint
import json
import requests
from os import getenv
import string
import hashlib

caesar_cipher = Blueprint('caesarcipher', __name__)

TOKEN = getenv('TOKEN')

@caesar_cipher.route('/')
def get_encrypted():
    response = requests.get('https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token={}'.format(TOKEN))
    data = response.json()
    answer = get_answer()
    answer['numero_casas'] = data['numero_casas']
    answer['token'] = TOKEN
    answer['cifrado'] = data['cifrado']
    answer['decifrado'] = decipherer(answer)
    answer['resumo_criptografico'] = hashlib.sha1((answer['decifrado']).encode('utf-8')).hexdigest()
    update_answer(answer)
    return submit_answer()

    
def get_answer():
    file = open('caesar_cipher/answer.json', 'r')
    answer = json.load(file)
    file.close()
    return answer


def update_answer(answer):
    file = open('caesar_cipher/answer.json', 'w')
    json.dump(answer, file)
    file.close()


def decipherer(answer):
    letters = string.ascii_lowercase
    decifrado = ''
    for letter in answer['cifrado']:
        decifrado += letter if not letter in letters else letters[ (letters.index(letter) - answer['numero_casas']) % 26 ]
    return decifrado


def submit_answer():
    with open('caesar_cipher/answer.json', 'rb') as answer:
        response = requests.post(
            'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token={}'.format(TOKEN),
            files={'answer': answer},
        )
    data = response.json()
    return(data)

