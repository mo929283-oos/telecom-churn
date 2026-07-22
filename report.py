"""
===========================================================
TelcoGuard AI
Report Generator
===========================================================
"""

from datetime import datetime

from pathlib import Path

from config import REPORT_DIR, PROJECT_NAME



# ==========================================================
# HTML STYLE
# ==========================================================

REPORT_STYLE = """

<style>

body{

font-family:Arial, sans-serif;

background:#0f172a;

color:white;

padding:40px;

}


.container{

background:#1e293b;

padding:30px;

border-radius:20px;

}


.title{

font-size:35px;

font-weight:bold;

color:#4f8bf9;

}


.card{

background:#334155;

padding:20px;

border-radius:15px;

margin:15px 0;

}


.risk{

font-size:25px;

font-weight:bold;

}


table{

width:100%;

border-collapse:collapse;

}


td,th{

padding:12px;

border-bottom:1px solid #475569;

}


</style>

"""



# ==========================================================
# CREATE REPORT
# ==========================================================

def create_report(

        customer,

        prediction,

        ai_analysis,

        financial

):


    timestamp = datetime.now().strftime(

        "%Y-%m-%d %H:%M"

    )


    risk_color = (

        "#22c55e"

        if prediction["risk"]=="Low"

        else

        "#f59e0b"

        if prediction["risk"]=="Medium"

        else

        "#ef4444"

    )



    html = f"""

<html>

<head>

{REPORT_STYLE}

</head>


<body>


<div class="container">


<div class="title">

🚀 {PROJECT_NAME}

</div>


<p>

Generated:

{timestamp}

</p>



<div class="card">


<h2>

Customer Prediction

</h2>


<table>


<tr>

<td>Status</td>

<td>

{prediction['status']}

</td>

</tr>



<tr>

<td>

Churn Probability

</td>


<td>

{prediction['probability_percent']}%

</td>

</tr>



<tr>

<td>

Confidence

</td>


<td>

{prediction['confidence']}%

</td>

</tr>



<tr>

<td>

Risk

</td>


<td style="color:{risk_color}">

{prediction['risk']}

</td>


</tr>


</table>


</div>





<div class="card">


<h2>

🤖 AI Recommendation

</h2>


<p>

{ai_analysis['summary']}

</p>


</div>





<div class="card">


<h2>

💰 Financial Impact

</h2>


<table>


<tr>

<td>

Expected Loss

</td>


<td>

${financial['expected_loss']}

</td>


</tr>



<tr>

<td>

Saving Opportunity

</td>


<td>

${financial['saving_opportunity']}

</td>


</tr>



<tr>

<td>

Retention ROI

</td>


<td>

{financial['retention_roi']}%

</td>


</tr>


</table>


</div>




<div class="card">


<h2>

Risk Factors

</h2>


<ul>

"""


    for factor in ai_analysis["factors"]:


        html += f"""

<li>

<b>

{factor['factor']}

</b>

-

{factor['reason']}

</li>

"""


    html += """

</ul>


</div>



</div>


</body>


</html>

"""



    file_path = (

        Path(REPORT_DIR)

        /

        "TelcoGuard_Report.html"

    )


    with open(

        file_path,

        "w",

        encoding="utf-8"

    ) as file:


        file.write(html)



    return file_path
