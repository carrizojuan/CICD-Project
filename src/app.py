from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Sos mi amor te amo tanto vamos a tomar mate a la COSTA'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)