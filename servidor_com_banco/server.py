from bottle import route, run, view

from models import Chamado


@route('/')
@view("index")
def index():
    chamados = Chamado.select()
    print(chamados)
    return {'nomes': [chamado.name for chamado in chamados]}

run(host='localhost', port=8080)