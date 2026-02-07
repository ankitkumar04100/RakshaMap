import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import pickle
import os

# Load dataset
dataset_path = os.path.join(os.path.dirname(__file__), "dataset/incidents.csv")
data = pd.read_csv(dataset_path)

# Feature Engineering
# Convert time_of_day "HH:MM" to integer
data['time_int'] = data['time_of_day'].str.replace(':', '').astype(int)

X = data[['latitude', 'longitude', 'time_int']]
y = data['severity']  # Risk score (0-10 scale)

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# Save trained model
model_path = os.path.join(os.path.dirname(__file__), "model.pkl")
with open(model_path, 'wb') as f:
    pickle.dump(model, f)

print("Model trained and saved as model.pkl")
