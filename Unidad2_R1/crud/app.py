#CRUD unidad 2 R1 Axel  Alejandro Almager Rodrigez

import json
import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

# Establece la conexión con la base de datos
def get_db_connection():
    conn = sqlite3.connect('crud.db')
    conn.row_factory = sqlite3.Row
    return conn

# Método GET para obtener todos los registros de la tabla albumes
@app.route('/albumes', methods=['GET'])
def get_albumes():
    registros = []
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM albumes')
    data = cursor.fetchall()
    for reg in data:
        registros.append(dict(reg))
    conn.close()
    return jsonify(registros)

# Método GET para obtener todos los registros de la tabla canciones
@app.route('/canciones', methods=['GET'])
def get_canciones():
    registros = []
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM canciones')
    data = cursor.fetchall()
    for reg in data:
        registros.append(dict(reg))
    conn.close()
    return jsonify(registros)

# Método PUT para crear un registro en la tabla albumes
@app.route('/albumes', methods=['PUT'])
def create_album():
    record = json.loads(request.data)

    conn = get_db_connection()
    cursor = conn.cursor()
    insert = 'INSERT INTO albumes (id_album, titulo, fecha_publicacion, sello_discografico, genero, numero_canciones, duracion_total, artista, año_lanzamiento, pais_origen) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
    cursor.execute(insert, (record['id_album'], record['titulo'], record['fecha_publicacion'], record['sello_discografico'], record['genero'], record['numero_canciones'], record['duracion_total'], record['artista'], record['año_lanzamiento'], record['pais_origen']))
    conn.commit()
    return jsonify(record)

# Método PUT para crear un registro en la tabla canciones
@app.route('/canciones', methods=['PUT'])
def create_cancion():
    record = json.loads(request.data)

    conn = get_db_connection()
    cursor = conn.cursor()
    insert = 'INSERT INTO canciones (id_cancion, titulo, duracion, genero, numero_pista, compositor, año_lanzamiento, idioma, id_album) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)'
    cursor.execute(insert, (record['id_cancion'], record['titulo'], record['duracion'], record['genero'], record['numero_pista'], record['compositor'], record['año_lanzamiento'], record['idioma'], record['id_album']))
    conn.commit()
    return jsonify(record)

# Método DELETE para eliminar un registro de la tabla albumes
@app.route('/albumes', methods=['DELETE'])
def delete_album():
    record = json.loads(request.data)
    conn = get_db_connection()
    cursor = conn.cursor()
    delete = 'DELETE FROM albumes WHERE id_album = ?'
    cursor.execute(delete, (record['id_album'],))
    conn.commit()
    return jsonify(record)

# Método DELETE para eliminar un registro de la tabla canciones
@app.route('/canciones', methods=['DELETE'])
def delete_cancion():
    record = json.loads(request.data)
    conn = get_db_connection()
    cursor = conn.cursor()
    delete = 'DELETE FROM canciones WHERE id_cancion = ?'
    cursor.execute(delete, (record['id_cancion'],))
    conn.commit()
    return jsonify(record)

# Método POST para actualizar un registro en la tabla albumes
@app.route('/albumes', methods=['POST'])
def update_album():
    record = json.loads(request.data)
    
    conn = get_db_connection()
    cursor = conn.cursor()
    update = 'UPDATE albumes SET titulo = ?, fecha_publicacion = ?, sello_discografico = ?, genero = ?, numero_canciones = ?, duracion_total = ?, artista = ?, año_lanzamiento = ?, pais_origen = ? WHERE id_album = ?'
    cursor.execute(update, (record['titulo'], record['fecha_publicacion'], record['sello_discografico'], record['genero'], record['numero_canciones'], record['duracion_total'], record['artista'], record['año_lanzamiento'], record['pais_origen'], record['id_album']))
    conn.commit()
    return jsonify(record)

# Método POST para actualizar un registro en la tabla canciones
@app.route('/canciones', methods=['POST'])
def update_cancion():
    record = json.loads(request.data)
    
    conn = get_db_connection()
    cursor = conn.cursor()
    update = 'UPDATE canciones SET titulo = ?, duracion = ?, genero = ?, numero_pista = ?, compositor = ?, año_lanzamiento = ?, idioma = ?, id_album = ? WHERE id_cancion = ?'
    cursor.execute(update, (record['titulo'], record['duracion'], record['genero'], record['numero_pista'], record['compositor'], record['año_lanzamiento'], record['idioma'], record['id_album'], record['id_cancion']))
    conn.commit()
    return jsonify(record)

# Inicia el servicio
if __name__ == '__main__':
    app.run(debug=True)
