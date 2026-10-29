from flask import Flask

app = Flask(__name__)


@app.route('/hello')
def hello_word():
    #logica da função
    return 'Olá, 1TDSPF! Bem-vindos ao framework Flask!'