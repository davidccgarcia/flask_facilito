from flask import Flask

app = Flask(__name__) # nuevo objeto

@app.route('/') # wrap o decorador
def index():
    return 'Hola mundo' # Regresa un string
app.run() # Se encarga de ejecutar el servidor en el puerto 5000