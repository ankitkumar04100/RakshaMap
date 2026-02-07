# 🗄️ SQLite Prototype Database
The backend uses a SQLite database to store historical incident data. It can be generated using Python scripts or DB Browser for SQLite.

## Example Table Schema
```
CREATE TABLE incidents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    latitude REAL NOT NULL,
    longitude REAL NOT NULL,
    time_of_day TEXT NOT NULL,
    severity INTEGER,
    description TEXT
);
```
- id → Unique identifier for each incident
- latitude → Latitude of incident location
- longitude → Longitude of incident location
- time_of_day → Time of incident (format: HH:MM)
- severity → Numerical score of incident severity (optional)
- description → Short text describing the incident

## ⚡ How to Run the Backend

**1. Navigate to the backend folder**
```
cd backend
```

**2. Install dependencies**
```
pip install fastapi uvicorn pydantic
```

**3. Start the API server**
```
uvicorn main:app --reload
```

**4. Test the API**
Open in browser or Postman:
```
http://127.0.0.1:8000/risk?lat=28.6139&lon=77.209&time_of_day=21:30
```
This returns a JSON object with risk score and risk category.
