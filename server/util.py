import json
import pickle
from sklearn.preprocessing import StandardScaler

def load_model():
    # Load the pre-trained model
    with open('artifacts/scoring_avg_model_v2.pickle', 'rb') as f:
        model = pickle.load(f)
    
    # Load the scaler
    with open('artifacts/scaler.pickle', 'rb') as f:
        scaler = pickle.load(f)
    
    return model, scaler

def load_columns():
    # Load the model columns
    with open('artifacts/columns.json', 'r') as f:
        data = json.load(f)
        columns = data['data_columns']  # Accessing the list correctly
    return columns

def predict_scoring_average(model, scaled_data):
    prediction = model.predict(scaled_data)
    return prediction[0]
