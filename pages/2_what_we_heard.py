import streamlit as st

st.title("What We Heard")
st.markdown("*From our February 19th conversation — confirming we captured this correctly*")

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🏔️ Challenges")

    challenges = [
        ("76-80+ ERPs across the enterprise", "SAP, JDE, Oracle — every acquisition brings another system. Extracting audit data requires navigating each one individually."),
        ("Manual, time-intensive audit processes", "Data extraction for a single audit can take weeks. SSIS-based extraction pipelines, Access databases as UI — fragile and slow."),
        ("~900 controls to test", "SOX compliance across a sprawling, acquisitive organization. Interim and annual testing cycles are resource-constrained."),
        ("Limited cross-system visibility", "Hard to stitch data across ERPs, geographies, and business units for comprehensive audit coverage."),
        ("86+ TB of unstructured data", "Contracts, invoices, supporting documentation scattered across systems with no unified search or analysis."),
    ]

    for title, desc in challenges:
        st.markdown(
            f'<div class="poc-card">'
            f'<strong>⚠️ {title}</strong><br>'
            f'<span style="color:#6c757d; font-size:0.9rem;">{desc}</span>'
            f'</div>',
            unsafe_allow_html=True,
        )

with col2:
    st.markdown("### 🎯 Aspirations")

    aspirations = [
        ("Agents live by June/July for interim SOX testing", "Kim wants to show measurable progress before the next testing cycle. Tangible, not theoretical."),
        ("Expand audit coverage without expanding headcount", "Do more audits, deeper dives, larger sample sizes — with the same team. Data analytics as a force multiplier."),
        ("Cross-ERP audit analytics", "One platform to query across all 76+ ERPs. Stitch PO, invoice, and payment data regardless of source system."),
        ("AI-augmented exception detection", "Move from sampling to population-level testing. Let AI surface anomalies human reviewers would miss."),
        ("Replicable, scalable audit programs", "Build once, run across every business unit and geography. Consistent methodology, automated execution."),
    ]

    for title, desc in aspirations:
        st.markdown(
            f'<div class="poc-card">'
            f'<strong>✅ {title}</strong><br>'
            f'<span style="color:#6c757d; font-size:0.9rem;">{desc}</span>'
            f'</div>',
            unsafe_allow_html=True,
        )

st.divider()

st.markdown("### 🏗️ Current Environment")

env_col1, env_col2, env_col3, env_col4 = st.columns(4)
env_col1.metric("ERPs", "76-80+", "SAP, JDE, Oracle")
env_col2.metric("Controls", "~900", "SOX compliance")
env_col3.metric("Unstructured Data", "86+ TB", "Contracts, docs")
env_col4.metric("GRC Platform", "AuditBoard", "+ ServiceNow")
