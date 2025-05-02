# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import model

app = FastAPI()

# "Warehouse_block", "Mode_of_Shipment", "Customer_care_calls", "Customer_rating", "Cost_of_the_Product", "Prior_purchases", "Product_importance", "Gender", "Discount_offered", "Weight_in_gms"
# D,Flight,4,2,177,3,low,F,44,1233,1
class PredictionInput(BaseModel):
    Warehouse_block: str    # A to F
    Mode_of_Shipment: str   # Flight, Ship, Road
    Customer_care_calls: int
    Customer_rating: int    # 1 to 5
    Cost_of_the_Product: int
    Prior_purchases: int
    Product_importance: str # low, medium, high
    Gender: str # M or F
    Discount_offered: int
    Weight_in_gms: int

@app.get("/")
def home():
    return {"message": "Welcome to the MLOps ECommerce Shipment Forecast API"}

@app.post("/predict")
def predict(data: PredictionInput):
    print("input data")
    print(data)
    try:
        prediction = model.predict_shipment(data.dict())
        print("output data")
        print(prediction)
        return {"shipment_prediction": prediction}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
