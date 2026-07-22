"""
===========================================================
TelcoGuard AI
Model Loader
===========================================================
"""

import joblib
import streamlit as st

from config import (
    MODEL_PATH,
    SCALER_PATH,
    MODEL_COLUMNS_PATH
)


# ==========================================================
# LOAD MODEL
# ==========================================================

@st.cache_resource(show_spinner=False)
def load_model():
    """
    Load trained XGBoost model.
    """

    model = joblib.load(MODEL_PATH)

    return model


# ==========================================================
# LOAD SCALER
# ==========================================================

@st.cache_resource(show_spinner=False)
def load_scaler():
    """
    Load StandardScaler.
    """

    scaler = joblib.load(SCALER_PATH)

    return scaler


# ==========================================================
# LOAD MODEL COLUMNS
# ==========================================================

@st.cache_resource(show_spinner=False)
def load_columns():
    """
    Load training columns.
    """

    columns = joblib.load(MODEL_COLUMNS_PATH)

    return columns


# ==========================================================
# LOAD EVERYTHING
# ==========================================================

@st.cache_resource(show_spinner=False)
def load_all():

    model = load_model()

    scaler = load_scaler()

    columns = load_columns()

    return model, scaler, columns


# ==========================================================
# CHECK FILES
# ==========================================================

def validate():

    errors = []

    try:
        load_model()
    except Exception as e:
        errors.append(
            f"Model Error : {e}"
        )

    try:
        load_scaler()
    except Exception as e:
        errors.append(
            f"Scaler Error : {e}"
        )

    try:
        load_columns()
    except Exception as e:
        errors.append(
            f"Columns Error : {e}"
        )

    return errors
