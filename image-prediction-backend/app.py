from flask import Flask, request, jsonify
from flask_cors import CORS
import os

from yolo_model import yolo_predict

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    filename = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filename)

    result = yolo_predict(filename) #result is the variable containg final prediction- this needs to converted to speech

    print(result)

    return jsonify({'prediction': result}) #set the value for prediction state in react imageUpload.js file


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)

