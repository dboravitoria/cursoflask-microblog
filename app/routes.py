from app import app
from flask import render_template

dados = {"Nome": "Débora", "Idade": "21", "Estado": "Solteira", "Profissão": "Vendedora", "Contato": "(11)92017-8082"}


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', dados=dados)

@app.route('/contato')
def contato():
    return render_template('contato.html', dados=dados)


if __name__ == '__main__':
    app.run(debug=True) 


