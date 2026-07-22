"""
===========================================================
TelcoGuard AI
Dashboard Components
===========================================================
"""

import streamlit as st

from html_utils import render_html

from config import (
    PROJECT_NAME,
    HERO_TITLE,
    HERO_SUBTITLE
)


# ==========================================================
# HERO SECTION
# ==========================================================

def render_hero():

    render_html(f"""

        <div class="hero">

            <h1>
                🚀 {HERO_TITLE}
            </h1>


            <p>
                {HERO_SUBTITLE}
            </p>


            <br>

            <span style="
            background:#2563EB;
            padding:8px 18px;
            border-radius:20px;
            font-weight:600;
            ">

            XGBoost Powered Intelligence

            </span>

        </div>

        """)


# ==========================================================
# KPI CARD
# ==========================================================

def metric_card(

        title,

        value,

        icon="📊"

):

    render_html(f"""

        <div class="metric-card">

            <div style="
            font-size:30px;
            ">
            {icon}
            </div>


            <div class="metric-title">

            {title}

            </div>


            <div class="metric-value">

            {value}

            </div>


        </div>

        """)


# ==========================================================
# KPI ROW
# ==========================================================

def render_kpis(

        prediction_result

):

    col1,col2,col3,col4 = st.columns(4)


    probability = (
        prediction_result["probability_percent"]
    )


    with col1:

        metric_card(

            "Churn Probability",

            f"{probability}%",

            "⚠️"

        )


    with col2:

        metric_card(

            "Risk Level",

            prediction_result["risk"],

            "🔥"

        )


    with col3:

        metric_card(

            "Confidence",

            f"{prediction_result['confidence']}%",

            "🎯"

        )


    with col4:

        metric_card(

            "Financial Risk",

            f"${prediction_result['financial_loss']}",

            "💰"

        )


# ==========================================================
# RISK BADGE
# ==========================================================

def risk_badge(level):


    if level == "Low":

        css="badge-low"

        icon="🟢"


    elif level == "Medium":

        css="badge-medium"

        icon="🟡"


    else:

        css="badge-high"

        icon="🔴"



    render_html(f"""

        <span class="{css}">

        {icon} {level} Risk

        </span>

        """)


# ==========================================================
# CUSTOMER SUMMARY
# ==========================================================

def customer_summary(

        customer_data,

        prediction_result

):

    render_html("""

        <h2>

        👤 Customer Intelligence Summary

        </h2>

        """)


    col1,col2 = st.columns(2)



    with col1:

        render_html(f"""

            <div class="glass">


            <h4>
            Customer Profile
            </h4>


            <p>
            Tenure:
            <b>
            {customer_data.get('tenure')}
            </b>
            months
            </p>


            <p>
            Monthly Charges:
            <b>
            ${customer_data.get('MonthlyCharges')}
            </b>
            </p>


            <p>
            Contract:
            <b>
            {customer_data.get('Contract')}
            </b>
            </p>


            </div>

            """)



    with col2:

        render_html(f"""

            <div class="glass">


            <h4>
            AI Prediction
            </h4>


            <p>
            Status:
            <b>
            {prediction_result['status']}
            </b>
            </p>


            <p>
            Risk:
            </p>

            """)


        risk_badge(

            prediction_result["risk"]

        )


        render_html("</div>")


# ==========================================================
# AI RECOMMENDATION
# ==========================================================

def recommendation_card(

        prediction_result

):

    rec = prediction_result["recommendation"]


    render_html(f"""

        <div class="ai-card">


        <h2>
        🤖 AI Retention Recommendation
        </h2>


        <h4>

        Priority:

        <span style="
        color:#38BDF8;
        ">

        {rec['priority']}

        </span>

        </h4>


        <p>

        {rec['action']}

        </p>


        </div>


        """)
# ==========================================================
# EXECUTIVE DASHBOARD HEADER
# ==========================================================

def section_title(title, subtitle=None):

    render_html(f"""

        <div class="title">

        {title}

        </div>

        """)


    if subtitle:

        render_html(f"""

            <div class="subtitle">

            {subtitle}

            </div>

            """)



# ==========================================================
# CHART CONTAINER
# ==========================================================

def chart_container(

        title,

        chart

):

    render_html(f"""

        <div class="chart-card">

        <h3>

        {title}

        </h3>

        </div>

        """)


    st.plotly_chart(

        chart,

        use_container_width=True

    )



# ==========================================================
# RISK ANALYSIS SECTION
# ==========================================================

def risk_analysis(

        prediction_result,

        gauge,

        probability_chart,

        health_chart

):

    section_title(

        "🎯 AI Risk Intelligence",

        "Advanced churn probability analysis"

    )


    col1,col2 = st.columns(2)


    with col1:

        st.plotly_chart(

            gauge,

            use_container_width=True

        )


    with col2:

        st.plotly_chart(

            probability_chart,

            use_container_width=True

        )


    st.plotly_chart(

        health_chart,

        use_container_width=True

    )



# ==========================================================
# FINANCIAL IMPACT
# ==========================================================

def financial_card(

        loss

):


    render_html(f"""

        <div class="glass">


        <h2>

        💰 Financial Impact

        </h2>


        <h1 style="
        color:#EF4444;
        ">

        ${loss}

        </h1>


        <p>

        Estimated yearly revenue at risk

        </p>


        </div>

        """)



# ==========================================================
# TIMELINE COMPONENT
# ==========================================================

def render_timeline():

    section_title(

        "📅 Customer Journey Timeline"

    )


    steps = [

        (
            "🟢",
            "Customer Joined",
            "Initial subscription created"
        ),

        (
            "🔵",
            "Usage Monitoring",
            "Behavior analysis started"
        ),

        (
            "🟡",
            "Risk Detection",
            "AI detected possible churn"
        ),

        (
            "🟣",
            "Retention Action",
            "Personalized offer generated"
        ),

        (
            "🔴",
            "Follow Up",
            "Customer success team contact"
        )

    ]


    html=""


    for icon,title,text in steps:


        html += f"""

        <div class="timeline-item">

        <h4>

        {icon} {title}

        </h4>


        <p>

        {text}

        </p>


        </div>

        """


    render_html(f"""

        <div class="timeline">

        {html}

        </div>

        """)



# ==========================================================
# WHAT IF SIMULATOR INPUTS
# ==========================================================

def scenario_simulator():

    section_title(

        "🧪 What-If Scenario Simulator",

        "Test how customer changes affect churn probability"

    )


    col1,col2,col3 = st.columns(3)



    with col1:

        contract = st.selectbox(

            "Contract",

            [

                "Month-to-month",

                "One year",

                "Two year"

            ],

            key="scenario_contract"

        )


    with col2:

        monthly = st.slider(

            "Monthly Charges",

            10,

            150,

            70,

            key="scenario_monthly"

        )


    with col3:

        tenure = st.slider(

            "Tenure",

            0,

            80,

            20,

            key="scenario_tenure"

        )


    return {

        "Contract": contract,

        "MonthlyCharges": monthly,

        "tenure": tenure

    }



# ==========================================================
# DOWNLOAD CENTER
# ==========================================================

def download_center(

        report_file

):

    section_title(

        "📥 Report Center"

    )


    with open(

        report_file,

        "rb"

    ) as file:


        st.download_button(

            label="Download Customer Report",

            data=file,

            file_name="TelcoGuard_Report.pdf",

            mime="application/pdf"

        )



# ==========================================================
# FEATURE IMPORTANCE
# ==========================================================

def feature_section(

        chart

):

    section_title(

        "🔍 Explainable AI"

    )


    render_html("""

        <div class="glass">

        Model explanation using feature contribution analysis.

        </div>

        """)


    st.plotly_chart(

        chart,

        use_container_width=True

    )



# ==========================================================
# FOOTER
# ==========================================================

def footer():

    render_html("""

        <div class="footer">

        🚀 TelcoGuard AI | Customer Churn Intelligence Platform

        </div>

        """)
