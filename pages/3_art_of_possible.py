import streamlit as st

st.title("Art of the Possible")
st.markdown("*Snowflake Cortex AI — mapped to your Internal Audit workflow*")

st.divider()

st.markdown("### Two-Lane AI Architecture for Audit")
st.markdown("SOX-compliant controls and exploratory analytics can coexist on the same platform.")

lane1, lane2 = st.columns(2)

with lane1:
    st.markdown(
        '<div class="poc-card" style="border-left: 4px solid #28a745;">'
        '<h4 style="color:#28a745;">🔒 Lane 1: SOX-Compliant Controls</h4>'
        '<ul>'
        '<li><strong>Cortex Analyst</strong> — natural language → deterministic SQL</li>'
        '<li>Semantic models enforce approved query patterns</li>'
        '<li>Version-controlled, auditable, reproducible</li>'
        '<li>Every query logged with full lineage</li>'
        '<li>RBAC + dynamic masking enforced</li>'
        '</ul>'
        '<p style="color:#6c757d; font-size:0.85rem;">Use for: SOX testing, control validation, regulatory reporting</p>'
        '</div>',
        unsafe_allow_html=True,
    )

with lane2:
    st.markdown(
        '<div class="poc-card" style="border-left: 4px solid #29B5E8;">'
        '<h4 style="color:#29B5E8;">🔍 Lane 2: Exploratory / Operational</h4>'
        '<ul>'
        '<li><strong>Cortex Agents</strong> — multi-tool orchestration</li>'
        '<li>Flexible analysis, anomaly detection, pattern discovery</li>'
        '<li>Search across 86+ TB of unstructured docs</li>'
        '<li>Exception investigation & root cause analysis</li>'
        '<li>Natural language interaction for ad-hoc queries</li>'
        '</ul>'
        '<p style="color:#6c757d; font-size:0.85rem;">Use for: Fraud detection, deep dives, operational audits, special projects</p>'
        '</div>',
        unsafe_allow_html=True,
    )

st.divider()

st.markdown("### Cortex AI Stack — Your Audit Use Cases")

capabilities = [
    {
        "name": "Cortex Analyst",
        "icon": "📊",
        "what": "Natural language → SQL over structured data via semantic models",
        "audit_use": "\"Show me all POs over $50K with no matching goods receipt\" — deterministic, auditable SQL every time",
        "sox": True,
    },
    {
        "name": "Cortex Agents",
        "icon": "🤖",
        "what": "Multi-tool AI orchestration — combines Analyst, Search, and custom tools",
        "audit_use": "Three-way match agent: receives a question, queries PO/Invoice/GR data, runs match logic, flags exceptions, writes audit trail",
        "sox": False,
    },
    {
        "name": "Cortex Search",
        "icon": "🔎",
        "what": "Semantic search over unstructured documents (contracts, invoices, policies)",
        "audit_use": "\"Find all contracts with change-of-control clauses related to the Frigoblock acquisition\" — instant results across 86+ TB",
        "sox": False,
    },
    {
        "name": "Document AI",
        "icon": "📄",
        "what": "Extract structured data from invoices, receipts, contracts at scale",
        "audit_use": "Automate invoice data extraction across formats and languages — feed directly into three-way match",
        "sox": False,
    },
    {
        "name": "Zero-Copy Clones",
        "icon": "🔐",
        "what": "Instant, cost-free copies of production data for audit-isolated environments",
        "audit_use": "Clone ERP data into an audit sandbox — no extraction delays, no data movement, instant freshness",
        "sox": True,
    },
    {
        "name": "RBAC & Dynamic Masking",
        "icon": "🛡️",
        "what": "Role-based access control with real-time data masking policies",
        "audit_use": "Auditors see only what they need. PII masked automatically. Every access logged for compliance.",
        "sox": True,
    },
]

for cap in capabilities:
    st.markdown(
        f'<div class="poc-card">'
        f'<strong>{cap["icon"]} {cap["name"]}</strong><br>'
        f'{cap["what"]}<br>'
        f'<span style="color:#29B5E8; font-size:0.9rem;">→ <em>{cap["audit_use"]}</em></span>'
        f'</div>',
        unsafe_allow_html=True,
    )

st.divider()

st.markdown("### Integration with Your Ecosystem")

int_col1, int_col2, int_col3 = st.columns(3)

with int_col1:
    st.markdown(
        '<div class="poc-card">'
        '<strong>🔗 Microsoft Integration</strong><br>'
        'Cortex MCP ↔ Azure AI Foundry<br>'
        'Copilot Studio connectors<br>'
        'Teams-native audit notifications'
        '</div>',
        unsafe_allow_html=True,
    )

with int_col2:
    st.markdown(
        '<div class="poc-card">'
        '<strong>📋 AuditBoard</strong><br>'
        'Snowflake as the data layer behind GRC<br>'
        'Feed exception results directly into workflows<br>'
        'Unified audit trail across platforms'
        '</div>',
        unsafe_allow_html=True,
    )

with int_col3:
    st.markdown(
        '<div class="poc-card">'
        '<strong>⚙️ ServiceNow</strong><br>'
        'Auto-create tickets from audit exceptions<br>'
        'Track remediation through existing workflows<br>'
        'Close the loop on findings'
        '</div>',
        unsafe_allow_html=True,
    )
