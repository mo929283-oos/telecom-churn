"""
===========================================================
TelcoGuard AI
Professional Plotly Charts
===========================================================
"""

import plotly.graph_objects as go
import plotly.express as px
import pandas as pd


# ==========================================================
# COLOR PALETTE
# ==========================================================

PRIMARY = "#4F8BF9"
SUCCESS = "#22C55E"
WARNING = "#F59E0B"
DANGER = "#EF4444"
CARD = "#1E293B"
BACKGROUND = "#0F172A"


# ==========================================================
# COMMON LAYOUT
# ==========================================================

def update_layout(fig, title):

    fig.update_layout(

        title=dict(
            text=title,
            x=0.5,
            font=dict(size=20)
        ),

        template="plotly_dark",

        paper_bgcolor=BACKGROUND,

        plot_bgcolor=BACKGROUND,

        margin=dict(
            l=20,
            r=20,
            t=50,
            b=20
        ),

        font=dict(
            family="Poppins",
            color="white"
        )

    )

    return fig


# ==========================================================
# GAUGE CHART
# ==========================================================

def gauge_chart(probability):

    value = probability * 100

    fig = go.Figure(

        go.Indicator(

            mode="gauge+number",

            value=value,

            number={
                "suffix": "%"
            },

            gauge={

                "axis": {

                    "range": [0, 100]

                },

                "bar": {

                    "color": PRIMARY

                },

                "steps": [

                    {

                        "range": [0, 40],

                        "color": SUCCESS

                    },

                    {

                        "range": [40, 70],

                        "color": WARNING

                    },

                    {

                        "range": [70, 100],

                        "color": DANGER

                    }

                ]

            }

        )

    )

    return update_layout(

        fig,

        "Churn Risk Gauge"

    )


# ==========================================================
# DONUT CHART
# ==========================================================

def probability_chart(probability):

    stay = round(

        (1 - probability) * 100,

        2

    )

    churn = round(

        probability * 100,

        2

    )

    fig = px.pie(

        names=[

            "Stay",

            "Churn"

        ],

        values=[

            stay,

            churn

        ],

        hole=.65,

        color_discrete_sequence=[

            SUCCESS,

            DANGER

        ]

    )

    return update_layout(

        fig,

        "Customer Probability"

    )


# ==========================================================
# RISK BAR
# ==========================================================

def risk_bar(probability):

    fig = go.Figure()

    fig.add_trace(

        go.Bar(

            x=["Risk"],

            y=[

                probability * 100

            ],

            marker_color=PRIMARY,

            width=[0.45]

        )

    )

    fig.update_yaxes(

        range=[0,100]

    )

    return update_layout(

        fig,

        "Risk Score"

    )


# ==========================================================
# FINANCIAL IMPACT
# ==========================================================

def financial_chart(loss):

    fig = go.Figure(

        go.Indicator(

            mode="number",

            value=loss,

            number={

                "prefix":"$",

                "valueformat":".2f"

            }

        )

    )

    return update_layout(

        fig,

        "Estimated Annual Revenue Loss"

    )


# ==========================================================
# KPI CARD
# ==========================================================

def kpi_card(

        title,

        value,

        color=PRIMARY

):

    fig = go.Figure()

    fig.add_annotation(

        text=f"<b>{value}</b>",

        x=.5,

        y=.6,

        showarrow=False,

        font=dict(

            size=38,

            color=color

        )

    )

    fig.add_annotation(

        text=title,

        x=.5,

        y=.28,

        showarrow=False,

        font=dict(

            size=17,

            color="white"

        )

    )

    fig.update_layout(

        template="plotly_dark",

        paper_bgcolor=CARD,

        plot_bgcolor=CARD,

        xaxis=dict(

            visible=False

        ),

        yaxis=dict(

            visible=False

        ),

        margin=dict(

            l=0,

            r=0,

            t=0,

            b=0

        )

    )

    return fig


# ==========================================================
# FEATURE IMPORTANCE
# ==========================================================

def feature_importance_chart(df):

    fig = px.bar(

        df.head(10),

        x="Importance",

        y="Feature",

        orientation="h",

        color="Importance",

        color_continuous_scale="Blues"

    )

    fig.update_layout(

        yaxis=dict(

            autorange="reversed"

        )

    )

    return update_layout(

        fig,

        "Top Important Features"

    )


# ==========================================================
# CUSTOMER HEALTH
# ==========================================================

def customer_health(probability):

    health = (1-probability)*100

    fig = go.Figure(

        go.Indicator(

            mode="gauge+number",

            value=health,

            number={

                "suffix":"%"

            },

            gauge={

                "axis":{

                    "range":[0,100]

                },

                "bar":{

                    "color":SUCCESS

                }

            }

        )

    )

    return update_layout(

        fig,

        "Customer Health Score"

    )


# ==========================================================
# TIMELINE
# ==========================================================

def timeline():

    data = pd.DataFrame({

        "Stage":[

            "Customer Joined",

            "Usage Increased",

            "Risk Detected",

            "Retention Action",

            "Prediction"

        ],

        "Value":[

            1,

            2,

            3,

            4,

            5

        ]

    })

    fig = px.line(

        data,

        x="Stage",

        y="Value",

        markers=True

    )

    return update_layout(

        fig,

        "Customer Journey"

    )
