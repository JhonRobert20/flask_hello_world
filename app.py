from flask import Flask, render_template
from flask.globals import request, session
from flask.helpers import url_for
from werkzeug.utils import redirect
from errores import funcion_salir
from funciones import *

app = Flask(__name__)
app.secret_key = "Llave_de_bloque"

@app.route('/')
def hello_world():
  return funcion_hello_world()

@app.route('/index/<mensaje>/<usuario>')
def inicio(mensaje, usuario):
  return render_template('index.html', mensaje = mensaje, usuario = usuario )

@app.route('/jhon')
def jhon():
  return render_template('index.html', mensaje = "aaaaaad", usuario = "aa")

@app.route('/saludar/<nombre>')
def saludar(nombre):
  return funcion_saludar(nombre)

@app.route('/edad/<int:edad>')
def mostrar_edad(edad):
  return funcion_mostrar_edad(edad)

@app.route('/mostrar/<nombre>', methods = ['GET', 'POST'])
def mostrar_nombre(nombre):
  return render_template('mostrar.html', nombre = nombre)

@app.route('/redireccionar')
def redireccionar():
  return redirect(url_for('mostrar_edad', edad = 25))

@app.route('/api/mostrar/<nombre>', methods = ["GET", "POST"])
def mostrar_json(nombre):
  return funcion_mostrar_json(nombre)

@app.route('/login', methods = ['GET', 'POST'])
def login():
  return funcion_login()

@app.route('/logout')
def logout():
  return funcion_logout()

@app.route('/salir')
def salir():
  return funcion_salir()

@app.errorhandler(404)
def pagina_no_encontrada(error):
  return render_template('error404.html', error=error), 404

@app.errorhandler(500)
def pagina_error_interno(error):
  return render_template('error404.html', error = error), 500