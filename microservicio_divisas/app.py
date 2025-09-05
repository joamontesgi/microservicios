from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017/")
db = client["microservicio"]
divisas_collection = db["divisas"]

@app.route('/divisas', methods=['POST'])
def agregar_divisa():
    data = request.get_json()
    result = divisas_collection.insert_one({
        "origen": data["origen"],
        "destino": data["destino"],
        "valor": float(data["valor"]) 
    })
    return jsonify({
        "mensaje": "Divisa guardada correctamentaaaaae",
        "id": str(result.inserted_id)
    }), 201

@app.route('/convertir', methods=['POST'])
def convertir_divisa():
    data = request.get_json()
    origen = data["origen"]
    destino = data["destino"]
    cantidad = float(data["cantidad"])
    tasa = divisas_collection.find_one({"origen": origen, "destino": destino})
    equivalencia = cantidad * tasa["valor"]
    return jsonify({
        "origen": origen,
        "destino": destino,
        "cantidad": cantidad,
        "tasa": tasa["valor"],
        "resultado": equivalencia
    }), 200


@app.route("/par", methods=['POST'])
def par():
    numero = request.get_json()
    valor = numero.get('val')
    if(valor%2==0):
        return "Es par"
    else:
        return "No es par"
    







if __name__ == '__main__':
    app.run(debug=True, port=5000)
