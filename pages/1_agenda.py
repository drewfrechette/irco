import streamlit as st

st.title("Agenda & Introductions")

st.markdown("### Internal Audit — Follow-Up: The Art of the Possible")
st.markdown("*Building on our February 19th conversation*")

st.divider()

col1, col2 = st.columns([3, 2])

with col1:
    st.markdown("### Today's Agenda")
    agenda_items = [
        ("What We Heard", "Playback of your challenges, goals & aspirations"),
        ("Art of the Possible", "Snowflake Cortex AI mapped to your audit workflow"),
        ("Customer Stories", "Two anonymized case studies from similar organizations"),
        ("POC Proposal", "Three-Way Match — immediate value, measurable results"),
        ("Live Concept Demo", "What the finished agent looks like in practice"),
        ("Next Steps", "Engagement model, timeline & resources"),
    ]

    for i, (title, desc) in enumerate(agenda_items, 1):
        st.markdown(
            f'<div class="highlight-box">'
            f'<span class="section-num">{i}</span>'
            f'<strong>{title}</strong> — {desc}'
            f'</div>',
            unsafe_allow_html=True,
        )

with col2:
    st.markdown("### Meeting Objective")
    st.info(
        "Show the Internal Audit team specific, actionable ways Snowflake's "
        "Cortex AI platform can transform their audit processes — and leave "
        "with agreement on a focused POC to prove value."
    )

    st.markdown("### Your Team Today")
    irco_team = {
        "Kim Ford": "VP, Internal Audit",
        "Jon Castrey": "Director, Americas Audit",
        "Stephanie Sydow": "Director, Global SOX",
        "Alaina Valkoff": "IT Audit Manager",
    }
    for name, role in irco_team.items():
        st.markdown(f"**{name}** — *{role}*")

st.divider()
st.markdown(
    '<div class="highlight-box" style="border-left: 4px solid #28a745;">'
    '<strong>Our Mission</strong><br>'
    'Shift Internal Audit from a 60/40 SOX-to-Operational split to a <strong>40/60 model</strong> — '
    'freeing the team to spend more time on high-value operational audits, strategic risk, and '
    'proactive insights. Snowflake and Cortex AI are the lever to automate the repetitive, '
    'scale the coverage, and make the shift possible.'
    '</div>',
    unsafe_allow_html=True,
)
