from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'gilazooooos ya estudie para mañana'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)