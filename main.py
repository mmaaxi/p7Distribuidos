from flask import Flask, jsonify, request

app = Flask(__name__)

# Paquetes simulados en memoria
paquetes = {
    "PKG001": {"destino": "CDMX", "estado": "En almacén"},
    "PKG002": {"destino": "Guadalajara", "estado": "En tránsito"},
    "PKG003": {"destino": "Monterrey", "estado": "Entregado"},
    "PKG004": {"destino": "Puebla", "estado": "En camino"},
    "PKG005": {"destino": "Tijuana", "estado": "En almacén"}
}

# Consultar estado de un paquete
@app.route('/paquete/<paquete_id>', methods=['GET'])
def obtener_paquete(paquete_id):
    if paquete_id not in paquetes:
        return jsonify({'error': 'Paquete no encontrado'}), 404
    return jsonify({
        'id': paquete_id,
        'destino': paquetes[paquete_id]['destino'],
        'estado': paquetes[paquete_id]['estado']
    })

# Listar todos los paquetes
@app.route('/paquetes', methods=['GET'])
def listar_paquetes():
    return jsonify(paquetes)

# Actualizar estado de un paquete
@app.route('/paquete/<paquete_id>', methods=['PUT'])
def actualizar_estado(paquete_id):
    if paquete_id not in paquetes:
        return jsonify({'error': 'Paquete no encontrado'}), 404

    data = request.get_json()
    nuevo_estado = data.get('estado')
    if not nuevo_estado:
        return jsonify({'error': 'Campo "estado" requerido'}), 400

    paquetes[paquete_id]['estado'] = nuevo_estado
    return jsonify({'mensaje': f'Estado del paquete {paquete_id} actualizado a "{nuevo_estado}"'}), 200

# Crear un nuevo paquete (simulado)
@app.route('/paquete', methods=['POST'])
def crear_paquete():
    data = request.get_json()
    paquete_id = data.get('id')
    destino = data.get('destino')

    if not paquete_id or not destino:
        return jsonify({'error': 'Faltan campos requeridos'}), 400

    if paquete_id in paquetes:
        return jsonify({'error': 'El paquete ya existe'}), 409

    paquetes[paquete_id] = {
        'destino': destino,
        'estado': 'En almacén'  # Estado inicial
    }
    return jsonify({'mensaje': f'Paquete {paquete_id} registrado exitosamente'}), 201

# Eliminar un paquete
@app.route('/paquete/<paquete_id>', methods=['DELETE'])
def eliminar_paquete(paquete_id):
    if paquete_id not in paquetes:
        return jsonify({'error': 'Paquete no encontrado'}), 404

    del paquetes[paquete_id]
    return jsonify({'mensaje': f'Paquete {paquete_id} eliminado exitosamente'}), 200
import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))  # Usa el puerto 8080 por defecto
    app.run(debug=True, host='0.0.0.0', port=port)
