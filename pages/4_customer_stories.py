import streamlit as st

st.title("Customer Stories")
st.markdown("*Anonymized case studies from organizations with similar audit challenges*")

st.divider()

tab1, tab2 = st.tabs(["📊 Case Study 1: Audit Data Analytics", "🔐 Case Study 2: Data Governance & Security Auditing"])

with tab1:
    st.markdown("### Global Industrial Manufacturer — Audit Data Analytics")
    st.markdown("*A multi-billion dollar industrial manufacturer with complex ERP landscape*")

    st.markdown("#### The Challenge")
    st.markdown(
        '<div class="poc-card" style="border-left: 4px solid #dc3545;">'
        '<ul>'
        '<li>Manual extraction from multiple SAP instances — taking <strong>weeks to months</strong> per audit</li>'
        '<li>Days just to extract PO data by plant</li>'
        '<li>Limited sample sizes due to manual constraints</li>'
        '<li>Audit team spending more time on data wrangling than actual analysis</li>'
        '<li>Site visits required large teams for extended periods</li>'
        '</ul>'
        '</div>',
        unsafe_allow_html=True,
    )

    st.markdown("#### What They Built")
    st.markdown(
        '<div class="poc-card" style="border-left: 4px solid #29B5E8;">'
        '<ul>'
        '<li><strong>Single unified dashboard</strong> across all ERP instances</li>'
        '<li>Dramatically increased sample sizes — from sampling to population-level testing</li>'
        '<li>Cross-system, cross-geography data stitching</li>'
        '<li>Discovered open POs dating back to 2015 that had been invisible</li>'
        '<li>Built automated robot to auto-close POs after 100 days of inactivity</li>'
        '</ul>'
        '</div>',
        unsafe_allow_html=True,
    )

    st.markdown("#### Outcomes")

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("PACS Tests Automated", "38%", "Continuous monitoring")
    m2.metric("Cost Avoidance", "~$270K", "Over 3 years")
    m3.metric("PO Analysis Time", "2 weeks", "Down from 1-2 months")
    m4.metric("Full Audits", "+50%", "20 → 25 + 5 deep dives")

    st.markdown("#### Additional Impact")
    imp1, imp2 = st.columns(2)
    with imp1:
        st.markdown(
            '<div class="highlight-box">'
            '<strong>Site Visit Efficiency</strong><br>'
            '5-6 people for 4 weeks → 2-3 people for 2 weeks<br>'
            '<em>Same coverage, fraction of the cost</em>'
            '</div>',
            unsafe_allow_html=True,
        )
    with imp2:
        st.markdown(
            '<div class="highlight-box">'
            '<strong>Replicability</strong><br>'
            'Build once, deploy across every plant and geography<br>'
            '<em>Consistent methodology, automated execution</em>'
            '</div>',
            unsafe_allow_html=True,
        )

    st.markdown(
        '<div class="quote-box">'
        '"The primary benefits of using our data analytics include improved productivity, efficiency, '
        'better controls, complex analysis capabilities, and replicability."'
        '<br><br>— Internal Audit Leadership'
        '</div>',
        unsafe_allow_html=True,
    )

    st.markdown("#### Why This Matters for IR")
    st.success(
        "This company had a similar ERP landscape and audit challenge. They started with PO analysis — "
        "the same starting point we're recommending — and expanded from there. "
        "Their 76+ ERPs parallel your 76-80+ ERPs."
    )

with tab2:
    st.markdown("### Enterprise Organization — Data Governance & Security Auditing")
    st.markdown("*Replaced legacy platform with Snowflake for comprehensive audit traceability*")

    st.markdown("#### The Challenge")
    st.markdown(
        '<div class="poc-card" style="border-left: 4px solid #dc3545;">'
        '<ul>'
        '<li>Legacy platform (Cloudera) was a <strong>"black box"</strong> — no visibility into data access</li>'
        '<li>Could not answer: Who accessed what data? When? How often? From where?</li>'
        '<li>Unable to enforce granular access policies consistently</li>'
        '<li>Reactive security posture — finding issues after the fact</li>'
        '<li>Audit and compliance processes were manual and incomplete</li>'
        '</ul>'
        '</div>',
        unsafe_allow_html=True,
    )

    st.markdown("#### What They Built with Snowflake")
    st.markdown(
        '<div class="poc-card" style="border-left: 4px solid #29B5E8;">'
        '<ul>'
        '<li><strong>Complete traceability</strong> — every query, every access, every role, every machine</li>'
        '<li>Automated RBAC enforcement across all data assets</li>'
        '<li>PII masking policies applied dynamically based on role</li>'
        '<li>Real-time monitoring of data access patterns</li>'
        '<li>Simplified audit and compliance with built-in governance</li>'
        '</ul>'
        '</div>',
        unsafe_allow_html=True,
    )

    st.markdown("#### Outcomes")

    r1, r2, r3 = st.columns(3)
    with r1:
        st.metric("Security Posture", "Proactive", "From reactive")
    with r2:
        st.metric("Audit Complexity", "Simplified", "Complete traceability")
    with r3:
        st.metric("Policy Enforcement", "Automated", "RBAC + PII masking")

    st.markdown(
        '<div class="quote-box">'
        '"With Snowflake traceability we are able to know every single detail that is happening, '
        'who is accessing what, how many times, what role, via what machine."'
        '<br><br>— Data Governance Leadership'
        '</div>',
        unsafe_allow_html=True,
    )

    st.markdown("#### Why This Matters for IR")
    st.success(
        "With 76+ ERPs and growing through acquisitions, governance and traceability are critical. "
        "Snowflake's native RBAC, dynamic masking, and complete access logging give your audit team "
        "the visibility they need — built into the platform, not bolted on."
    )
