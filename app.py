from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np

app = Flask(__name__)
CORS(app)

# Load the trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return "Model backend is up and running!"

# Example: Predict endpoint
@app.route('/api/predict', methods=['POST'])
def predict():
    data = request.get_json()
    
    # Example: Extract features from request body
    try:
        features = data["customerAge","gender","dependentCount","educationLevel","maritalStatus","incomeCategory","cardCategory","monthsOnBook","totalRelationshipCount","monthsInactive12Mon","contactsCount12Mon","creditLimit","totalRevolvingBal","avgOpenToBuy","totalAmtChngQ4Q1","totalTransAmt","totalTransCt","totalCtChngQ4Q1","avgUtilizationRatio"]
  # Expecting a list: [val1, val2, val3, ...]
        prediction = model.predict([features])  # Model expects 2D array
        return jsonify({'prediction': prediction[0]})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
