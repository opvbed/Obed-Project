from flask import Flask, render_template, request, jsonify
from models.model import AIModel
from utils.helpers import preprocess_data

app = Flask(__name__)
model = AIModel()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    processed_data = preprocess_data(data)
    prediction = model.predict(processed_data)
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)