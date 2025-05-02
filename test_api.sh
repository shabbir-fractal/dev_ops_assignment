#!/bin/bash
curl -X 'POST' \
  'http://127.0.0.1:8001/predict' \
  -H 'Content-Type: application/json' \
  -d '{
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

}'
