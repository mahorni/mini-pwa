from flask import Flask, request
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Enables CORS

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_photo():
    file = request.files.get('photo')
    if file:
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)
        return f"Photo saved to {filepath}", 200
    return "No file received", 400

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
