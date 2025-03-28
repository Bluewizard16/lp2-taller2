from flask import Flask, render_template, redirect
import sqlite3
from pprint import pprint

# cargamos todos los datos
conexion = sqlite3.connect('web2.sqlite3')
conexion.row_factory = sqlite3.Row # Modo diccionario
cursor = conexion.cursor()
cursor.execute("""
SELECT * FROM productos;
""")
productos = [ dict(p) for producto in cursor.fetchall() ]
pprint(productos)
cursor.close()
conexion.close()

# aplicación
app = Flask(__name__)

# rutas
@app.route('/')
def ruta_raiz():
  pass

@app.route('/producto/<int:pid>')
def ruta_producto(pid):
  pass
  
# programa principal
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
