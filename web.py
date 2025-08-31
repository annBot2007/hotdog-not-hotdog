from flask import Flask, render_template, request, jsonify
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

print("DEBUG API_URL:", os.getenv("HUGGING_FACE_API_URL"))
print("DEBUG API_KEY:", os.getenv("HUGGING_FACE_API_KEY"))

API_URL = os.getenv("HUGGING_FACE_API_URL")
headers = {'Authorization': f'Bearer {os.getenv("HUGGING_FACE_API_KEY")}'}

app = Flask(__name__)

def query(image_bytes):
    response = requests.post(API_URL, headers=headers, data=image_bytes)
    return response.json()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if "file" not in request.files:
        return "No file part in the request", 400

    file = request.files["file"]
    if file.filename == "":
        return "No selected file", 400

    # now you can save or process it
    file.save("uploaded_" + file.filename)
    return "File uploaded successfully!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=81)
