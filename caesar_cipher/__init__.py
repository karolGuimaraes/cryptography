from flask import Flask, Blueprint
from caesar_cipher.views import caesar_cipher

api = Flask(__name__)

with api.app_context():
    api.register_blueprint(caesar_cipher)