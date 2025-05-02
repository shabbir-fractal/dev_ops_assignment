# test_main.py
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the MLOps ECommerce Shipment Forecast API"}

def test_predict():
    response = client.post("/predict", json={
        "Warehouse_block": "C",
        "Mode_of_Shipment": "Road",
        "Customer_care_calls":33,
        "Customer_rating": 4,
        "Cost_of_the_Product": 344,
        "Prior_purchases": 4,
        "Product_importance": "low",
        "Gender": "F",
        "Discount_offered": 10,
        "Weight_in_gms": 100
    })
    assert response.status_code == 200
    assert "shipment_prediction" in response.json()
