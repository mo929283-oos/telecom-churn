"""
===========================================================
TelcoGuard AI
Scenario Simulator Engine
===========================================================
"""


from predictor import predict_customer



# ==========================================================
# APPLY CUSTOMER CHANGES
# ==========================================================

def apply_changes(

        customer,

        changes

):

    updated_customer = customer.copy()


    for key, value in changes.items():

        updated_customer[key] = value


    return updated_customer



# ==========================================================
# RUN SCENARIO
# ==========================================================

def run_scenario(

        original_customer,

        changes,

        model,

        scaler,

        columns

):


    modified_customer = apply_changes(

        original_customer,

        changes

    )


    result = predict_customer(

        modified_customer,

        model,

        scaler,

        columns

    )


    return {


        "customer":

            modified_customer,


        "result":

            result

    }



# ==========================================================
# COMPARE RESULTS
# ==========================================================

def compare_results(

        original_result,

        scenario_result

):


    old_probability = (

        original_result["probability"]

    )


    new_probability = (

        scenario_result["probability"]

    )


    improvement = (

        old_probability

        -

        new_probability

    )


    improvement_percent = (

        improvement * 100

    )


    if improvement > 0:

        status = "Improved"

        message = (

            "Scenario reduced churn probability."

        )


    elif improvement < 0:

        status = "Worse"

        message = (

            "Scenario increased churn probability."

        )


    else:

        status = "No Change"

        message = (

            "Scenario did not affect prediction."

        )


    return {


        "old_probability":

            round(old_probability*100,2),


        "new_probability":

            round(new_probability*100,2),


        "improvement":

            round(improvement_percent,2),


        "status":

            status,


        "message":

            message

    }



# ==========================================================
# RETENTION SCENARIOS
# ==========================================================

def recommended_scenarios(customer):


    scenarios = []


    # Contract Upgrade

    if customer.get("Contract") == "Month-to-month":


        scenarios.append({

            "name":

                "Upgrade Contract",


            "changes":

                {

                "Contract":

                    "One year"

                }

        })



    # Lower Price Scenario

    if customer.get("MonthlyCharges",0) > 70:


        scenarios.append({

            "name":

                "Discount Offer",


            "changes":

                {

                "MonthlyCharges":

                    customer["MonthlyCharges"]*0.85

                }

        })



    # Support Scenario

    if customer.get("TechSupport") == "No":


        scenarios.append({

            "name":

                "Add Technical Support",


            "changes":

                {

                "TechSupport":

                    "Yes"

                }

        })


    return scenarios



# ==========================================================
# RUN ALL SCENARIOS
# ==========================================================

def evaluate_scenarios(

        customer,

        model,

        scaler,

        columns

):


    scenarios = recommended_scenarios(

        customer

    )


    results = []


    for scenario in scenarios:


        output = run_scenario(

            customer,

            scenario["changes"],

            model,

            scaler,

            columns

        )


        results.append({

            "scenario":

                scenario["name"],


            "result":

                output["result"]

        })


    return results
