from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/productos", methods=["GET"])
def productos():
    return jsonify([
        {"id": 1, "nombre": "Laptop", "precio": 1500},
        {"id": 2, "nombre": "Mouse", "precio": 20},
        {"id": 3, "nombre": "Teclado", "precio": 45}
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)