# TelcoGuard AI — Customer Churn Intelligence Platform

TelcoGuard AI is a Streamlit web app that predicts whether a telecom customer
is likely to churn (leave the company), using an XGBoost model trained on
real customer data. It's fully self-contained and ready to run.

## Project Structure

```
telcoguard/
├── app.py                  # Main entry point — run this file
├── config.py                # Global settings and constants
├── styles.py                 # Custom CSS for the UI
├── loader.py                  # Loads the trained model / scaler / columns
├── preprocessing.py            # Prepares customer input before prediction
├── predictor.py                 # Prediction logic
├── charts.py                     # Interactive Plotly charts
├── components.py                  # Reusable UI components (cards, headers)
├── financial.py                    # Financial impact calculations
├── ai_engine.py                     # AI-generated analysis and recommendations
├── simulator.py                      # What-If scenario simulator
├── report.py                          # Generates a downloadable HTML customer report
├── html_utils.py                       # Helper for rendering HTML correctly in Streamlit
├── train.py                            # Training script for the XGBoost model
├── requirements.txt
├── WA_Fn-UseC_-Telco-Customer-Churn.csv  # Original training dataset
└── models/
    ├── xgb_model.pkl
    ├── scaler.pkl
    └── model_columns.pkl
```

## Running Locally

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
2. Run the app from inside the `telcoguard` folder:
   ```
   streamlit run app.py
   ```
3. Your browser will open automatically at `http://localhost:8501`

## Retraining the Model (optional)

To retrain the model on the same customer dataset:
```
python train.py
```
This regenerates `xgb_model.pkl`, `scaler.pkl`, and `model_columns.pkl`.
Make sure to place them inside the `models/` folder afterwards.

## Deploying to Streamlit Community Cloud

1. Push this repo's contents to a GitHub repository (the `app.py` file
   should sit at the repo root, not inside a subfolder).
2. Go to [share.streamlit.io](https://share.streamlit.io), sign in with
   GitHub, and click **New app**.
3. Select your repository and branch, set **Main file path** to `app.py`,
   and click **Deploy**.

`requirements.txt` is pinned to package versions verified to load the
saved model files correctly — this avoids compatibility issues on
deployment.

## Key Features

- **Instant churn prediction** with four headline metrics: Churn
  Probability, Risk Level, Confidence, and Financial Risk.
- **🎲 Fill Random Values** button — instantly populates the input form
  with realistic random customer data, no manual typing required.
- **Five analysis tabs**: Overview, Risk Analysis (charts), AI Insights
  (recommendations), Financial Impact, and Explainable AI.
- **What-If scenario simulator** to test how changing a customer's
  attributes affects their churn risk.
- **Downloadable HTML report** per customer.

## Fixes Applied to the Original Code

1. **Split into real modules** — the original `app.py` contained the code
   for ~10 separate modules pasted together, despite having `import`
   statements expecting them as standalone files. Split into proper files
   matching those imports.
2. **Fixed model file paths** — pointed to a `models/` folder that didn't
   exist; the model files are now correctly placed there.
3. **Fixed broken CSS** — a `st.markdown("""...""")` call was closed
   prematurely, leaving ~300 lines of CSS as invalid top-level code
   (`SyntaxError`). Merged into one properly closed string.
4. **Fixed out-of-scope variables** — the Scenario Simulator and Report
   Generation sections referenced prediction data that might not exist
   yet, causing a `NameError`. Nested them inside the correct conditional
   block.
5. **Fixed raw HTML rendering as plain text** — blank lines inside HTML
   snippets were causing Streamlit's Markdown parser to cut the HTML block
   short, so tags showed up as literal text instead of being rendered.
   Added a `render_html()` helper (in `html_utils.py`) that collapses each
   snippet to a single line before rendering.
6. **Pinned `requirements.txt` versions** to match what was verified to
   work with the saved model files.
