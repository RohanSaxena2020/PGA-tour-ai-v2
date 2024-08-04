import json
import pickle
import os
from sklearn.preprocessing import StandardScaler

def load_model():
    try:
        base_path = os.path.dirname(__file__)
        model_path = os.path.join(base_path, 'artifacts', 'scoring_avg_model_v3.pickle')
        scaler_path = os.path.join(base_path, 'artifacts', 'scaler_v2.pickle')

        with open(model_path, 'rb') as f:
            model = pickle.load(f)
        
        with open(scaler_path, 'rb') as f:
            scaler = pickle.load(f)
        
        return model, scaler
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Required file not found: {e}")

def load_columns():
    try:
        base_path = os.path.dirname(__file__)
        columns_path = os.path.join(base_path, 'artifacts', 'columns_v2.json')

        with open(columns_path, 'r') as f:
            data = json.load(f)
            columns = data['data_columns']  # Accessing the list correctly
        return columns
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Required file not found: {e}")

def predict_scoring_average(model, scaled_data):
    prediction = model.predict(scaled_data)
    return prediction[0]
