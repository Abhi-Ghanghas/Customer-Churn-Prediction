import streamlit as st
import pandas as pd
import joblib


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="ChurnPredict | Customer Retention",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# LOAD MODEL
# ============================================================

@st.cache_resource
def load_model():
    return joblib.load("Models/churn_model.pkl")


model = load_model()


# ============================================================
# GLOBAL CSS
# ============================================================

st.markdown("""
<style>

html, body, [class*="css"] {
    font-family: Inter, Segoe UI, Arial, sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 80% 5%, rgba(129,140,248,0.10), transparent 30%),
        radial-gradient(circle at 20% 10%, rgba(59,130,246,0.08), transparent 28%),
        linear-gradient(135deg,#f7f9ff 0%,#f5f8ff 45%,#fbfcff 100%);
    color:#15213a;
}

.block-container {
    max-width: 1500px;
    padding-top: 0.8rem;
    padding-bottom: 2rem;
}

#MainMenu {
    visibility:hidden;
}

footer {
    visibility:hidden;
}

header {
    background:transparent !important;
}


/* ============================================================
   SIDEBAR
   ============================================================ */

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg,#ffffff,#f8faff);
    border-right:1px solid #e6ebf5;
}

section[data-testid="stSidebar"] > div {
    padding-top:1rem;
}


/* ============================================================
   LIGHT SIDEBAR DROPDOWNS
   THIS IS THE IMPORTANT FIX
   ============================================================ */

section[data-testid="stSidebar"] div[data-baseweb="select"] > div {
    background-color: #ffffff !important;
    color: #1f2937 !important;

    border: 1px solid #dbe3ef !important;

    border-radius: 10px !important;

    box-shadow:
        0 2px 8px rgba(70,90,140,0.04) !important;
}


/* Selected Male / Female / Yes / No text */

section[data-testid="stSidebar"]
div[data-baseweb="select"] span {

    color: #1f2937 !important;
}


/* Dropdown arrow */

section[data-testid="stSidebar"]
div[data-baseweb="select"] svg {

    fill: #64748b !important;
    color: #64748b !important;
}


/* Dropdown popup */

div[data-baseweb="popover"] ul {

    background-color: #ffffff !important;

    border: 1px solid #e1e7f0 !important;

    border-radius: 10px !important;

    box-shadow:
        0 12px 28px rgba(50,70,120,0.14) !important;
}


/* Individual dropdown options */

div[data-baseweb="popover"] li {

    background-color: #ffffff !important;

    color: #1f2937 !important;
}


/* Dropdown hover */

div[data-baseweb="popover"] li:hover {

    background-color: #eef4ff !important;

    color: #2563eb !important;
}


/* ============================================================
   NUMBER INPUT
   ============================================================ */

div[data-testid="stNumberInput"] input {
    background:white !important;
    color:#1f2937 !important;
    border-radius:10px !important;
}


/* ============================================================
   BUTTON
   ============================================================ */

div.stButton > button {

    width:100%;

    border:none;

    border-radius:12px;

    padding:0.8rem 1rem;

    background:
        linear-gradient(
            90deg,
            #4f46e5,
            #2563eb
        );

    color:white;

    font-weight:800;

    box-shadow:
        0 10px 25px rgba(79,70,229,0.22);

    transition:all .2s ease;
}


div.stButton > button:hover {

    transform:translateY(-1px);

    box-shadow:
        0 14px 30px rgba(79,70,229,0.30);
}


/* ============================================================
   TOP BAR
   ============================================================ */

.topbar {

    display:flex;

    justify-content:space-between;

    align-items:center;

    background:rgba(255,255,255,.82);

    border:1px solid #e7ebf5;

    border-radius:18px;

    padding:14px 18px;

    margin-bottom:16px;

    box-shadow:
        0 6px 24px rgba(60,80,140,.05);
}


.brand {

    display:flex;

    align-items:center;

    gap:10px;
}


.brand-icon {

    width:38px;

    height:38px;

    border-radius:10px;

    background:
        linear-gradient(
            135deg,
            #2563eb,
            #7c3aed
        );

    display:flex;

    align-items:center;

    justify-content:center;

    color:white;

    font-size:20px;
}


.brand-title {

    font-size:22px;

    font-weight:900;

    color:#14213b;
}


.brand-title span {

    color:#5b5df0;
}


.brand-sub {

    font-size:12px;

    color:#8190a8;

    margin-top:1px;
}


.navwrap {

    display:flex;

    gap:12px;

    align-items:center;
}


.navitem {

    padding:8px 13px;

    border-radius:10px;

    color:#55627b;

    font-size:13px;

    font-weight:700;
}


.navitem.active {

    background:
        linear-gradient(
            90deg,
            #2563eb,
            #4f46e5
        );

    color:white;
}


.nav-cta {

    background:#eef2ff;

    color:#4f46e5;

    border:1px solid #d8ddff;

    border-radius:12px;

    padding:9px 14px;

    font-size:12px;

    font-weight:800;
}


/* ============================================================
   HERO
   ============================================================ */

.hero {

    background:
        radial-gradient(
            circle at 85% 25%,
            rgba(124,58,237,.18),
            transparent 28%
        ),

        radial-gradient(
            circle at 75% 85%,
            rgba(14,165,233,.14),
            transparent 25%
        ),

        linear-gradient(
            135deg,
            #ffffff,
            #eef6ff
        );

    border:1px solid #dfe8f6;

    border-radius:22px;

    padding:34px 38px;

    box-shadow:
        0 12px 35px rgba(65,85,150,.07);

    margin-bottom:16px;
}


.hero-badge {

    color:#6d5dfc;

    font-size:11px;

    letter-spacing:2.4px;

    font-weight:900;

    margin-bottom:10px;
}


.hero-title {

    font-size:52px;

    line-height:0.98;

    letter-spacing:-2px;

    font-weight:900;

    color:#111a30;

    margin:0;
}


.hero-title span {

    background:
        linear-gradient(
            90deg,
            #147df5,
            #635bff
        );

    -webkit-background-clip:text;

    -webkit-text-fill-color:transparent;
}


.hero-subtitle {

    font-size:16px;

    color:#536079;

    line-height:1.55;

    max-width:690px;

    margin-top:15px;
}


.feature-row {

    display:flex;

    gap:12px;

    margin-top:22px;

    flex-wrap:wrap;
}


.feature {

    background:rgba(255,255,255,.88);

    border:1px solid #e4e9f3;

    border-radius:13px;

    padding:10px 14px;

    font-size:12px;

    color:#43506a;

    box-shadow:
        0 4px 15px rgba(70,90,140,.04);
}


/* ============================================================
   PANELS
   ============================================================ */

.panel {

    background:rgba(255,255,255,.95);

    border:1px solid #e3e9f4;

    border-radius:18px;

    padding:20px;

    box-shadow:
        0 8px 30px rgba(70,90,150,.06);
}


.panel-title {

    font-size:20px;

    font-weight:900;

    color:#172033;

    margin-bottom:4px;
}


.panel-subtitle {

    font-size:12px;

    color:#8290a7;

    margin-bottom:14px;
}


/* ============================================================
   METRIC CARDS
   ============================================================ */

.metric-card {

    background:#ffffff;

    border:1px solid #e4e9f4;

    border-radius:16px;

    padding:18px;

    box-shadow:
        0 7px 22px rgba(70,90,150,.05);

    min-height:125px;
}


.metric-label {

    color:#7c89a0;

    font-size:11px;

    font-weight:800;

    letter-spacing:.4px;
}


.metric-value {

    margin-top:10px;

    color:#172033;

    font-size:27px;

    font-weight:900;
}


.pred-card-red {

    background:
        linear-gradient(
            135deg,
            #fff7f7,
            #fff0f2
        );

    border:1px solid #ffccd2;
}


.pred-card-yellow {

    background:
        linear-gradient(
            135deg,
            #fffdf5,
            #fff7e5
        );

    border:1px solid #ffe0a0;
}


.pred-card-green {

    background:
        linear-gradient(
            135deg,
            #f2fffa,
            #eafcf6
        );

    border:1px solid #c8eedf;
}


.red-text {

    color:#ef4c5a;
}


.yellow-text {

    color:#f4a000;
}


.green-text {

    color:#10b981;
}


/* ============================================================
   RISK BAR
   ============================================================ */

.riskbox {

    background:#ffffff;

    border:1px solid #e4e9f3;

    border-radius:16px;

    padding:18px 20px;

    margin-top:14px;
}


.riskhead {

    display:flex;

    justify-content:space-between;

    font-weight:900;

    color:#243149;

    margin-bottom:10px;
}


.riskbg {

    height:14px;

    border-radius:999px;

    background:#edf1f7;

    overflow:hidden;
}


.riskfill {

    height:100%;

    border-radius:999px;

    background:
        linear-gradient(
            90deg,
            #2ecf95,
            #facc15,
            #fb923c,
            #ef476f
        );
}


/* ============================================================
   ALERTS
   ============================================================ */

.alert-red {

    background:
        linear-gradient(
            135deg,
            #fff6f7,
            #fff0f2
        );

    border:1px solid #ffc5cd;

    border-radius:14px;

    padding:16px 18px;

    color:#c93f4b;

    margin-top:14px;
}


.alert-green {

    background:
        linear-gradient(
            135deg,
            #f1fff8,
            #ebfff6
        );

    border:1px solid #bdebd6;

    border-radius:14px;

    padding:16px 18px;

    color:#087a57;

    margin-top:14px;
}


/* ============================================================
   STRATEGY
   ============================================================ */

.strategy-box {

    background:
        linear-gradient(
            135deg,
            #fffdf4,
            #fff8e7
        );

    border:1px solid #ffe2a7;

    border-radius:16px;

    padding:20px;

    min-height:250px;
}


.risk-factor-box {

    background:
        linear-gradient(
            135deg,
            #f6fbff,
            #eef6ff
        );

    border:1px solid #cfe3ff;

    border-radius:16px;

    padding:20px;

    min-height:250px;
}


.strategy-item,
.risk-item {

    margin:9px 0;

    color:#394660;

    font-size:13px;
}


/* ============================================================
   MODEL
   ============================================================ */

.model-box {

    background:
        linear-gradient(
            135deg,
            #f7f5ff,
            #f2f4ff
        );

    border:1px solid #dfdafc;

    border-radius:16px;

    padding:20px;
}


.model-row {

    display:flex;

    justify-content:space-between;

    gap:16px;

    padding:10px 0;

    border-bottom:1px solid #e8e8f5;

    font-size:13px;

    color:#62708a;
}


.model-row:last-child {

    border-bottom:none;
}


.model-row strong {

    color:#1f2b44;
}


/* ============================================================
   MISSION
   ============================================================ */

.mission-box {

    background:
        linear-gradient(
            135deg,
            #effff9,
            #f3fff8
        );

    border:1px solid #ccefe1;

    border-radius:16px;

    padding:20px;

    margin-top:14px;
}


.mission-quote {

    color:#385469;

    font-style:italic;

    line-height:1.5;

    font-size:14px;
}


.section-title {

    font-size:23px;

    color:#172033;

    font-weight:900;

    margin:10px 0 13px 0;
}


/* ============================================================
   FOOTER
   ============================================================ */

.footer {

    margin-top:24px;

    background:rgba(255,255,255,.8);

    border:1px solid #e8edf5;

    border-radius:14px;

    padding:16px;

    text-align:center;

    color:#8490a5;

    font-size:12px;
}


@media(max-width:900px) {

    .hero-title {
        font-size:38px;
    }

    .topbar {
        display:block;
    }

    .navwrap {
        margin-top:10px;
        flex-wrap:wrap;
    }
}
/* ============================================================
   FORCE LIGHT SIDEBAR SELECT BOXES
   ============================================================ */

section[data-testid="stSidebar"] [data-testid="stSelectbox"] div[data-baseweb="select"] > div {
    background: #ffffff !important;
    background-color: #ffffff !important;
    border: 1px solid #d8e0ec !important;
    border-radius: 10px !important;
    color: #1f2937 !important;
    box-shadow: 0 2px 8px rgba(30, 60, 100, 0.05) !important;
}


/* Male / Female / Yes / No text */

section[data-testid="stSidebar"] [data-testid="stSelectbox"] div[data-baseweb="select"] * {
    color: #1f2937 !important;
}


/* Arrow */

section[data-testid="stSidebar"] [data-testid="stSelectbox"] svg {
    fill: #64748b !important;
    color: #64748b !important;
}


/* Dropdown list container */

div[data-baseweb="popover"] {
    background: #ffffff !important;
}


div[data-baseweb="popover"] > div {
    background: #ffffff !important;
}


/* Actual dropdown menu */

div[data-baseweb="menu"] {
    background: #ffffff !important;
    border: 1px solid #dfe6ef !important;
    border-radius: 10px !important;
}


/* Options */

div[data-baseweb="menu"] li,
div[data-baseweb="menu"] [role="option"] {
    background: #ffffff !important;
    color: #1f2937 !important;
}


/* Hovered option */

div[data-baseweb="menu"] li:hover,
div[data-baseweb="menu"] [role="option"]:hover {
    background: #eef4ff !important;
    color: #2563eb !important;
}


/* Selected option */

div[data-baseweb="menu"] [aria-selected="true"] {
    background: #eef2ff !important;
    color: #4f46e5 !important;
}
</style>
""", unsafe_allow_html=True)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        '<div class="brand" style="margin-bottom:8px;"><div class="brand-icon">📊</div><div><div class="brand-title">Churn<span>Predict</span></div><div class="brand-sub">Customer Retention Intelligence</div></div></div>',
        unsafe_allow_html=True
    )

    st.markdown("### 👤 Customer Information")

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    senior_citizen = st.selectbox(
        "Senior Citizen",
        ["No", "Yes"]
    )

    partner = st.selectbox(
        "Partner",
        ["Yes", "No"]
    )

    dependents = st.selectbox(
        "Dependents",
        ["Yes", "No"]
    )

    tenure = st.slider(
        "Tenure (Months)",
        0,
        72,
        3
    )

    phone_service = st.selectbox(
        "Phone Service",
        ["Yes", "No"]
    )

    multiple_lines = st.selectbox(
        "Multiple Lines",
        [
            "No",
            "Yes",
            "No phone service"
        ]
    )

    internet_service = st.selectbox(
        "Internet Service",
        [
            "DSL",
            "Fiber optic",
            "No"
        ]
    )

    online_security = st.selectbox(
        "Online Security",
        [
            "Yes",
            "No",
            "No internet service"
        ]
    )

    online_backup = st.selectbox(
        "Online Backup",
        [
            "Yes",
            "No",
            "No internet service"
        ]
    )

    device_protection = st.selectbox(
        "Device Protection",
        [
            "Yes",
            "No",
            "No internet service"
        ]
    )

    tech_support = st.selectbox(
        "Tech Support",
        [
            "Yes",
            "No",
            "No internet service"
        ]
    )

    streaming_tv = st.selectbox(
        "Streaming TV",
        [
            "Yes",
            "No",
            "No internet service"
        ]
    )

    streaming_movies = st.selectbox(
        "Streaming Movies",
        [
            "Yes",
            "No",
            "No internet service"
        ]
    )

    contract = st.selectbox(
        "Contract Type",
        [
            "Month-to-month",
            "One year",
            "Two year"
        ]
    )

    paperless_billing = st.selectbox(
        "Paperless Billing",
        ["Yes", "No"]
    )

    payment_method = st.selectbox(
        "Payment Method",
        [
            "Electronic check",
            "Mailed check",
            "Bank transfer (automatic)",
            "Credit card (automatic)"
        ]
    )

    monthly_charges = st.number_input(
        "Monthly Charges ($)",
        min_value=0.0,
        max_value=200.0,
        value=95.0
    )

    total_charges = st.number_input(
        "Total Charges ($)",
        min_value=0.0,
        max_value=10000.0,
        value=285.0
    )


# ============================================================
# TOP BAR
# ============================================================

st.markdown(
    '<div class="topbar"><div class="brand"><div class="brand-icon">📊</div><div><div class="brand-title">Churn<span>Predict</span></div><div class="brand-sub">Happy Customers. Stronger Business.</div></div></div><div class="navwrap"><div class="navitem active">🏠 Home</div><div class="navitem">📊 Insights</div><div class="navitem">⚙️ How It Works</div><div class="navitem">ⓘ About</div><div class="nav-cta">Turn Data Into Loyal Customers</div></div></div>',
    unsafe_allow_html=True
)


# ============================================================
# CUSTOMER DATA
# ============================================================

senior_value = 1 if senior_citizen == "Yes" else 0


customer_data = pd.DataFrame({

    "gender": [gender],

    "SeniorCitizen": [senior_value],

    "Partner": [partner],

    "Dependents": [dependents],

    "tenure": [tenure],

    "PhoneService": [phone_service],

    "MultipleLines": [multiple_lines],

    "InternetService": [internet_service],

    "OnlineSecurity": [online_security],

    "OnlineBackup": [online_backup],

    "DeviceProtection": [device_protection],

    "TechSupport": [tech_support],

    "StreamingTV": [streaming_tv],

    "StreamingMovies": [streaming_movies],

    "Contract": [contract],

    "PaperlessBilling": [paperless_billing],

    "PaymentMethod": [payment_method],

    "MonthlyCharges": [monthly_charges],

    "TotalCharges": [total_charges]

})


# ============================================================
# MAIN LAYOUT
# ============================================================

main_col, right_col = st.columns(
    [3.1, 1.05],
    gap="medium"
)


# ============================================================
# MAIN COLUMN
# ============================================================

with main_col:

    # HERO

    st.markdown(
        '<div class="hero"><div class="hero-badge">AI POWERED ANALYTICS</div><div class="hero-title">Customer Churn<br><span>Prediction</span></div><div class="hero-subtitle">Understand your customers. Predict churn. Take action.<br>Use machine learning to identify at-risk customers and build stronger, longer-lasting relationships.</div><div class="feature-row"><div class="feature">⚡ <b>Accurate Predictions</b><br>ML Powered</div><div class="feature">📊 <b>Business Insights</b><br>Data Driven</div><div class="feature">💎 <b>Increase Retention</b><br>Higher Revenue</div></div></div>',
        unsafe_allow_html=True
    )


    # PREDICT BUTTON

    predict = st.button(
        "✨ Predict Customer Churn",
        type="primary"
    )


    if predict:

        prediction = model.predict(
            customer_data
        )[0]

        probability = model.predict_proba(
            customer_data
        )[0][1]

        churn_percent = probability * 100


        # RISK LEVEL

        if churn_percent >= 70:

            risk_level = "HIGH"
            risk_color = "#ef4444"

        elif churn_percent >= 40:

            risk_level = "MEDIUM"
            risk_color = "#f59e0b"

        else:

            risk_level = "LOW"
            risk_color = "#10b981"


        prediction_text = (
            "Likely to Churn"
            if prediction == 1
            else "Likely to Stay"
        )


        pred_class = (
            "red-text"
            if prediction == 1
            else "green-text"
        )


        # PREDICTION RESULTS

        st.markdown(
            '<div class="section-title">📊 Prediction Results</div>',
            unsafe_allow_html=True
        )


        p1, p2, p3 = st.columns(3)


        with p1:

            st.markdown(
                f'<div class="metric-card pred-card-red"><div class="metric-label">🎯 CHURN PROBABILITY</div><div class="metric-value red-text">{churn_percent:.2f}%</div></div>',
                unsafe_allow_html=True
            )


        with p2:

            st.markdown(
                f'<div class="metric-card pred-card-yellow"><div class="metric-label">⚠️ RISK LEVEL</div><div class="metric-value" style="color:{risk_color};">{risk_level}</div></div>',
                unsafe_allow_html=True
            )


        with p3:

            st.markdown(
                f'<div class="metric-card pred-card-green"><div class="metric-label">👤 PREDICTION</div><div class="metric-value {pred_class}" style="font-size:23px;">{prediction_text}</div></div>',
                unsafe_allow_html=True
            )


        # RISK SCORE

        st.markdown(
            f'<div class="riskbox"><div class="riskhead"><span>Churn Risk Score</span><span>{churn_percent:.2f}%</span></div><div class="riskbg"><div class="riskfill" style="width:{churn_percent}%"></div></div></div>',
            unsafe_allow_html=True
        )


        # ALERT

        if prediction == 1:

            st.markdown(
                f'<div class="alert-red"><b>⚠️ This customer is likely to churn.</b><br><br>Based on the provided information, the model estimates a <b>{churn_percent:.2f}%</b> probability of churn for this customer.</div>',
                unsafe_allow_html=True
            )

        else:

            st.markdown(
                f'<div class="alert-green"><b>✅ This customer is likely to stay.</b><br><br>The estimated churn probability is <b>{churn_percent:.2f}%</b>.</div>',
                unsafe_allow_html=True
            )


        # ====================================================
        # RISK FACTORS
        # ====================================================

        risk_factors = []


        if contract == "Month-to-month":

            risk_factors.append(
                "📋 Month-to-month contract"
            )


        if tenure < 12:

            risk_factors.append(
                "⏱️ Low customer tenure"
            )


        if internet_service == "Fiber optic":

            risk_factors.append(
                "🌐 Fiber optic service"
            )


        if tech_support == "No":

            risk_factors.append(
                "🛡️ No technical support"
            )


        if online_security == "No":

            risk_factors.append(
                "🔐 No online security service"
            )


        if payment_method == "Electronic check":

            risk_factors.append(
                "💳 Electronic check payment method"
            )


        if monthly_charges > 80:

            risk_factors.append(
                "💵 High monthly charges"
            )


        # ====================================================
        # RETENTION STRATEGY
        # ====================================================

        b1, b2 = st.columns(
            [1.25, 1]
        )


        with b1:

            if risk_level == "HIGH":

                actions = [

                    "Provide an immediate personalized retention offer",

                    "Offer a discount for switching to an annual contract",

                    "Assign priority customer support",

                    "Review service quality issues"

                ]


            elif risk_level == "MEDIUM":

                actions = [

                    "Send targeted loyalty offers",

                    "Recommend annual contract benefits",

                    "Monitor support interactions",

                    "Offer personalized service upgrades"

                ]


            else:

                actions = [

                    "Maintain current service quality",

                    "Continue loyalty rewards",

                    "Recommend relevant service upgrades"

                ]


            action_html = "".join(

                f'<div class="strategy-item">✅ {a}</div>'

                for a in actions
            )


            st.markdown(
                f'<div class="strategy-box"><div class="panel-title">💡 Recommended Retention Strategy</div><div class="panel-subtitle">Recommended actions based on the customer&apos;s current churn risk.</div>{action_html}</div>',
                unsafe_allow_html=True
            )


        with b2:

            if risk_factors:

                factor_html = "".join(

                    f'<div class="risk-item">{r}</div>'

                    for r in risk_factors
                )

            else:

                factor_html = (
                    '<div class="risk-item">'
                    '✅ No major common churn factors detected.'
                    '</div>'
                )


            st.markdown(
                f'<div class="risk-factor-box"><div class="panel-title">🚨 Possible Risk Factors</div><div class="panel-subtitle">Customer characteristics associated with churn risk.</div>{factor_html}</div>',
                unsafe_allow_html=True
            )


    else:

        st.markdown(
            '<div class="panel"><div class="panel-title">📊 Prediction Results</div><div class="panel-subtitle">Enter customer details on the left and click <b>Predict Customer Churn</b> to generate a churn probability, risk level, and recommended retention strategy.</div></div>',
            unsafe_allow_html=True
        )


# ============================================================
# RIGHT COLUMN
# ============================================================

with right_col:

    st.markdown(
        '<div class="panel"><div class="panel-title">👤 Customer Overview</div><div class="panel-subtitle">Key information at a glance</div></div>',
        unsafe_allow_html=True
    )


    st.markdown(
        f'<div class="metric-card"><div class="metric-label">📅 TENURE</div><div class="metric-value">{tenure} months</div></div>',
        unsafe_allow_html=True
    )


    st.write("")


    st.markdown(
        f'<div class="metric-card"><div class="metric-label">💵 MONTHLY CHARGES</div><div class="metric-value">${monthly_charges:.2f}</div></div>',
        unsafe_allow_html=True
    )


    st.write("")


    st.markdown(
        f'<div class="metric-card"><div class="metric-label">💳 TOTAL CHARGES</div><div class="metric-value">${total_charges:.2f}</div></div>',
        unsafe_allow_html=True
    )


    st.write("")


    st.markdown(
        f'<div class="metric-card"><div class="metric-label">📋 CONTRACT TYPE</div><div class="metric-value" style="font-size:20px;">{contract}</div></div>',
        unsafe_allow_html=True
    )


    st.write("")


    # MODEL INFORMATION

    st.markdown(
        '<div class="model-box"><div class="panel-title">⚙️ About the Model</div><div class="model-row"><span>Final Model</span><strong>Logistic Regression</strong></div><div class="model-row"><span>ROC-AUC</span><strong>0.8359</strong></div><div class="model-row"><span>Compared</span><strong>LR · RF · XGBoost</strong></div><div class="model-row"><span>Explainability</span><strong>SHAP</strong></div></div>',
        unsafe_allow_html=True
    )


    # MISSION

    st.markdown(
        '<div class="mission-box"><div class="panel-title">🌿 Our Mission</div><div class="mission-quote">“Turn data into loyal customers and build stronger businesses.”</div></div>',
        unsafe_allow_html=True
    )


# ============================================================
# CUSTOMER INFORMATION
# ============================================================

with st.expander(
    "🔎 View complete customer information"
):

    st.dataframe(
        customer_data,
        use_container_width=True,
        hide_index=True
    )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    '<div class="footer"><b>📊 ChurnPredict</b> &nbsp;•&nbsp; Customer Churn Prediction & Retention Analytics &nbsp;•&nbsp; Built with Python & Streamlit &nbsp;•&nbsp; Machine Learning · Data Analytics · Predictive Intelligence</div>',
    unsafe_allow_html=True
)
