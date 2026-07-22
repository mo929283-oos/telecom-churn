"""
===========================================================
TelcoGuard AI
Prediction Engine
===========================================================
"""

import numpy as np
import pandas as pd

from preprocessing import preprocess


# ==========================================================
# RISK LEVEL
# ==========================================================

def get_risk_level(probability):

    if probability < 0.40:
        return "Low"

    elif probability < 0.70:
        return "Medium"

    return "High"


# ==========================================================
# CONFIDENCE
# ==========================================================

def confidence_score(probability):

    probability = float(probability)

    confidence = max(
        probability,
        1 - probability
    )

    return round(confidence * 100, 2)


# ==========================================================
# CUSTOMER STATUS
# ==========================================================

def customer_status(prediction):

    if prediction == 1:
        return "Likely to Churn"

    return "Likely to Stay"


# ==========================================================
# AI RECOMMENDATION
# ==========================================================

def recommendation(probability):

    if probability >= 0.85:

        return {
            "priority": "Critical",
            "action":
            "Immediate retention campaign, assign senior support, "
            "offer premium discount and contact within 24 hours."
        }

    elif probability >= 0.70:

        return {
            "priority": "High",
            "action":
            "Provide loyalty offers, personalized discounts and "
            "technical support follow-up."
        }

    elif probability >= 0.40:

        return {
            "priority": "Medium",
            "action":
            "Monitor customer behavior and send engagement campaigns."
        }

    return {
        "priority": "Low",
        "action":
        "Customer is stable. Continue standard engagement strategy."
    }


# ==========================================================
# BUSINESS IMPACT
# ==========================================================

def business_impact(
        probability,
        monthly_charge):

    expected_loss = probability * monthly_charge * 12

    return round(expected_loss, 2)


# ==========================================================
# MAIN PREDICTION
# ==========================================================

def predict_customer(

        customer_data,

        model,

        scaler,

        model_columns

):

    X = preprocess(

        customer_data,

        scaler,

        model_columns

    )

    prediction = int(

        model.predict(X)[0]

    )

    probability = float(

        model.predict_proba(X)[0][1]

    )

    result = {

        "prediction": prediction,

        "probability": probability,

        "probability_percent":

            round(probability * 100, 2),

        "risk":

            get_risk_level(probability),

        "confidence":

            confidence_score(probability),

        "status":

            customer_status(prediction),

        "recommendation":

            recommendation(probability),

        "financial_loss":

            business_impact(

                probability,

                customer_data["MonthlyCharges"]

            )

    }

    return result


# ==========================================================
# BULK PREDICTION
# ==========================================================

def batch_predict(

        dataframe,

        model,

        scaler,

        model_columns

):

    results = []

    for _, row in dataframe.iterrows():

        prediction = predict_customer(

            row.to_dict(),

            model,

            scaler,

            model_columns

        )

        results.append(prediction)

    return pd.DataFrame(results)
