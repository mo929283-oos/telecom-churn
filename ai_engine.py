"""
===========================================================
TelcoGuard AI
Explainable AI Recommendation Engine
===========================================================
"""


# ==========================================================
# RISK EXPLANATION
# ==========================================================

def analyze_risk_factors(customer):

    factors = []


    # Contract Analysis

    if customer.get("Contract") == "Month-to-month":

        factors.append({

            "factor":
                "Monthly Contract",

            "impact":
                "High",

            "reason":
                "Monthly contracts have higher churn probability."

        })


    # Tenure Analysis

    tenure = customer.get(
        "tenure",
        0
    )


    if tenure < 12:

        factors.append({

            "factor":
                "New Customer",

            "impact":
                "Medium",

            "reason":
                "Customers in early lifecycle need stronger engagement."

        })


    # Charges Analysis

    monthly = customer.get(

        "MonthlyCharges",

        0

    )


    if monthly > 80:

        factors.append({

            "factor":
                "High Monthly Charges",

            "impact":
                "High",

            "reason":
                "High pricing may increase customer dissatisfaction."

        })


    # Support

    if customer.get("TechSupport") == "No":

        factors.append({

            "factor":
                "No Technical Support",

            "impact":
                "Medium",

            "reason":
                "Lack of support increases churn risk."

        })


    return factors



# ==========================================================
# RECOMMENDATION GENERATOR
# ==========================================================

def generate_recommendation(

        probability,

        factors

):


    if probability >= 0.85:

        priority = "Critical"

        action = [

            "Contact customer immediately",

            "Offer personalized retention discount",

            "Assign customer success manager"

        ]


    elif probability >= 0.70:


        priority = "High"


        action = [

            "Launch loyalty campaign",

            "Provide service upgrade",

            "Monitor customer activity"

        ]


    elif probability >= 0.40:


        priority = "Medium"


        action = [

            "Send engagement offers",

            "Improve communication"

        ]


    else:


        priority = "Low"


        action = [

            "Maintain normal relationship",

            "Continue monitoring"

        ]


    return {


        "priority":

            priority,


        "actions":

            action,


        "risk_factors":

            factors

    }



# ==========================================================
# EXECUTIVE SUMMARY
# ==========================================================

def executive_summary(

        customer,

        probability,

        factors

):


    risk = (

        "High Risk"

        if probability >= 0.7

        else

        "Moderate Risk"

        if probability >= 0.4

        else

        "Low Risk"

    )


    summary = f"""

Customer is classified as:

{risk}


The AI model estimates churn probability of:

{round(probability*100,2)}%


Main detected risk factors:

"""


    for factor in factors:

        summary += (

            f"- {factor['factor']} "

            f"({factor['impact']} Impact)\n"

        )


    return summary



# ==========================================================
# COMPLETE AI ANALYSIS
# ==========================================================

def generate_ai_analysis(

        customer,

        probability

):


    factors = analyze_risk_factors(

        customer

    )


    recommendation = generate_recommendation(

        probability,

        factors

    )


    summary = executive_summary(

        customer,

        probability,

        factors

    )


    return {


        "summary":

            summary,


        "recommendation":

            recommendation,


        "factors":

            factors

    }
