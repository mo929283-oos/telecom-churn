"""
===========================================================
TelcoGuard AI
Data Preprocessing
===========================================================
"""

import pandas as pd

from config import NUMERIC_COLUMNS


# ==========================================================
# YES / NO ENCODING
# ==========================================================

YES_NO_MAPPING = {
    "Yes": 1,
    "No": 0
}


# ==========================================================
# GENDER
# ==========================================================

GENDER_MAPPING = {
    "Male": 1,
    "Female": 0
}


# ==========================================================
# CLEAN INPUT
# ==========================================================

def clean_input(data: dict):

    df = pd.DataFrame([data])

    # -----------------------------------------

    if "TotalCharges" in df.columns:

        df["TotalCharges"] = (
            pd.to_numeric(
                df["TotalCharges"],
                errors="coerce"
            )
            .fillna(0)
        )

    # -----------------------------------------

    for col in NUMERIC_COLUMNS:

        if col in df.columns:

            df[col] = pd.to_numeric(
                df[col],
                errors="coerce"
            ).fillna(0)

    return df


# ==========================================================
# YES / NO
# ==========================================================

def encode_binary(df):

    binary_columns = [

        "Partner",

        "Dependents",

        "PhoneService",

        "MultipleLines",

        "OnlineSecurity",

        "OnlineBackup",

        "DeviceProtection",

        "TechSupport",

        "StreamingTV",

        "StreamingMovies",

        "PaperlessBilling"

    ]

    for col in binary_columns:

        if col in df.columns:

            df[col] = df[col].map(
                YES_NO_MAPPING
            )

    return df


# ==========================================================
# GENDER
# ==========================================================

def encode_gender(df):

    if "gender" in df.columns:

        df["gender"] = df["gender"].map(
            GENDER_MAPPING
        )

    return df


# ==========================================================
# ONE HOT
# ==========================================================

def one_hot_encode(df):

    categorical = [

        "InternetService",

        "Contract",

        "PaymentMethod"

    ]

    df = pd.get_dummies(

        df,

        columns=categorical,

        dtype=int

    )

    return df


# ==========================================================
# MATCH TRAINING COLUMNS
# ==========================================================

def align_columns(

        df,

        model_columns

):

    for col in model_columns:

        if col not in df.columns:

            df[col] = 0

    df = df[model_columns]

    return df


# ==========================================================
# SCALE
# ==========================================================

def scale_numeric(

        df,

        scaler

):

    df[NUMERIC_COLUMNS] = scaler.transform(

        df[NUMERIC_COLUMNS]

    )

    return df


# ==========================================================
# COMPLETE PIPELINE
# ==========================================================

def preprocess(

        customer_data,

        scaler,

        model_columns

):

    df = clean_input(

        customer_data

    )

    df = encode_binary(df)

    df = encode_gender(df)

    df = one_hot_encode(df)

    df = align_columns(

        df,

        model_columns

    )

    df = scale_numeric(

        df,

        scaler

    )

    return df
