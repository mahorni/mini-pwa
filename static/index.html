from flask import Flask, request, send_from_directory
from flask_cors import CORS
import os

# Tell Flask that 'static' is your static folder, and serve it at URL '/'
app = Flask(__name__, static_folder='static', static_url_path='')
CORS(app)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Serve index.html for the root URL
@app.route('/')
def index():
    return app.send_static_file('index.html')

# Serve any other static asset too (manifest.json, service-worker.js, etc.)
@app.route('/<path:filename>')
def static_files(filename):
    return send_from_directory(app.static_folder, filename)

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
