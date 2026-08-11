from datetime import datetime
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_moment import Moment

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/')
def index():
    # chama o arquivo index.html que está dentro da pasta templates/
    return render_template('index.html', current_time=datetime.utcnow())

@app.route('/user/<name>')
def user(name):
    # chama o arquivo user.html
    return render_template('user.html', name=name)

# rota para Identificação
@app.route('/identificacao')
def identificacao():
    return render_template(
        'user.html',
        name="Hiandra",
        prontuario="PT3038513",
        meutitulo="IFSP"
    )

# rota para Contexto da Requisição
@app.route('/contextorequisicao')
def contexto_requisicao():
    user_agent = request.headers.get('User-Agent')
    remote_ip = request.remote_addr
    host = request.host
    return render_template(
        'contexto.html',
        name="Hiandra",
        user_agent=user_agent,
        remote_ip=remote_ip,
        host=host
    )

@app.errorhandler(404)
def page_not_found(e):
    # chama o arquivo 404.html
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    # chama o arquivo 500.html
    return render_template('500.html'), 500