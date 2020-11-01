from flask import Flask, render_template, request
import redis

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_word', methods=['POST'])
#Esta funcion guarda los valores ingresados por teclado en nuestra pagina web.
#Al ser una ruta con el metodo POST, cumple con la sentencia If para guardar los valores y luego ser imprimidos por consola utilizando Redis.
def add_word():

    r = redis.Redis(host='localhost')
    if request.method == 'POST':
        id_ =  request.form['id_'] 
        palabra = request.form['palabra']
        significado = request.form['significado']
        
        r.hset('w', 'id', id_)
        r.hset('w', 'palabra', palabra)
        r.hset('w', 'significado', significado)

        print(r.hgetall('w'))

        return 'received'

if __name__ == '__main__':
    app.run(debug = True)
