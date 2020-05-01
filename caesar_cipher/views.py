from flask import request, jsonify, Blueprint
import json
import requests
from os import getenv

caesar_cipher = Blueprint('caesarcipher', __name__)

TOKEN = getenv('TOKEN')

@caesar_cipher.route('/')
@caesar_cipher.route('/listar', methods=['GET'])
def listar_planetas():
    get_encrypted()
    return ("oiiiiiiiiiii")


def get_encrypted():
    response = requests.get('https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token={}'.format(TOKEN))
    data = response.json()
    update_answer()


def get_answer():
    file = open('caesar_cipher/answer.json', 'r')
    answer = json.load(file)
    file.close()
    return answer


def update_answer(answer):
    file = open('caesar_cipher/answer.json', 'w')
    json.dump(answer, file)
    file.close()
