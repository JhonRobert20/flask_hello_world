from flask import render_template
from flask.globals import request, session
from werkzeug.utils import redirect
from flask.helpers import url_for

def funcion_mostrar_edad(edad):
  mayoria_edad = True if edad >= 18 else False
  
  return {
    "edad" : edad,
    "mayoria edad" : mayoria_edad
  }

def funcion_mostrar_json(nombre):
  if nombre == '1':
    return {
      'nombre' : "a",
      'metodo http' : request.method
    }
  else:
    enviar = {
      'nombre' : nombre
    }
    return enviar

def funcion_saludar(nombre):
  return {
    "saludos" : "hola", 
    "parametros" : nombre
  }

def funcion_logout():
  session.pop('username')
  return redirect(url_for('hello_world'))

def funcion_login():
  if request.method == 'POST':
      session['username'] = request.form['username']
      return redirect(url_for('hello_world'))

  else:
    return render_template('login.html')

def funcion_hello_world():
  dic = {
    'usuario' : "none",
    'mensaje' : "El usuario no ha hecho Login",
  }
  if 'username' in session:
    dic = {
      'usuario' : session['username'],
      'mensaje' : "El usuario " + session['username'] + " se ha Logeado"
    }

  return redirect(url_for('inicio', mensaje = dic['mensaje'], usuario = dic['usuario'] ))