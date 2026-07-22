"""
===========================================================
TelcoGuard AI
Configuration File
===========================================================
Author : Mostafa Ahmed
Project: TelcoGuard AI
===========================================================
"""

from pathlib import Path

# =============================================================================
# PROJECT PATHS
# =============================================================================

BASE_DIR = Path(__file__).resolve().parent

MODEL_DIR = BASE_DIR / "models"

ASSETS_DIR = BASE_DIR / "assets"

REPORT_DIR = BASE_DIR / "reports"

REPORT_DIR.mkdir(exist_ok=True)


# =============================================================================
# MODEL FILES
# =============================================================================

MODEL_PATH = MODEL_DIR / "xgb_model.pkl"

SCALER_PATH = MODEL_DIR / "scaler.pkl"

MODEL_COLUMNS_PATH = MODEL_DIR / "model_columns.pkl"


# =============================================================================
# PROJECT INFO
# =============================================================================

PROJECT_NAME = "TelcoGuard AI"

PROJECT_VERSION = "2.0"

AUTHOR = "Mostafa Ahmed"

COMPANY = "TelcoGuard Analytics"

MODEL_NAME = "XGBoost Classifier"

MODEL_TYPE = "Binary Classification"

TARGET = "Customer Churn"


# =============================================================================
# THEME COLORS
# =============================================================================

PRIMARY = "#4F8BF9"

SECONDARY = "#1E293B"

SUCCESS = "#16A34A"

WARNING = "#F59E0B"

DANGER = "#DC2626"

INFO = "#38BDF8"

BACKGROUND = "#0F172A"

CARD = "#1E293B"

TEXT = "#F8FAFC"

MUTED = "#94A3B8"


# =============================================================================
# RISK LEVELS
# =============================================================================

LOW_RISK = 0.40

MEDIUM_RISK = 0.70

HIGH_RISK = 1.00


# =============================================================================
# FINANCIAL SETTINGS
# =============================================================================

DEFAULT_CUSTOMER_VALUE = 1200

DEFAULT_RETENTION_COST = 120

DEFAULT_PROFIT_MARGIN = 0.35


# =============================================================================
# NUMERIC FEATURES
# =============================================================================

NUMERIC_COLUMNS = [

    "tenure",

    "MonthlyCharges",

    "TotalCharges"

]


# =============================================================================
# YES / NO FEATURES
# =============================================================================

YES_NO_COLUMNS = [

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


# =============================================================================
# CATEGORICAL FEATURES
# =============================================================================

CATEGORICAL_COLUMNS = {

    "gender": [

        "Male",

        "Female"

    ],

    "InternetService": [

        "DSL",

        "Fiber optic",

        "No"

    ],

    "Contract": [

        "Month-to-month",

        "One year",

        "Two year"

    ],

    "PaymentMethod": [

        "Electronic check",

        "Mailed check",

        "Bank transfer (automatic)",

        "Credit card (automatic)"

    ]

}


# =============================================================================
# KPI DEFAULT VALUES
# =============================================================================

DEFAULT_ACCURACY = 0.84

DEFAULT_PRECISION = 0.77

DEFAULT_RECALL = 0.73

DEFAULT_F1 = 0.75

DEFAULT_AUC = 0.88


# =============================================================================
# RISK LABELS
# =============================================================================

RISK_LABELS = {

    "Low": "#22C55E",

    "Medium": "#F59E0B",

    "High": "#EF4444"

}


# =============================================================================
# DASHBOARD TEXT
# =============================================================================

HERO_TITLE = "TelcoGuard AI"

HERO_SUBTITLE = (
    "Enterprise Customer Churn Intelligence Platform "
    "Powered by XGBoost & Explainable AI"
)


FOOTER = (
    "© 2026 TelcoGuard AI | Built with Streamlit + Plotly"
)
