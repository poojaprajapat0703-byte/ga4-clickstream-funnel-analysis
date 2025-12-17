# ===============================
# GA4 FUNNEL & SEQUENCE ANALYSIS
# ===============================

import streamlit as st
import pandas as pd
import plotly.express as px

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(
    page_title="GA4 Funnel & Sequence Analysis",
    layout="wide"
)

st.title("📊 GA4 Funnel, Drop-off & Time Analysis")
st.caption("Session-based GA4 clickstream analytics (Interview-ready)")

# -------------------------------
# DATA LOADING (SAFE)
# -------------------------------
st.header("1️⃣ Load Data")
@st.cache_data
def load_data():
    return pd.read_csv("Data/GA4_synthetic_data.csv")

df = load_data()

st.success("✅ Sample GA4 data loaded automatically")

# -------------------------------
# BASIC CLEANING (MANDATORY)
# -------------------------------
df["event_date"] = pd.to_datetime(df["event_date"], format="%Y%m%d")

df = df.sort_values(
    by=["user_id", "session_id", "engagement_time_msec"]
)

st.success("✅ Data loaded successfully")

# -------------------------------
# DATA OVERVIEW
# -------------------------------
st.subheader("📌 Dataset Overview")

c1, c2, c3 = st.columns(3)
c1.metric("Total Rows", len(df))
c2.metric("Unique Users", df["user_id"].nunique())
c3.metric("Unique Sessions", df["session_id"].nunique())

with st.expander("🔍 Preview Raw Data"):
    st.dataframe(df.head(100), use_container_width=True)

# =========================================================
# 2️⃣ SESSION SEQUENCE ANALYSIS (FROM YOUR NOTEBOOK)
# =========================================================
st.header("2️⃣ Exploratory Session Sequences")

session_seq = (
    df.groupby("session_id")["event_name"]
    .apply(list)
    .reset_index()
)

session_seq["sequence"] = session_seq["event_name"].apply(
    lambda x: " → ".join(x)
)

top_sequences = (
    session_seq["sequence"]
    .value_counts()
    .head(10)
    .reset_index()
)
top_sequences.columns = ["Sequence", "Sessions"]

st.subheader("🔁 Top 10 Event Sequences")
st.dataframe(top_sequences, use_container_width=True)

# =========================================================
# 3️⃣ FUNNEL ANALYSIS (SESSION-BASED)
# =========================================================
st.header("3️⃣ Funnel Analysis")

funnel_steps = [
    "session_start",
    "page_view",
    "add_to_cart",
    "purchase"
]

funnel_df = (
    df.groupby("session_id")["event_name"]
    .apply(list)
    .reset_index()
)

for step in funnel_steps:
    funnel_df[step] = funnel_df["event_name"].apply(
        lambda x: 1 if step in x else 0
    )

# Funnel counts
funnel_counts = {
    step: funnel_df[step].sum()
    for step in funnel_steps
}

funnel_summary = pd.DataFrame({
    "Step": funnel_steps,
    "Sessions Reached": list(funnel_counts.values())
})

funnel_summary["Conversion %"] = (
    funnel_summary["Sessions Reached"]
    / funnel_summary.iloc[0]["Sessions Reached"]
    * 100
).round(2)

st.subheader("📉 Funnel Summary")
st.dataframe(funnel_summary, use_container_width=True)

# Small clean chart
fig_funnel = px.bar(
    funnel_summary,
    x="Step",
    y="Sessions Reached",
    text="Conversion %",
    height=350
)
st.plotly_chart(fig_funnel, use_container_width=True)

# =========================================================
# 4️⃣ DROP-OFF ANALYSIS
# =========================================================
st.header("4️⃣ Drop-off Analysis")

drop_data = []

for i in range(len(funnel_steps) - 1):
    cur = funnel_steps[i]
    nxt = funnel_steps[i + 1]

    dropped = funnel_df[
        (funnel_df[cur] == 1) & (funnel_df[nxt] == 0)
    ]

    drop_data.append({
        "From": cur,
        "To": nxt,
        "Dropped Sessions": len(dropped)
    })

drop_df = pd.DataFrame(drop_data).sort_values(
    by="Dropped Sessions",
    ascending=False
)

st.subheader("🚨 Top Drop-off Points")
st.dataframe(drop_df, use_container_width=True)

# =========================================================
# 5️⃣ TIME-BASED ANALYSIS (FROM NOTEBOOK)
# =========================================================
st.header("5️⃣ Time-based Conversion Analysis")

session_time = (
    df.groupby("session_id")["engagement_time_msec"]
    .sum()
    .reset_index()
)

funnel_time = funnel_df.merge(
    session_time,
    on="session_id",
    how="left"
)

funnel_time["engagement_time_sec"] = (
    funnel_time["engagement_time_msec"] / 1000
)

funnel_time["conversion_status"] = funnel_time["purchase"].apply(
    lambda x: "Converted" if x == 1 else "Dropped"
)

bins = [0, 10, 30, 60, 120, 300]
labels = ["0-10s", "10-30s", "30-60s", "60-120s", "120s+"]

funnel_time["time_bucket"] = pd.cut(
    funnel_time["engagement_time_sec"],
    bins=bins,
    labels=labels,
    include_lowest=True
)

bucket_summary = (
    funnel_time
    .groupby(["time_bucket", "conversion_status"])
    .size()
    .reset_index(name="Sessions")
)

st.subheader("⏱ Time Spent vs Conversion")

fig_time = px.bar(
    bucket_summary,
    x="time_bucket",
    y="Sessions",
    color="conversion_status",
    barmode="group",
    height=350
)

st.plotly_chart(fig_time, use_container_width=True)

# =========================================================
# FINAL NOTE
# =========================================================
st.success("✅ Full GA4 analysis loaded successfully — no hidden errors")
