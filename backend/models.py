import pickle
import os
import math

# Load trained model
MODEL_PATH = os.path.join(os.path.dirname(__file__), "../ai_model/model.pkl")
with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

def get_risk_score(lat, lon, time_of_day):
    """
    Simple example: Predicts risk score (0-100) using trained ML model
    """
    # Example features vector
    features = [[lat, lon, int(time_of_day.replace(":", ""))]]
    
    # Predict risk score
    score = model.predict(features)[0]
    
    # Categorize risk
    if score < 35:
        category = "Safe"
    elif score < 70:
        category = "Moderate"
    else:
        category = "High-Risk"
    
    return math.ceil(score), category
