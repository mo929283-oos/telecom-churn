"""
===========================================================
TelcoGuard AI
Financial Intelligence Engine
===========================================================
"""


from config import (
    DEFAULT_CUSTOMER_VALUE,
    DEFAULT_RETENTION_COST,
    DEFAULT_PROFIT_MARGIN
)



# ==========================================================
# CUSTOMER LIFETIME VALUE
# ==========================================================

def calculate_clv(

        monthly_charge,

        months=24

):

    """
    Estimate Customer Lifetime Value
    """

    value = (

        monthly_charge

        *

        months

    )


    return round(value,2)



# ==========================================================
# CHURN LOSS
# ==========================================================

def calculate_churn_loss(

        probability,

        monthly_charge

):

    """

    Expected revenue loss

    """

    yearly_value = (

        monthly_charge

        *

        12

    )


    loss = (

        probability

        *

        yearly_value

    )


    return round(loss,2)



# ==========================================================
# RETENTION COST
# ==========================================================

def retention_cost(

        customers=1

):


    return (

        DEFAULT_RETENTION_COST

        *

        customers

    )



# ==========================================================
# SAVING OPPORTUNITY
# ==========================================================

def saving_opportunity(

        probability,

        monthly_charge

):


    loss = calculate_churn_loss(

        probability,

        monthly_charge

    )


    opportunity = loss * 0.75


    return round(opportunity,2)



# ==========================================================
# ROI CALCULATION
# ==========================================================

def calculate_roi(

        saved_value,

        campaign_cost

):


    if campaign_cost == 0:

        return 0


    roi = (

        (saved_value - campaign_cost)

        /

        campaign_cost

    ) * 100


    return round(roi,2)



# ==========================================================
# PROFIT IMPACT
# ==========================================================

def profit_impact(

        revenue

):


    profit = (

        revenue

        *

        DEFAULT_PROFIT_MARGIN

    )


    return round(profit,2)



# ==========================================================
# COMPLETE FINANCIAL REPORT
# ==========================================================

def financial_report(

        probability,

        monthly_charge

):


    clv = calculate_clv(

        monthly_charge

    )


    loss = calculate_churn_loss(

        probability,

        monthly_charge

    )


    saving = saving_opportunity(

        probability,

        monthly_charge

    )


    roi = calculate_roi(

        saving,

        DEFAULT_RETENTION_COST

    )


    return {


        "customer_lifetime_value":

            clv,


        "expected_loss":

            loss,


        "saving_opportunity":

            saving,


        "retention_roi":

            roi,


        "profit_impact":

            profit_impact(loss)

    }
