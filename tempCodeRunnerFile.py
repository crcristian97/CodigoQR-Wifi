from flask import Flask, render_template, request, jsonify
from backend.generate_qr import generate_qr

app = Flask(__name__)

# Ruta para servir la página principal
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para generar el código QR
@app.route('/generate_qr', methods=['POST'])
def generate_qr_code():
    data = request.json
    ssid = data.get('ssid')
    password = data.get('password')
    
    if not ssid or not password:
        return jsonify({"error": "SSID and Password are required"}), 400
    
    image_path = generate_qr(ssid, password)
    return jsonify({"image_path": image_path}), 200

if __name__ == '__main__':
    app.run(debug=True)
