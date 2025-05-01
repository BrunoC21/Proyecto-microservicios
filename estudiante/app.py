from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
db_link = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_DATABASE_URI'] = db_link
database = SQLAlchemy(app)

class Student(database.Model):
    __tablename__= 'student'
    rut = database.Column(database.String(12), primary_key=True)
    nombre_completo = database.Column(database.String(100))
    edad = database.Column(database.Integer)
    curso = database.Column(database.String(100))

@app.route('/estudiantes', methods=['POST'])
def crear_estudiante():
    data = request.get_json()
    nuevo_student = Student(**data)
    database.session.add(nuevo_student)
    database.session.commit()
    return jsonify({"mensaje": "Estudiante creado"}), 200

@app.route('/estudiantes', methods=['GET'])
def obtener_estudiantes():
    estudiantes = Student.query.all()
    result = []
    for e in estudiantes:
        result.append({
            'rut': e.rut,
            'nombre_completo': e.nombre_completo,
            'edad': e.edad,
            'curso': e.curso
        })
    return jsonify(result)

@app.route('/estudiantes/<rut>', methods=['GET'])
def obtener_estudiante_por_rut(rut):
    estudiante = Student.query.get(rut)
    if estudiante:
        return jsonify({
            'rut': estudiante.rut,
            'nombre_completo': estudiante.nombre_completo,
            'edad': estudiante.edad,
            'curso': estudiante.curso
        })
    else:
        return jsonify({"mensaje": "Estudiante no encontrado"}), 404

with app.app_context():
    database.create_all()
app.run(host='0.0.0.0', port=5000)

