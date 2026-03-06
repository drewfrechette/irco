import streamlit as st

st.title("POC Proposal: Three-Way Match")
st.markdown("*PO ↔ Invoice ↔ Goods Receipt — across 76+ ERPs, powered by Cortex AI*")

st.divider()

st.markdown("### Why Three-Way Match?")

why_col1, why_col2, why_col3 = st.columns(3)

with why_col1:
    st.markdown(
        '<div class="poc-card" style="border-left: 4px solid #ffc107;">'
        '<strong>🎯 High Impact</strong><br>'
        'Touches every business unit, every ERP. '
        'A universal audit test that scales across the entire organization.'
        '</div>',
        unsafe_allow_html=True,
    )

with why_col2:
    st.markdown(
        '<div class="poc-card" style="border-left: 4px solid #28a745;">'
        '<strong>⚡ Fast to Value</strong><br>'
        'Structured data already exists in your ERPs. '
        'No unstructured data challenges. Clear success criteria.'
        '</div>',
        unsafe_allow_html=True,
    )

with why_col3:
    st.markdown(
        '<div class="poc-card" style="border-left: 4px solid #29B5E8;">'
        '<strong>🔧 Extensible</strong><br>'
        'Same architecture powers Rev27 variance, duplicate invoice detection, '
        'and future audit tests.'
        '</div>',
        unsafe_allow_html=True,
    )

st.divider()

st.markdown("### Architecture")

st.code("""
┌─────────────────────────────────────────────────────────────┐
│                    IRCO ERP Data                            │
│              SAP  ·  JDE  ·  Oracle  ·  Others              │
└──────────────────────────┬──────────────────────────────────┘
                           │
                    Zero-Copy Clone
                  (audit-isolated env)
                           │
               ┌───────────┴───────────┐
               │    Semantic Model     │ ← Cortex Analyst
               │  (PO / Invoice / GR)  │   Natural language → SQL
               └───────────┬───────────┘
                           │
                    Cortex Agent
                           │
          ┌────────────────┼────────────────┐
          │                │                │
    ┌─────┴─────┐   ┌─────┴─────┐   ┌─────┴─────┐
    │  Tool 1   │   │  Tool 2   │   │  Tool 3   │
    │ Three-Way │   │  Rev27    │   │ Duplicate  │
    │   Match   │   │ Variance  │   │  Invoice   │
    └─────┬─────┘   └─────┬─────┘   └─────┬─────┘
          │                │                │
          └────────────────┼────────────────┘
                           │
               Streamlit Dashboard
          (Exception Viewer + Audit Trail)
""", language=None)

st.divider()

st.markdown("### What the Agent Does")

step_col1, step_col2 = st.columns(2)

with step_col1:
    steps = [
        ("1️⃣ Receive", "Auditor asks a natural language question: *\"Show me unmatched invoices over $10K from the Davidson plant in Q4\"*"),
        ("2️⃣ Query", "Cortex Analyst translates to deterministic SQL via the semantic model — queries across all relevant ERPs"),
        ("3️⃣ Match", "Three-way match tool compares PO ↔ Invoice ↔ Goods Receipt. Flags mismatches on quantity, price, dates"),
    ]
    for emoji, desc in steps:
        st.markdown(
            f'<div class="highlight-box"><strong>{emoji}</strong><br>{desc}</div>',
            unsafe_allow_html=True,
        )

with step_col2:
    steps2 = [
        ("4️⃣ Flag", "Exceptions categorized: missing GR, price variance > threshold, quantity mismatch, timing anomaly"),
        ("5️⃣ Trail", "Every step logged — query, results, match logic, exceptions — complete audit trail"),
        ("6️⃣ Present", "Results surfaced in Streamlit dashboard with drill-down, export, and remediation tracking"),
    ]
    for emoji, desc in steps2:
        st.markdown(
            f'<div class="highlight-box"><strong>{emoji}</strong><br>{desc}</div>',
            unsafe_allow_html=True,
        )

st.divider()

st.markdown("### POC Scope & Timeline")

scope_col1, scope_col2 = st.columns(2)

with scope_col1:
    st.markdown("#### In Scope")
    st.markdown("""
- **1-2 ERP sources** (start with highest-volume SAP instance)
- **Three-way match** across PO, Invoice, Goods Receipt
- **Semantic model** for natural language querying
- **Cortex Agent** with match tool + exception flagging
- **Streamlit dashboard** for exception review
- **Complete audit trail** for every agent action
""")

with scope_col2:
    st.markdown("#### Success Criteria")
    st.markdown("""
- ✅ Agent correctly identifies known mismatches in test data
- ✅ Natural language queries return accurate, deterministic results
- ✅ Exceptions categorized and prioritized automatically
- ✅ Full audit trail captured for every interaction
- ✅ Dashboard usable by audit team without technical training
- ✅ Processing time: minutes vs. current weeks
""")

st.divider()

st.markdown("### Timeline")

t1, t2, t3 = st.columns(3)

with t1:
    st.markdown(
        '<div class="poc-card" style="border-top: 4px solid #ffc107;">'
        '<strong>Weeks 1-2</strong><br>'
        'Data onboarding & semantic model<br>'
        '<span style="color:#6c757d; font-size:0.85rem;">Clone ERP data, build semantic layer, validate schema</span>'
        '</div>',
        unsafe_allow_html=True,
    )

with t2:
    st.markdown(
        '<div class="poc-card" style="border-top: 4px solid #29B5E8;">'
        '<strong>Weeks 3-4</strong><br>'
        'Agent build & match logic<br>'
        '<span style="color:#6c757d; font-size:0.85rem;">Cortex Agent + tools, exception rules, audit trail</span>'
        '</div>',
        unsafe_allow_html=True,
    )

with t3:
    st.markdown(
        '<div class="poc-card" style="border-top: 4px solid #28a745;">'
        '<strong>Weeks 5-6</strong><br>'
        'Dashboard & validation<br>'
        '<span style="color:#6c757d; font-size:0.85rem;">Streamlit UI, user testing, results review with audit team</span>'
        '</div>',
        unsafe_allow_html=True,
    )

st.info("**Target:** Agent operational before interim SOX testing cycle (June/July)")
