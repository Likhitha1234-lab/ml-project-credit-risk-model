import streamlit as st
from prediction_helper import predict

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Lauki Finance · Credit Risk",
    page_icon="📊",
    layout="centered",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
/* ── Google Font ── */
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600&family=DM+Mono&display=swap');

/* ── Root palette (no blues) ── */
:root {
    --bg:        #F7F5F0;
    --surface:   #FFFFFF;
    --border:    #E2DDD6;
    --accent:    #C0392B;      /* deep crimson – risk / finance feel  */
    --accent2:   #2C7A4B;      /* forest green – "safe" rating colour */
    --text-hd:   #1A1A1A;
    --text-body: #3D3D3D;
    --text-mute: #7A7268;
    --shadow:    0 2px 12px rgba(0,0,0,0.07);
}

/* ── Base ── */
html, body, [data-testid="stAppViewContainer"] {
    background-color: var(--bg) !important;
    font-family: 'DM Sans', sans-serif;
    color: var(--text-body);
}
[data-testid="stHeader"] { background: transparent !important; }

/* ── Hide default Streamlit chrome ── */
#MainMenu, footer { visibility: hidden; }

/* ── Page wrapper ── */
.block-container {
    max-width: 860px !important;
    padding: 2rem 2rem 4rem !important;
}

/* ── Header banner ── */
.lf-header {
    background: var(--surface);
    border: 1px solid var(--border);
    border-left: 5px solid var(--accent);
    border-radius: 10px;
    padding: 1.6rem 1.8rem 1.3rem;
    margin-bottom: 1.8rem;
    box-shadow: var(--shadow);
}
.lf-header h1 {
    font-size: 2rem;
    font-weight: 700;
    margin: 0 0 .3rem;
    letter-spacing: -.4px;
    line-height: 1.15;
}
.lf-header h1 .brand {
    color: #C0392B;          /* crimson — brand identity */
}
.lf-header h1 .colon {
    color: #7A7268;          /* muted separator */
    font-weight: 400;
}
.lf-header h1 .subtitle-text {
    color: #1A5C52;          /* deep teal — distinct, no blue */
}
.lf-header p {
    font-size: .875rem;
    color: var(--text-mute);
    margin: 0;
}

/* ── Section cards ── */
.lf-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 1.2rem 1.4rem 1rem;
    margin-bottom: 1.1rem;
    box-shadow: var(--shadow);
}
.lf-card-title {
    font-size: .72rem;
    font-weight: 600;
    letter-spacing: .08em;
    text-transform: uppercase;
    color: var(--accent);
    margin-bottom: .9rem;
    padding-bottom: .45rem;
    border-bottom: 1px solid var(--border);
}

/* ── Loan-to-Income badge ── */
.lti-box {
    background: #FDF6F5;
    border: 1px solid #EACBC8;
    border-radius: 8px;
    padding: .6rem .9rem;
    display: flex;
    flex-direction: column;
    gap: .15rem;
    height: 100%;
    justify-content: center;
}
.lti-label {
    font-size: .72rem;
    font-weight: 600;
    letter-spacing: .05em;
    text-transform: uppercase;
    color: var(--text-mute);
}
.lti-value {
    font-family: 'DM Mono', monospace;
    font-size: 1.45rem;
    font-weight: 600;
    color: var(--accent);
    line-height: 1;
}

/* ── Streamlit widget overrides ── */
label[data-testid="stWidgetLabel"] p {
    font-size: .8rem !important;
    font-weight: 500 !important;
    color: var(--text-body) !important;
    letter-spacing: .01em;
}
div[data-baseweb="input"] input,
div[data-baseweb="select"] div {
    border-color: var(--border) !important;
    border-radius: 7px !important;
    background: #FAFAFA !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: .875rem !important;
    color: var(--text-hd) !important;
}
div[data-baseweb="input"] input:focus,
div[data-baseweb="select"] div:focus-within {
    border-color: var(--accent) !important;
    box-shadow: 0 0 0 2px rgba(192,57,43,.15) !important;
}

/* ── Calculate button ── */
div[data-testid="stButton"] > button {
    background: var(--accent) !important;
    color: #fff !important;
    border: none !important;
    border-radius: 8px !important;
    padding: .65rem 2.2rem !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: .9rem !important;
    font-weight: 600 !important;
    letter-spacing: .02em !important;
    transition: opacity .15s, transform .1s !important;
    width: 100% !important;
}
div[data-testid="stButton"] > button:hover {
    opacity: .88 !important;
    transform: translateY(-1px) !important;
}

/* ── Results panel ── */
.result-panel {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 1.4rem 1.8rem;
    margin-top: 1.2rem;
    box-shadow: var(--shadow);
}
.result-panel h3 {
    font-size: .72rem;
    font-weight: 600;
    letter-spacing: .08em;
    text-transform: uppercase;
    color: var(--text-mute);
    margin: 0 0 1rem;
}
.metrics-row {
    display: flex;
    gap: 1.2rem;
    flex-wrap: wrap;
}
.metric-box {
    flex: 1;
    min-width: 130px;
    background: #FAFAF8;
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: .9rem 1rem;
}
.metric-label {
    font-size: .7rem;
    font-weight: 600;
    letter-spacing: .06em;
    text-transform: uppercase;
    color: var(--text-mute);
    margin-bottom: .35rem;
}
.metric-value {
    font-family: 'DM Mono', monospace;
    font-size: 1.5rem;
    font-weight: 700;
    color: var(--text-hd);
    line-height: 1;
}
.rating-badge {
    display: inline-block;
    padding: .25rem .75rem;
    border-radius: 20px;
    font-size: .85rem;
    font-weight: 600;
    margin-top: .4rem;
}
.rating-good  { background: #E8F5EE; color: #1E6E3E; }
.rating-avg   { background: #FEF3CD; color: #7A5800; }
.rating-poor  { background: #FDECEA; color: #9B2C2C; }

/* ── Divider ── */
.lf-divider {
    border: none;
    border-top: 1px solid var(--border);
    margin: 1.5rem 0 1rem;
}
</style>
""", unsafe_allow_html=True)

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="lf-header">
    <h1>
        <span class="brand">📊 Lauki Finance</span><span class="colon"> : </span><span class="subtitle-text">Credit Risk Modelling</span>
    </h1>
    <p>Enter borrower details to assess default probability and generate a credit score.</p>
</div>
""", unsafe_allow_html=True)

# ── Section 1 : Borrower Financials ──────────────────────────────────────────
st.markdown('<div class="lf-card"><div class="lf-card-title">Borrower Financials</div>', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1:
    age = st.number_input('Age', min_value=18, step=1, max_value=100, value=28)
with col2:
    income = st.number_input('Annual Income (₹)', min_value=0, value=1200000)
with col3:
    loan_amount = st.number_input('Loan Amount (₹)', min_value=0, value=2560000)
st.markdown('</div>', unsafe_allow_html=True)

# ── Loan-to-Income ratio (derived) ───────────────────────────────────────────
loan_to_income_ratio = loan_amount / income if income > 0 else 0.0

# ── Section 2 : Loan Details ─────────────────────────────────────────────────
st.markdown('<div class="lf-card"><div class="lf-card-title">Loan Details</div>', unsafe_allow_html=True)
col4, col5, col6 = st.columns(3)
with col4:
    st.markdown(f"""
    <div class="lti-box">
        <span class="lti-label">Loan-to-Income Ratio</span>
        <span class="lti-value">{loan_to_income_ratio:.2f}</span>
    </div>
    """, unsafe_allow_html=True)
with col5:
    loan_tenure_months = st.number_input('Loan Tenure (months)', min_value=0, step=1, value=36)
with col6:
    avg_dpd_per_delinquency = st.number_input('Avg DPD per Delinquency', min_value=0, value=20)
st.markdown('</div>', unsafe_allow_html=True)

# ── Section 3 : Credit Behaviour ─────────────────────────────────────────────
st.markdown('<div class="lf-card"><div class="lf-card-title">Credit Behaviour</div>', unsafe_allow_html=True)
col7, col8, col9 = st.columns(3)
with col7:
    delinquency_ratio = st.number_input('Delinquency Ratio (%)', min_value=0, max_value=100, step=1, value=30)
with col8:
    credit_utilization_ratio = st.number_input('Credit Utilization (%)', min_value=0, max_value=100, step=1, value=30)
with col9:
    num_open_accounts = st.number_input('Open Loan Accounts', min_value=1, max_value=4, step=1, value=2)
st.markdown('</div>', unsafe_allow_html=True)

# ── Section 4 : Loan Classification ──────────────────────────────────────────
st.markdown('<div class="lf-card"><div class="lf-card-title">Loan Classification</div>', unsafe_allow_html=True)
col10, col11, col12 = st.columns(3)
with col10:
    residence_type = st.selectbox('Residence Type', ['Owned', 'Rented', 'Mortgage'])
with col11:
    loan_purpose = st.selectbox('Loan Purpose', ['Education', 'Home', 'Auto', 'Personal'])
with col12:
    loan_type = st.selectbox('Loan Type', ['Unsecured', 'Secured'])
st.markdown('</div>', unsafe_allow_html=True)

# ── Calculate button ──────────────────────────────────────────────────────────
st.markdown('<hr class="lf-divider">', unsafe_allow_html=True)

if st.button('Calculate Credit Risk'):
    probability, credit_score, rating = predict(
        age, income, loan_amount, loan_tenure_months, avg_dpd_per_delinquency,
        delinquency_ratio, credit_utilization_ratio, num_open_accounts,
        residence_type, loan_purpose, loan_type
    )

    # Choose rating badge class
    rating_lower = rating.lower()
    if any(w in rating_lower for w in ['excellent', 'good', 'very good', 'a', 'b']):
        badge_class = "rating-good"
    elif any(w in rating_lower for w in ['average', 'fair', 'c']):
        badge_class = "rating-avg"
    else:
        badge_class = "rating-poor"

    st.markdown(f"""
    <div class="result-panel">
        <h3>Risk Assessment Results</h3>
        <div class="metrics-row">
            <div class="metric-box">
                <div class="metric-label">Default Probability</div>
                <div class="metric-value">{probability:.1%}</div>
            </div>
            <div class="metric-box">
                <div class="metric-label">Credit Score</div>
                <div class="metric-value">{credit_score}</div>
            </div>
            <div class="metric-box">
                <div class="metric-label">Rating</div>
                <div class="metric-value" style="font-size:1.1rem; padding-top:.3rem;">
                    <span class="rating-badge {badge_class}">{rating}</span>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("""
<div style="text-align:center; margin-top:2.5rem; font-size:.75rem; color:#9A9187;">
    Lauki Finance · Credit Risk Model · Codebasics ML Course
</div>
""", unsafe_allow_html=True)