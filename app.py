import streamlit as st

st.set_page_config(
    page_title="Ingersoll Rand × Snowflake | Internal Audit",
    page_icon="❄️",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
    .block-container {padding-top: 1.5rem; padding-bottom: 1rem;}
    [data-testid="stSidebar"] {background-color: #f0f4f8;}
    h1 {color: #1a3a5c;}
    h2 {color: #29B5E8;}
    h3 {color: #1a3a5c;}
    .stMetric label {font-size: 0.85rem !important;}
    .highlight-box {
        background: linear-gradient(135deg, #e8f4f8 0%, #d1ecf1 100%);
        border-left: 4px solid #29B5E8;
        padding: 1rem 1.25rem;
        border-radius: 0 8px 8px 0;
        margin: 0.5rem 0;
    }
    .quote-box {
        background: #f8f9fa;
        border-left: 4px solid #6c757d;
        padding: 1rem 1.25rem;
        border-radius: 0 8px 8px 0;
        margin: 0.75rem 0;
        font-style: italic;
        color: #495057;
    }
    .poc-card {
        background: white;
        border: 1px solid #dee2e6;
        border-radius: 10px;
        padding: 1.25rem;
        margin: 0.5rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    .section-num {
        display: inline-block;
        background: #29B5E8;
        color: white;
        width: 28px;
        height: 28px;
        border-radius: 50%;
        text-align: center;
        line-height: 28px;
        font-weight: bold;
        font-size: 0.85rem;
        margin-right: 8px;
    }
</style>
""", unsafe_allow_html=True)

agenda = st.Page("pages/1_agenda.py", title="Agenda & Introductions", icon="📋")
what_we_heard = st.Page("pages/2_what_we_heard.py", title="What We Heard", icon="🎯")
art_of_possible = st.Page("pages/3_art_of_possible.py", title="Art of the Possible", icon="🚀")
customer_stories = st.Page("pages/4_customer_stories.py", title="Customer Stories", icon="📊")
poc_proposal = st.Page("pages/5_poc_proposal.py", title="POC Proposal", icon="🔧")
live_demo = st.Page("pages/6_live_demo.py", title="Live Concept Demo", icon="⚡")
next_steps = st.Page("pages/7_next_steps.py", title="Next Steps", icon="🤝")

pg = st.navigation([agenda, what_we_heard, art_of_possible, customer_stories, poc_proposal, live_demo, next_steps])

IR_LOGO = "https://azure-na-images.contentstack.com/v3/assets/blta8b68ee4d57aa34b/bltec884852b3e562e5/6880eec793b713f4a18091d6/ingersoll_rand_bigger_logo.jpg?width=400&quality=80"
SF_LOGO = "https://logos-world.net/wp-content/uploads/2022/11/Snowflake-Symbol.png"

with st.sidebar:
    st.image(IR_LOGO, width=140)
    st.image(SF_LOGO, width=50)
    st.caption("Ingersoll Rand × Snowflake")
    st.caption("Internal Audit — Follow-Up Discussion")
    st.divider()
    st.markdown("**Your Snowflake Team**")
    st.markdown("- Drew Frechette — *Account Executive*")
    st.markdown("- Senthil Valli — *Solution Engineer*")
    st.markdown("- Doug Brown — *AI/ML AFE*")
    st.markdown("- Greg Sloyer — *Industry Principal*")
    st.divider()
    st.caption("March 2026")

pg.run()
