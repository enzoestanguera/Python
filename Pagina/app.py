from flask import Flask, jsonify, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/hello')
def hello_word():
    #logica da função
    return '<h1>Olá, 1TDSPF! Bem-vindos ao framework Flask!</h1>'

@app.route('/hello/<nome>')
def hello_name(nome):
    #logica 
    return f'Olá, {nome}'

@app.route('/soma/<int:n1>/<int:n2>')
def somar(n1, n2):
    #logica
    return f'A soma de {n1} com {n2} é {n1+n2}'

@app.route('/todo')
def todo_list():
    lista_tarefas = {
        'Tarefa 1': 'Estudar Python',
        'Tarefa 2' : 'Estudar Java',
        'Tarefa 3': 'Fazer alguma coisa...',
        'Tarefa 4': 'Apresentar o Cp amanhã'
    }
    return jsonify(lista_tarefas) #casting para JSON

@app.route('/')
def home():
    return redirect(url_for('pagina_inicial'))

@app.route('/home')
def pagina_inicial():
    return f'<h1> Bem-vindo a pagina inicial</h1>'

@app.route('/pagina1')
def pagina1():
    return render_template('pagina1.html')
    

if __name__ == '__main__':
    app.run(debug=True)