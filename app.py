"""
===========================================================
TelcoGuard AI
Main Streamlit Application
===========================================================
"""


import random

import streamlit as st

from html_utils import render_html


# ==========================================================
# INTERNAL MODULES
# ==========================================================

from styles import load_css


from loader import load_all


from predictor import predict_customer


from components import (

    render_hero,

    render_kpis,

    customer_summary,

    recommendation_card,

    scenario_simulator,

    render_timeline,

    footer

)


# ==========================================================
# PAGE CONFIGURATION
# ==========================================================


st.set_page_config(

    page_title="TelcoGuard AI",

    page_icon="🚀",

    layout="wide",

    initial_sidebar_state="expanded"

)



# ==========================================================
# LOAD STYLE
# ==========================================================


load_css()



# ==========================================================
# LOAD MODEL RESOURCES
# ==========================================================


@st.cache_resource

def initialize():

    return load_all()



model, scaler, model_columns = initialize()



# ==========================================================
# HERO
# ==========================================================


render_hero()



# ==========================================================
# SIDEBAR
# ==========================================================


with st.sidebar:


    st.markdown(
        """
        ## 🚀 TelcoGuard AI

        ### Customer Churn Prediction

        Powered by:
        **XGBoost + Explainable AI**

        ---
        """
    )


    st.markdown(

        """

        ### Navigation


        Select customer data below


        """

    )



# ==========================================================
# CUSTOMER INPUT SECTION
# ==========================================================


render_html("""
    <div class="title">
    👤 Customer Information
    </div>
    <div class="subtitle">
    Enter customer details to predict churn risk
    </div>
    """)



# ==========================================================
# INPUT FORM
# ==========================================================


# ==========================================================
# RANDOMIZE INPUTS
# ==========================================================


def fill_random_values():

    st.session_state["gender"] = random.choice(["Male", "Female"])
    st.session_state["tenure"] = random.randint(0, 72)
    st.session_state["Partner"] = random.choice(["Yes", "No"])
    st.session_state["Dependents"] = random.choice(["Yes", "No"])

    monthly = round(random.uniform(18.0, 120.0), 2)
    st.session_state["MonthlyCharges"] = monthly
    st.session_state["TotalCharges"] = round(
        monthly * st.session_state["tenure"] * random.uniform(0.9, 1.1),
        2
    )

    st.session_state["Contract"] = random.choice(
        ["Month-to-month", "One year", "Two year"]
    )
    st.session_state["InternetService"] = random.choice(
        ["DSL", "Fiber optic", "No"]
    )
    st.session_state["TechSupport"] = random.choice(["Yes", "No"])
    st.session_state["OnlineSecurity"] = random.choice(["Yes", "No"])
    st.session_state["PaperlessBilling"] = random.choice(["Yes", "No"])
    st.session_state["PaymentMethod"] = random.choice(
        [
            "Electronic check",
            "Mailed check",
            "Bank transfer (automatic)",
            "Credit card (automatic)"
        ]
    )


st.button(
    "🎲 Fill Random Values",
    on_click=fill_random_values
)


col1, col2, col3 = st.columns(3)


with col1:

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"],
        key="gender"
    )

    tenure = st.number_input(
        "Tenure (Months)",
        min_value=0,
        max_value=100,
        value=12,
        key="tenure"
    )

    Partner = st.selectbox(
        "Partner",
        ["Yes", "No"],
        key="Partner"
    )

    Dependents = st.selectbox(
        "Dependents",
        ["Yes", "No"],
        key="Dependents"
    )


with col2:

    MonthlyCharges = st.number_input(
        "Monthly Charges",
        min_value=0.0,
        value=70.0,
        key="MonthlyCharges"
    )

    TotalCharges = st.number_input(
        "Total Charges",
        min_value=0.0,
        value=800.0,
        key="TotalCharges"
    )

    Contract = st.selectbox(
        "Contract",
        ["Month-to-month", "One year", "Two year"],
        key="Contract"
    )

    InternetService = st.selectbox(
        "Internet Service",
        ["DSL", "Fiber optic", "No"],
        key="InternetService"
    )


with col3:

    TechSupport = st.selectbox(
        "Tech Support",
        ["Yes", "No"],
        key="TechSupport"
    )

    OnlineSecurity = st.selectbox(
        "Online Security",
        ["Yes", "No"],
        key="OnlineSecurity"
    )

    PaperlessBilling = st.selectbox(
        "Paperless Billing",
        ["Yes", "No"],
        key="PaperlessBilling"
    )

    PaymentMethod = st.selectbox(
        "Payment Method",
        [
            "Electronic check",
            "Mailed check",
            "Bank transfer (automatic)",
            "Credit card (automatic)"
        ],
        key="PaymentMethod"
    )



# ==========================================================
# CUSTOMER DICTIONARY
# ==========================================================


customer = {


    "gender":

        gender,


    "tenure":

        tenure,


    "Partner":

        Partner,


    "Dependents":

        Dependents,


    "MonthlyCharges":

        MonthlyCharges,


    "TotalCharges":

        TotalCharges,


    "Contract":

        Contract,


    "InternetService":

        InternetService,


    "TechSupport":

        TechSupport,


    "OnlineSecurity":

        OnlineSecurity,


    "PaperlessBilling":

        PaperlessBilling,


    "PaymentMethod":

        PaymentMethod

}
# ==========================================================
# PREDICTION BUTTON
# ==========================================================


st.divider()


predict_button = st.button(

    "🚀 Analyze Customer Churn Risk"

)



# ==========================================================
# RUN MODEL
# ==========================================================


if predict_button:


    with st.spinner(

        "AI model is analyzing customer behavior..."

    ):


        result = predict_customer(

            customer,

            model,

            scaler,

            model_columns

        )


        st.session_state["prediction"] = result


        st.session_state["customer"] = customer



# ==========================================================
# DISPLAY RESULTS
# ==========================================================


if "prediction" in st.session_state:


    prediction_result = st.session_state["prediction"]


    customer_data = st.session_state["customer"]



    st.divider()



    # ======================================================
    # KPI SECTION
    # ======================================================


    render_kpis(

        prediction_result

    )



    st.divider()



    # ======================================================
    # DASHBOARD TABS
    # ======================================================


    tab1, tab2, tab3, tab4, tab5 = st.tabs(

        [

            "📊 Overview",

            "🎯 Risk Analysis",

            "🤖 AI Insights",

            "💰 Financial Impact",

            "🔍 Explainable AI"

        ]

    )



    # ======================================================
    # TAB 1 OVERVIEW
    # ======================================================


    with tab1:


        customer_summary(

            customer_data,

            prediction_result

        )



        st.write("")



        recommendation_card(

            prediction_result

        )



        render_timeline()



    # ======================================================
    # TAB 2 RISK ANALYSIS
    # ======================================================


    with tab2:


        from charts import (

            gauge_chart,

            probability_chart,

            customer_health

        )



        st.markdown(

            """

            ### Churn Probability Analysis

            """

        )


        col1,col2 = st.columns(2)



        with col1:


            st.plotly_chart(

                gauge_chart(

                    prediction_result["probability"]

                ),

                use_container_width=True

            )



        with col2:


            st.plotly_chart(

                probability_chart(

                    prediction_result["probability"]

                ),

                use_container_width=True

            )



        st.plotly_chart(

            customer_health(

                prediction_result["probability"]

            ),

            use_container_width=True

        )



    # ======================================================
    # TAB 3 AI INSIGHTS
    # ======================================================


    with tab3:


        from ai_engine import generate_ai_analysis



        ai_result = generate_ai_analysis(

            customer_data,

            prediction_result["probability"]

        )


        st.markdown(

            """

            ## 🤖 AI Executive Summary

            """

        )


        st.info(

            ai_result["summary"]

        )


        st.markdown(

            """

            ## Recommended Actions

            """

        )


        for action in ai_result["recommendation"]["actions"]:


            st.success(

                "✔ " + action

            )



        st.markdown(

            """

            ## Detected Risk Factors

            """

        )


        for factor in ai_result["factors"]:


            st.warning(

                f"""

                **{factor['factor']}**

               

                {factor['reason']}

                """

            )



    # ======================================================
    # TAB 4 FINANCIAL IMPACT
    # ======================================================


    with tab4:


        from financial import financial_report



        financial = financial_report(

            prediction_result["probability"],

            customer_data["MonthlyCharges"]

        )


        col1,col2,col3 = st.columns(3)



        with col1:


            st.metric(

                "Customer Lifetime Value",

                f"${financial['customer_lifetime_value']}"

            )



        with col2:


            st.metric(

                "Expected Loss",

                f"${financial['expected_loss']}"

            )



        with col3:


            st.metric(

                "Retention ROI",

                f"{financial['retention_roi']}%"

            )



        st.markdown(

            """

            ### 💡 Business Opportunity

            """

        )


        st.success(

            f"""

            Saving Opportunity:

            ${financial['saving_opportunity']}

            """

        )



    # ======================================================
    # TAB 5 EXPLAINABLE AI
    # ======================================================


    with tab5:


        st.markdown(

            """

            ## 🔍 Model Explanation

            """

        )


        st.write(

            """

            The model analyzes customer behavior,

            contract information,

            payment patterns,

            and service usage

            to estimate churn probability.

            """

        )



        st.progress(

            prediction_result["probability"]

        )
    # ==========================================================
    # SCENARIO SIMULATOR
    # ==========================================================


    with st.expander(

        "🧪 What-If Analysis & Scenario Simulator"

    ):


        scenario_changes = scenario_simulator()



        if st.button(

            "Run Scenario Simulation"

        ):


            from simulator import (

                run_scenario,

                compare_results

            )


            scenario_output = run_scenario(

                customer_data,

                scenario_changes,

                model,

                scaler,

                model_columns

            )


            comparison = compare_results(

                prediction_result,

                scenario_output["result"]

            )



            st.subheader(

                "Scenario Result"

            )



            col1,col2,col3 = st.columns(3)



            with col1:


                st.metric(

                    "Original Risk",

                    f"{comparison['old_probability']}%"

                )



            with col2:


                st.metric(

                    "New Risk",

                    f"{comparison['new_probability']}%"

                )



            with col3:


                st.metric(

                    "Improvement",

                    f"{comparison['improvement']}%"

                )



            if comparison["status"] == "Improved":


                st.success(

                    comparison["message"]

                )


            elif comparison["status"] == "Worse":


                st.error(

                    comparison["message"]

                )


            else:


                st.info(

                    comparison["message"]

                )



    # ==========================================================
    # REPORT GENERATION
    # ==========================================================


    st.divider()



    st.markdown(

        """

        ## 📥 Download Center

        Generate a complete AI customer report

        """

    )



    if st.button(

        "Generate Customer Report"

    ):


        from report import create_report


        from ai_engine import generate_ai_analysis


        from financial import financial_report



        ai_result = generate_ai_analysis(

            customer_data,

            prediction_result["probability"]

        )



        financial = financial_report(

            prediction_result["probability"],

            customer_data["MonthlyCharges"]

        )



        report_path = create_report(

            customer_data,

            prediction_result,

            ai_result,

            financial

        )



        st.session_state["report"] = report_path



    if "report" in st.session_state:


        with open(

            st.session_state["report"],

            "rb"

        ) as file:


            st.download_button(

                label="⬇ Download TelcoGuard Report",

                data=file,

                file_name="TelcoGuard_AI_Report.html",

                mime="text/html"

            )



# ==========================================================
# FOOTER
# ==========================================================


footer()
