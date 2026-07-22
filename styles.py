import streamlit as st


def load_css():

    st.markdown("""

<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');

html,
body,
[class*="css"]{
    font-family:'Poppins',sans-serif;
}


/*=========================================================
MAIN
=========================================================*/

.stApp{

background:
linear-gradient(
135deg,
#07111f 0%,
#0f172a 30%,
#172554 100%
);

color:white;

}


/*=========================================================
HEADER
=========================================================*/

header{

visibility:hidden;

}

footer{

visibility:hidden;

}

#MainMenu{

visibility:hidden;

}


/*=========================================================
SIDEBAR
=========================================================*/

section[data-testid="stSidebar"]{

background:

linear-gradient(

180deg,

rgba(20,30,48,.95),

rgba(36,59,85,.96)

);

border-right:1px solid rgba(255,255,255,.08);

backdrop-filter:blur(20px);

}


/*=========================================================
HERO
=========================================================*/

.hero{

padding:45px;

border-radius:25px;

background:

linear-gradient(

135deg,

rgba(79,139,249,.22),

rgba(30,41,59,.92)

);

border:1px solid rgba(255,255,255,.10);

backdrop-filter:blur(16px);

box-shadow:

0 25px 60px rgba(0,0,0,.45);

margin-bottom:30px;

}


.hero h1{

font-size:52px;

font-weight:800;

color:white;

margin-bottom:10px;

}


.hero p{

font-size:18px;

color:#d8e3ff;

}


/*=========================================================
GLASS CARD
=========================================================*/

.glass{

background:

rgba(255,255,255,.05);

border-radius:22px;

padding:22px;

backdrop-filter:blur(18px);

border:

1px solid rgba(255,255,255,.08);

box-shadow:

0 15px 35px rgba(0,0,0,.35);

transition:.35s;

}

.glass:hover{

transform:translateY(-6px);

box-shadow:

0 25px 45px rgba(0,0,0,.45);

}


/*=========================================================
METRIC CARD
=========================================================*/

.metric-card{

background:

linear-gradient(

135deg,

rgba(79,139,249,.18),

rgba(255,255,255,.04)

);

padding:20px;

border-radius:18px;

border:1px solid rgba(255,255,255,.08);

text-align:center;

transition:.35s;

}

.metric-card:hover{

transform:scale(1.04);

}

.metric-title{

font-size:15px;

color:#CBD5E1;

}

.metric-value{

font-size:34px;

font-weight:700;

color:white;

}


/*=========================================================
BUTTON
=========================================================*/

.stButton>button{

width:100%;

height:55px;

border-radius:15px;

border:none;

font-weight:700;

font-size:16px;

background:

linear-gradient(

90deg,

#4F8BF9,

#2563EB

);

color:white;

transition:.3s;

}

.stButton>button:hover{

transform:translateY(-3px);

box-shadow:

0 15px 30px rgba(79,139,249,.35);

}


/*=========================================================
INPUTS
=========================================================*/

.stSelectbox,

.stNumberInput,

.stSlider,

.stTextInput{

background:transparent;

}

div[data-baseweb="select"]>div{

background:rgba(255,255,255,.05);

border-radius:12px;

border:1px solid rgba(255,255,255,.08);

}

input{

background:rgba(255,255,255,.05)!important;

color:white!important;

}


/*=========================================================
CUSTOM TITLE
=========================================================*/

.title{

font-size:32px;

font-weight:700;

margin-bottom:10px;

}

.subtitle{

font-size:18px;

color:#94A3B8;

}


/*=========================================================
FOOTER
=========================================================*/

.footer{

text-align:center;

padding:20px;

color:#94A3B8;

font-size:14px;

}


/*=========================================================
SCROLLBAR
=========================================================*/

::-webkit-scrollbar{

width:10px;

}

::-webkit-scrollbar-track{

background:#0f172a;

}

::-webkit-scrollbar-thumb{

background:#2563EB;

border-radius:20px;

}


/*=========================================================
DIVIDER
=========================================================*/

hr{

border:none;

height:1px;

background:

rgba(255,255,255,.08);

margin-top:25px;

margin-bottom:25px;

}

/*=========================================================
TABS
=========================================================*/

.stTabs [data-baseweb="tab-list"]{

gap:12px;

background:rgba(255,255,255,.03);

padding:10px;

border-radius:16px;

}

.stTabs [data-baseweb="tab"]{

height:55px;

padding-left:22px;

padding-right:22px;

background:rgba(255,255,255,.04);

border-radius:12px;

color:white;

font-weight:600;

transition:.3s;

}

.stTabs [aria-selected="true"]{

background:

linear-gradient(
90deg,
#2563EB,
#4F8BF9
);

}


/*=========================================================
EXPANDER
=========================================================*/

.streamlit-expanderHeader{

font-size:17px;

font-weight:600;

color:white;

background:rgba(255,255,255,.04);

border-radius:12px;

}


/*=========================================================
TABLES
=========================================================*/

thead tr th{

background:#1E3A8A!important;

color:white!important;

font-size:15px;

}

tbody{

background:rgba(255,255,255,.03);

}


/*=========================================================
DATAFRAME
=========================================================*/

[data-testid="stDataFrame"]{

border-radius:18px;

overflow:hidden;

border:1px solid rgba(255,255,255,.08);

}


/*=========================================================
GAUGE CARD
=========================================================*/

.gauge-card{

padding:25px;

border-radius:20px;

background:

linear-gradient(
135deg,
rgba(37,99,235,.15),
rgba(255,255,255,.04)
);

border:1px solid rgba(255,255,255,.08);

}


/*=========================================================
RISK BADGE
=========================================================*/

.badge-low{

padding:8px 18px;

border-radius:25px;

background:#16A34A;

color:white;

font-weight:600;

display:inline-block;

}

.badge-medium{

padding:8px 18px;

border-radius:25px;

background:#F59E0B;

color:white;

font-weight:600;

display:inline-block;

}

.badge-high{

padding:8px 18px;

border-radius:25px;

background:#DC2626;

color:white;

font-weight:600;

display:inline-block;

}


/*=========================================================
AI CARD
=========================================================*/

.ai-card{

background:

linear-gradient(
135deg,
rgba(59,130,246,.12),
rgba(255,255,255,.04)
);

padding:28px;

border-radius:20px;

border-left:6px solid #3B82F6;

box-shadow:0 10px 25px rgba(0,0,0,.30);

}


/*=========================================================
TIMELINE
=========================================================*/

.timeline{

border-left:3px solid #3B82F6;

margin-left:18px;

padding-left:22px;

}

.timeline-item{

margin-bottom:24px;

position:relative;

}

.timeline-item::before{

content:"";

position:absolute;

left:-31px;

top:4px;

width:14px;

height:14px;

border-radius:50%;

background:#4F8BF9;

}


/*=========================================================
DOWNLOAD BUTTON
=========================================================*/

.download-btn{

display:inline-block;

padding:14px 26px;

border-radius:12px;

background:

linear-gradient(
90deg,
#2563EB,
#3B82F6
);

color:white;

font-weight:700;

text-decoration:none;

transition:.3s;

}

.download-btn:hover{

transform:translateY(-4px);

}


/*=========================================================
PROBABILITY CARD
=========================================================*/

.probability-card{

padding:24px;

border-radius:20px;

background:

linear-gradient(
135deg,
rgba(99,102,241,.15),
rgba(255,255,255,.05)
);

text-align:center;

}

.probability-value{

font-size:54px;

font-weight:800;

color:white;

}


/*=========================================================
CHART CONTAINER
=========================================================*/

.chart-card{

padding:20px;

background:rgba(255,255,255,.04);

border-radius:20px;

border:1px solid rgba(255,255,255,.08);

box-shadow:0 10px 25px rgba(0,0,0,.25);

}

</style>

""", unsafe_allow_html=True)
