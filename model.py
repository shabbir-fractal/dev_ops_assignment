# model.py
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor


def convert_df(df):
    # Convert non-numeric columns to numeric
    df["Warehouse_block"] = df["Warehouse_block"].replace(["A","B","C","D","E", "F"], [1,2,3,4,5,6])
    df["Mode_of_Shipment"] = df["Mode_of_Shipment"].replace(["Flight","Ship","Road"], [1,2,3])
    df["Product_importance"] = df["Product_importance"].replace(["low","medium","high"], [1,2,3])
    df["Gender"] = df["Gender"].replace(["F","M"], [1,2])


def prepare_model():
    # Load dataset
    df = pd.read_csv("ecommerce_shipment_data.csv")
    convert_df(df)

    FEATURES = ["Warehouse_block", "Mode_of_Shipment", "Customer_care_calls", "Customer_rating", "Cost_of_the_Product", "Prior_purchases", "Product_importance", "Gender", "Discount_offered", "Weight_in_gms"]
    TARGET = "Reached.on.Time_Y.N"

    X = df[FEATURES]
    y = df[TARGET]

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train a simple model
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Save the trained model
    joblib.dump(model, "ecommerce_shipment.pkl")


# prepare_model()


def load_model():
    """Loads the trained model."""
    return joblib.load("ecommerce_shipment.pkl")


def predict_shipment(input_data: dict):
    """Takes JSON input and predicts sales."""
    model = load_model()
    df_input = pd.DataFrame([input_data])
    convert_df(df_input)
    prediction = model.predict(df_input)
    return prediction[0]
