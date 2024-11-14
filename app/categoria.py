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

    def __init__(self, cat_nombre, cat_desc): # Método constructor de la clase
        self.cat_nombre = cat_nombre # Asignar el valor del parámetro nombre al atributo nombre
        self.cat_desc = cat_desc
    
with app.app_context():
    db.create_all()  # Crear la base de datos



class categoriaSchema(ma.Schema): # Crear la clase categoriaSchema que hereda de ma.Schema, lo que hace es definir la estructura de la respuesta que se enviará al cliente
    class Meta: # Definir la clase Meta
        fields = ('cat_id', 'cat_nombre', 'cat_desc') # Definir los campos que se mostrarán en la respuesta

#una sola respuesta
categoria_schema = categoriaSchema() # Crear una instancia de categoriaSchema

#varias respuestas
categorias_schema = categoriaSchema(many=True) # Crear una instancia de categoriaSchema, pero con la opción many=True para indicar que se enviarán varias respuestas

###########GET############

@app.route('/categoria', methods=['GET']) # Definir la ruta de la API, es decir la URL que se usará para acceder a la API

def get_categoria():
    all_categoria = categoria.query.all() # Obtener todas las categorias
    result = categorias_schema.dump(all_categoria) # Serializar la lista de categorias, el dump lo que hace es convertir la lista de objetos en una lista de diccionarios
    return jsonify(result) # Enviar la lista de categorias serializada como respuesta, la transformamos en un json 
 
@app.route('/', methods=['GET']) # Definir la ruta de la API, es decir la URL que se usará para acceder a la API

def index(): # Definir la función que se ejecutará al ingresar a la ruta, es decir la acción que realizará la API
    return jsonify({'message': 'Hello, World!'}) # Mensaje de bienvenida

if __name__ == '__main__': # Iniciar la aplicación
    app.run(debug=True) # Iniciar la aplicación en modo debug, es decir que se reiniciará automáticamente al realizar cambios en el código


