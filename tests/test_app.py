# tests/test_app.py
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_predict_endpoint():
    # Define a sample payload (a Big Mac profile!)
    payload = {
        "total_fat": 30.0,
        "carbs": 45.0,
        "protein": 25.0,
        "sugar": 9.0
    }
    
    # Send a POST request to the API
    response = client.post("/predict", json=payload)
    
    # Check if the request was successful (Status 200 OK)
    assert response.status_code == 200
    
    # Check if we got a prediction back
    json_data = response.json()
    assert "predicted_calories" in json_data
    
    # Sanity check: Calories should be positive!
    assert json_data["predicted_calories"] > 0