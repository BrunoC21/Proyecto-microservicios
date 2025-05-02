from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
import requests

app = Flask(__name__)
db_url = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_DATABASE_URI'] = db_url
database = SQLAlchemy(app)

class Student(database.Model):
    __tablename__= 'student'
    rut = database.Column(database.String(12), primary_key=True)
    nombre_completo = database.Column(database.String(100))
    edad = database.Column(database.Integer)
    curso = database.Column(database.String(100))

class Evaluacion(database.Model):
    __tablename__= 'evaluacion'
    id = database.Column(database.Integer, primary_key=True)
    rut_estudiante = database.Column(database.String(12),database.ForeignKey('student.rut'), nullable=False)
    semestre = database.Column(database.String(20))
    asignatura = database.Column(database.String(100))
    nota = database.Column(database.Float)

@app.route('/evaluaciones', methods=['POST'])
def crear_evaluacion():
    data = request.get_json()
    rut_estudiante = data.get('rut_estudiante')
    solicitud = requests.get(f'http://estudiante:5000/estudiantes/{rut_estudiante}')
    if solicitud.status_code != 200:
        return jsonify({"mensaje": "No se puede crear evaluación: estudiante no encontrado."}), 400
    else:
        nueva_eva = Evaluacion(**data)
        database.session.add(nueva_eva)
        database.session.commit()
    return jsonify({"mensaje": "Evaluación creada"}), 201

@app.route('/evaluaciones', methods=['GET'])
def obtener_evaluaciones():
    evaluaciones = Evaluacion.query.all()
    result = []
    for e in evaluaciones:
        result.append({
            'id': e.id,
            'rut_estudiante': e.rut_estudiante,
            'semestre': e.semestre,
            'asignatura': e.asignatura,
            'nota': e.nota
        })
    return jsonify(result)

@app.route('/evaluaciones/<rut_estudiante>', methods=['GET'])
def obtener_evaluacion(rut_estudiante):
    evaluaciones = Evaluacion.query.filter_by(rut_estudiante=rut_estudiante).all()
    if evaluaciones:
        result = []
        for e in evaluaciones:
            result.append({
                'id': e.id,
                'rut_estudiante': e.rut_estudiante,
                'semestre': e.semestre,
                'asignatura': e.asignatura,
                'nota': e.nota
            })
        return jsonify(result)
    else:
        return jsonify({"mensaje": "Evaluación no encontrada"}), 404


with app.app_context():
    database.create_all()  
app.run(host='0.0.0.0', port=5001)
