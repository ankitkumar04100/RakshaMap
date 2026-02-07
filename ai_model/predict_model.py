import pickle
import os

# Load trained model
model_path = os.path.join(os.path.dirname(__file__), "model.pkl")
with open(model_path, 'rb') as f:
    model = pickle.load(f)

def predict_risk(lat, lon, time_of_day):
    """
    Predict risk score and category
    """
    time_int = int(time_of_day.replace(":", ""))
    features = [[lat, lon, time_int]]
    score = model.predict(features)[0]

    if score < 3.5:
        category = "Safe"
    elif score < 7:
        category = "Moderate"
    else:
        category = "High-Risk"

    return round(score, 1), category

# Example usage
if __name__ == "__main__":
    lat, lon, time_of_day = 28.6139, 77.209, "21:30"
    score, category = predict_risk(lat, lon, time_of_day)
    print(f"Predicted Risk Score: {score}, Category: {category}")
