from caesar_cipher import api
from os import getenv
from dotenv import load_dotenv
load_dotenv()

if __name__ == '__main__':
    host = '0.0.0.0'
    debug = eval(getenv('DEBUG').title())
    port = int(getenv('APP_PORT'))
    api.run(host=host, port=port, debug=debug)