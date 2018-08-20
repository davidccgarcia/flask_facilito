from flask import Flask
from flask import request

app = Flask(__name__) 

@app.route('/') 
def index():
    return 'Hola Mundo'

@app.route('/saluda')
def saluda():
    return 'Saluda al cliente'

# params/libros/1
@app.route('/params')
@app.route('/params/<name>/<last_name>')
@app.route('/params/<name>/<last_name>/<int:edad>')
def params(name = '', last_name = '', edad = ''):
    return '{} {}, tu edad es {}' . format(name, last_name, edad)

if __name__ == '__main__':
    app.run(debug = True, port = 8000 ) 