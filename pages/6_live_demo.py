import streamlit as st
import pandas as pd
import random

st.title("Live Concept Demo")
st.markdown("*What the Three-Way Match agent looks like in practice*")

st.divider()

random.seed(42)

erp_systems = ["SAP-NA", "SAP-EU", "JDE-APAC", "Oracle-LATAM"]
plants = ["Davidson, NC", "Swords, Ireland", "Milwaukee, WI", "Chennai, India", "Wuxi, China", "São Paulo, Brazil"]
vendors = [f"Vendor-{i:04d}" for i in range(1, 51)]

@st.cache_data
def generate_three_way_data():
    pos = []
    invoices = []
    goods_receipts = []
    matches = []

    for i in range(1, 201):
        erp = random.choice(erp_systems)
        plant = random.choice(plants)
        vendor = random.choice(vendors)
        po_amount = round(random.uniform(500, 150000), 2)
        qty = random.randint(1, 500)
        unit_price = round(po_amount / qty, 2)
        po_date = pd.Timestamp("2025-07-01") + pd.Timedelta(days=random.randint(0, 250))

        pos.append({
            "PO_NUMBER": f"PO-{erp[:3]}-{i:06d}",
            "ERP_SOURCE": erp,
            "PLANT": plant,
            "VENDOR_ID": vendor,
            "PO_DATE": po_date,
            "LINE_AMOUNT": po_amount,
            "QUANTITY": qty,
            "UNIT_PRICE": unit_price,
            "STATUS": "APPROVED",
        })

        has_invoice = random.random() > 0.08
        has_gr = random.random() > 0.12

        inv_amount = po_amount
        inv_qty = qty
        gr_qty = qty
        exception_type = None

        scenario = random.random()
        if scenario < 0.15:
            inv_amount = round(po_amount * random.uniform(1.02, 1.15), 2)
            exception_type = "PRICE_VARIANCE"
        elif scenario < 0.25:
            inv_qty = qty + random.randint(1, int(max(qty * 0.1, 2)))
            exception_type = "QTY_MISMATCH"
        elif scenario < 0.30:
            gr_qty = qty - random.randint(1, int(max(qty * 0.1, 1)))
            exception_type = "SHORT_SHIPMENT"

        if has_invoice:
            invoices.append({
                "INVOICE_NUMBER": f"INV-{i:06d}",
                "PO_NUMBER": f"PO-{erp[:3]}-{i:06d}",
                "VENDOR_ID": vendor,
                "INVOICE_DATE": po_date + pd.Timedelta(days=random.randint(5, 45)),
                "INVOICE_AMOUNT": inv_amount,
                "INVOICE_QTY": inv_qty,
            })
        else:
            exception_type = "MISSING_INVOICE"

        if has_gr:
            goods_receipts.append({
                "GR_NUMBER": f"GR-{i:06d}",
                "PO_NUMBER": f"PO-{erp[:3]}-{i:06d}",
                "GR_DATE": po_date + pd.Timedelta(days=random.randint(3, 30)),
                "GR_QTY": gr_qty if has_gr else 0,
                "PLANT": plant,
            })
        else:
            if exception_type is None:
                exception_type = "MISSING_GR"
            else:
                exception_type = exception_type + " + MISSING_GR"

        match_status = "MATCHED" if exception_type is None else "EXCEPTION"
        matches.append({
            "PO_NUMBER": f"PO-{erp[:3]}-{i:06d}",
            "ERP_SOURCE": erp,
            "PLANT": plant,
            "VENDOR_ID": vendor,
            "PO_AMOUNT": po_amount,
            "INVOICE_AMOUNT": inv_amount if has_invoice else None,
            "GR_QTY": gr_qty if has_gr else None,
            "PO_QTY": qty,
            "MATCH_STATUS": match_status,
            "EXCEPTION_TYPE": exception_type,
            "VARIANCE_AMOUNT": round(abs(inv_amount - po_amount), 2) if has_invoice and exception_type and "PRICE" in str(exception_type) else 0,
            "RISK_SCORE": random.randint(60, 99) if match_status == "EXCEPTION" else random.randint(1, 30),
        })

    return pd.DataFrame(pos), pd.DataFrame(invoices), pd.DataFrame(goods_receipts), pd.DataFrame(matches)


po_df, inv_df, gr_df, match_df = generate_three_way_data()

st.markdown("### 🤖 Agent Interaction")
st.markdown(
    '<div class="highlight-box">'
    'This demonstrates what an auditor\'s interaction with the Cortex Agent would look like. '
    'The agent receives natural language questions, queries across ERPs, runs match logic, and surfaces exceptions.'
    '</div>',
    unsafe_allow_html=True,
)

query = st.selectbox(
    "Ask the audit agent:",
    [
        "Show me all unmatched invoices over $10,000",
        "What are the top exceptions by risk score?",
        "Summarize three-way match status across all ERPs",
        "Show me price variances greater than 5%",
        "Which vendors have the most exceptions?",
    ],
)

if query == "Show me all unmatched invoices over $10,000":
    st.markdown("**Agent Response:**")
    exceptions = match_df[
        (match_df["MATCH_STATUS"] == "EXCEPTION") &
        (match_df["PO_AMOUNT"] > 10000)
    ].sort_values("RISK_SCORE", ascending=False)

    e1, e2, e3, e4 = st.columns(4)
    e1.metric("Exceptions Found", len(exceptions))
    e2.metric("Total Value at Risk", f"${exceptions['PO_AMOUNT'].sum():,.0f}")
    e3.metric("Avg Risk Score", f"{exceptions['RISK_SCORE'].mean():.0f}")
    e4.metric("ERPs Affected", exceptions["ERP_SOURCE"].nunique())

    st.dataframe(
        exceptions[["PO_NUMBER", "ERP_SOURCE", "PLANT", "VENDOR_ID", "PO_AMOUNT", "INVOICE_AMOUNT", "EXCEPTION_TYPE", "RISK_SCORE"]],
        use_container_width=True,
        hide_index=True,
    )

elif query == "What are the top exceptions by risk score?":
    st.markdown("**Agent Response:**")
    top = match_df[match_df["MATCH_STATUS"] == "EXCEPTION"].nlargest(15, "RISK_SCORE")
    st.dataframe(
        top[["PO_NUMBER", "ERP_SOURCE", "PLANT", "VENDOR_ID", "PO_AMOUNT", "EXCEPTION_TYPE", "RISK_SCORE", "VARIANCE_AMOUNT"]],
        use_container_width=True,
        hide_index=True,
    )

elif query == "Summarize three-way match status across all ERPs":
    st.markdown("**Agent Response:**")
    summary = match_df.groupby(["ERP_SOURCE", "MATCH_STATUS"]).size().unstack(fill_value=0)
    st.dataframe(summary, use_container_width=True)

    chart_data = match_df.groupby("ERP_SOURCE")["MATCH_STATUS"].value_counts().reset_index(name="count")
    st.bar_chart(chart_data, x="ERP_SOURCE", y="count", color="MATCH_STATUS", horizontal=False)

elif query == "Show me price variances greater than 5%":
    st.markdown("**Agent Response:**")
    price_var = match_df[match_df["EXCEPTION_TYPE"].str.contains("PRICE", na=False)].copy()
    price_var["VARIANCE_PCT"] = ((price_var["INVOICE_AMOUNT"] - price_var["PO_AMOUNT"]) / price_var["PO_AMOUNT"] * 100).round(2)
    price_var = price_var[price_var["VARIANCE_PCT"] > 5].sort_values("VARIANCE_PCT", ascending=False)

    st.dataframe(
        price_var[["PO_NUMBER", "ERP_SOURCE", "VENDOR_ID", "PO_AMOUNT", "INVOICE_AMOUNT", "VARIANCE_PCT", "RISK_SCORE"]],
        use_container_width=True,
        hide_index=True,
    )

elif query == "Which vendors have the most exceptions?":
    st.markdown("**Agent Response:**")
    vendor_exc = match_df[match_df["MATCH_STATUS"] == "EXCEPTION"].groupby("VENDOR_ID").agg(
        EXCEPTION_COUNT=("MATCH_STATUS", "count"),
        TOTAL_VALUE=("PO_AMOUNT", "sum"),
        AVG_RISK=("RISK_SCORE", "mean"),
    ).sort_values("EXCEPTION_COUNT", ascending=False).head(10).reset_index()
    vendor_exc["TOTAL_VALUE"] = vendor_exc["TOTAL_VALUE"].apply(lambda x: f"${x:,.0f}")
    vendor_exc["AVG_RISK"] = vendor_exc["AVG_RISK"].round(0).astype(int)
    st.dataframe(vendor_exc, use_container_width=True, hide_index=True)

st.divider()

st.markdown("### 📋 Audit Trail")
st.markdown("Every agent action is logged for compliance and reproducibility.")

trail_data = [
    {"TIMESTAMP": "2026-03-04 10:23:15", "ACTION": "QUERY_RECEIVED", "DETAIL": query, "USER": "auditor@ir.com"},
    {"TIMESTAMP": "2026-03-04 10:23:15", "ACTION": "SEMANTIC_TRANSLATE", "DETAIL": "NL → SQL via semantic model (deterministic)", "USER": "CORTEX_AGENT"},
    {"TIMESTAMP": "2026-03-04 10:23:16", "ACTION": "DATA_QUERY", "DETAIL": f"Queried {len(po_df)} POs across {po_df['ERP_SOURCE'].nunique()} ERPs", "USER": "CORTEX_ANALYST"},
    {"TIMESTAMP": "2026-03-04 10:23:17", "ACTION": "MATCH_EXECUTE", "DETAIL": f"Three-way match: {len(match_df[match_df['MATCH_STATUS']=='MATCHED'])} matched, {len(match_df[match_df['MATCH_STATUS']=='EXCEPTION'])} exceptions", "USER": "MATCH_TOOL"},
    {"TIMESTAMP": "2026-03-04 10:23:17", "ACTION": "RESULTS_RETURNED", "DETAIL": "Results displayed in dashboard", "USER": "CORTEX_AGENT"},
]

st.dataframe(pd.DataFrame(trail_data), use_container_width=True, hide_index=True)

st.divider()

st.markdown("### 📊 Match Overview")

overview_col1, overview_col2, overview_col3, overview_col4, overview_col5 = st.columns(5)
total = len(match_df)
matched = len(match_df[match_df["MATCH_STATUS"] == "MATCHED"])
exceptions = len(match_df[match_df["MATCH_STATUS"] == "EXCEPTION"])

overview_col1.metric("Total POs", total)
overview_col2.metric("Matched", matched, f"{matched/total*100:.0f}%")
overview_col3.metric("Exceptions", exceptions, f"{exceptions/total*100:.0f}%")
overview_col4.metric("ERP Sources", match_df["ERP_SOURCE"].nunique())
overview_col5.metric("Total Value", f"${match_df['PO_AMOUNT'].sum():,.0f}")

exc_by_type = match_df[match_df["MATCH_STATUS"] == "EXCEPTION"]["EXCEPTION_TYPE"].value_counts().reset_index()
exc_by_type.columns = ["Exception Type", "Count"]
st.bar_chart(exc_by_type, x="Exception Type", y="Count")
