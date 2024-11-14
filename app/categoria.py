from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


app = Flask(__name__) # Crear una instancia de Flask
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/bdpythonapi' # Configurar la base de datos
db = SQLAlchemy(app) # Crear una instancia de SQLAlchemy
ma = Marshmallow(app) # Crear una instancia de Marshmallow


class categoria(db.Model): # Crear la clase categoria que hereda de db.Model
    cat_id = db.Column(db.Integer, primary_key=True) # Atributo id de tipo Integer y clave primaria
    cat_nombre = db.Column(db.String(70), unique=True) # Atributo nombre de tipo String y único
    cat_desc = db.Column(db.String(200)) # Atributo descripción de tipo String

    def __init__(self, cat_nom, cat_desc): # Método constructor de la clase
        self.cat_nom = cat_nom # Asignar el valor del parámetro nombre al atributo nombre
        self.cat_desc = cat_desc
    
with app.app_context():
    db.create_all()  # Crear la base de datos
 
@app.route('/categoria', methods=['GET']) # Definir la ruta de la API, es decir la URL que se usará para acceder a la API

def index(): # Definir la función que se ejecutará al ingresar a la ruta, es decir la acción que realizará la API
    return jsonify({'message': 'Hello, World!'}) # Mensaje de bienvenida

if __name__ == '__main__': # Iniciar la aplicación
    app.run(debug=True) # Iniciar la aplicación en modo debug, es decir que se reiniciará automáticamente al realizar cambios en el código


