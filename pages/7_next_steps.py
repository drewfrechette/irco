import streamlit as st

st.title("Engagement Model & Next Steps")
st.markdown("*How we get from today to agents live for interim SOX testing*")

st.divider()

st.markdown("### Recommended Path")

path_col1, path_col2, path_col3 = st.columns(3)

with path_col1:
    st.markdown(
        '<div class="poc-card" style="border-top: 4px solid #ffc107; text-align:center;">'
        '<h3>Phase 1</h3>'
        '<strong>POC: Three-Way Match</strong><br><br>'
        '<strong>Duration:</strong> 4-6 weeks<br>'
        '<strong>Scope:</strong> 1-2 ERP sources<br>'
        '<strong>Outcome:</strong> Working agent + dashboard<br>'
        '<strong>Target:</strong> April-May 2026<br><br>'
        '<em>Prove the pattern. Demonstrate value.</em>'
        '</div>',
        unsafe_allow_html=True,
    )

with path_col2:
    st.markdown(
        '<div class="poc-card" style="border-top: 4px solid #29B5E8; text-align:center;">'
        '<h3>Phase 2</h3>'
        '<strong>Expand: Additional Tools</strong><br><br>'
        '<strong>Duration:</strong> 4-8 weeks<br>'
        '<strong>Add:</strong> Rev27, Duplicate Invoice<br>'
        '<strong>Outcome:</strong> Multi-tool agent<br>'
        '<strong>Target:</strong> June-July 2026<br><br>'
        '<em>Scale the architecture. Add audit tests.</em>'
        '</div>',
        unsafe_allow_html=True,
    )

with path_col3:
    st.markdown(
        '<div class="poc-card" style="border-top: 4px solid #28a745; text-align:center;">'
        '<h3>Phase 3</h3>'
        '<strong>Production: SOX Testing</strong><br><br>'
        '<strong>Duration:</strong> Ongoing<br>'
        '<strong>Scope:</strong> All ERPs, all controls<br>'
        '<strong>Outcome:</strong> Continuous monitoring<br>'
        '<strong>Target:</strong> H2 2026<br><br>'
        '<em>Operational at scale. Full coverage.</em>'
        '</div>',
        unsafe_allow_html=True,
    )

st.divider()

st.markdown("### Engagement Options")

opt1, opt2 = st.columns(2)

with opt1:
    st.markdown(
        '<div class="poc-card">'
        '<h4>Option A: Focused POC Sprint</h4>'
        '<strong>2-3 day intensive engagement</strong><br><br>'
        '• Snowflake SE + AI/ML specialist onsite or virtual<br>'
        '• Build Three-Way Match agent against your data<br>'
        '• Deliver working prototype + architecture blueprint<br>'
        '• Minimal time commitment from your team<br><br>'
        '<em style="color:#28a745;">Fastest path to demonstrable value</em>'
        '</div>',
        unsafe_allow_html=True,
    )

with opt2:
    st.markdown(
        '<div class="poc-card">'
        '<h4>Option B: RSA/PRSA Engagement</h4>'
        '<strong>Dedicated Snowflake resources, 12 months</strong><br><br>'
        '• 20 hrs/week of dedicated SA time<br>'
        '• Internal Audit / SOX included as focus area<br>'
        '• Covers POC → production journey<br>'
        '• Includes all three phases above<br><br>'
        '<em style="color:#29B5E8;">Comprehensive partner for the full journey</em>'
        '</div>',
        unsafe_allow_html=True,
    )

st.divider()

st.markdown("### SalesMate: Proof of Pattern")
st.markdown(
    '<div class="highlight-box">'
    'Your SalesMate initiative — <strong>26,000 hours saved annually</strong> — demonstrates that IR already '
    'knows how to deploy AI agents at scale. The Internal Audit use case follows the same pattern: '
    'structured data + semantic model + agent + Streamlit dashboard. Different domain, same architecture.'
    '</div>',
    unsafe_allow_html=True,
)

st.divider()

st.markdown("### Immediate Next Steps")

next_steps = [
    ("Align on POC scope", "Confirm 1-2 ERP sources, agree on test data set, define success criteria"),
    ("Schedule kickoff", "2-3 day engagement with Snowflake SE team + AI/ML AFE"),
    ("Data access", "IR team provisions access to PO/Invoice/GR data (or sample extract)"),
    ("Build & iterate", "Weekly check-ins during 4-6 week POC sprint"),
    ("Review & decide", "Demo results to Kim's team, decide on expansion plan"),
]

for i, (step, detail) in enumerate(next_steps, 1):
    st.markdown(
        f'<div class="highlight-box">'
        f'<span class="section-num">{i}</span>'
        f'<strong>{step}</strong><br>'
        f'<span style="color:#6c757d;">{detail}</span>'
        f'</div>',
        unsafe_allow_html=True,
    )

st.divider()

st.markdown("### Your Snowflake Team")

team_col1, team_col2, team_col3, team_col4 = st.columns(4)

with team_col1:
    st.markdown(
        '<div class="poc-card" style="text-align:center;">'
        '<strong>Drew Frechette</strong><br>'
        'Account Executive<br>'
        '<em style="color:#6c757d;">Your primary technical contact</em>'
        '</div>',
        unsafe_allow_html=True,
    )

with team_col2:
    st.markdown(
        '<div class="poc-card" style="text-align:center;">'
        '<strong>Senthil Valli</strong><br>'
        'Solution Engineer<br>'
        '<em style="color:#6c757d;">Architecture & implementation</em>'
        '</div>',
        unsafe_allow_html=True,
    )

with team_col3:
    st.markdown(
        '<div class="poc-card" style="text-align:center;">'
        '<strong>Doug Brown</strong><br>'
        'AI/ML AFE<br>'
        '<em style="color:#6c757d;">Cortex AI specialist</em>'
        '</div>',
        unsafe_allow_html=True,
    )

with team_col4:
    st.markdown(
        '<div class="poc-card" style="text-align:center;">'
        '<strong>Greg Sloyer</strong><br>'
        'Industry Principal<br>'
        '<em style="color:#6c757d;">Manufacturing & audit domain</em>'
        '</div>',
        unsafe_allow_html=True,
    )
