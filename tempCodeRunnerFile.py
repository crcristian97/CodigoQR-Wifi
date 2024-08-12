from flask import Flask, render_template, request, jsonify
from backend.generate_qr import generate_qr

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_qr', methods=['POST'])
def generate_qr_code():
    try:
        data = request.json
        ssid = data.get('ssid')
        password = data.get('password')

        if not ssid or not password:
            return jsonify({"error": "SSID and Password are required"}), 400

        image_path = generate_qr(ssid, password)
        if not image_path:
            return jsonify({"error": "Failed to generate QR code"}), 500

        return jsonify({"image_path": image_path}), 200

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "An internal error occurred"}), 500

if __name__ == '__main__':
    app.run(debug=True)
