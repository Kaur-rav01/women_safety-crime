import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler 

# Page configuration
st.set_page_config(
    page_title="WOMEN SAFETY INDIA | 2018",
    page_icon="🚨",
    layout="wide",
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        background-color: #f9f9f9;
    }
    h1 {
        color: #FF3E4D;
    }
    .stMetric {
        background-color: #f0f2f6;
        border-radius: 8px;
        padding: 0.5rem;
    }
    </style>
    """, unsafe_allow_html=True)

# Title and subtitle
st.title("🛡️ WOMEN SAFETY ANALYSIS IN INDIA (2018)")
st.markdown("🔍 **Explore crime statistics affecting women's safety across Indian states using real data.**")

# Load data
df = pd.read_csv("final_cleaned.csv")

# Compute safety score (lower cases per 1000 females → higher score)
scaler = MinMaxScaler()
df['Women_Safety_Score'] = 1 - scaler.fit_transform(df[['Cases_per_1000_Females']])

# Sidebar filters
st.sidebar.header("🔍 Filters")
state_options = df['State'].sort_values().unique()
selected_state = st.sidebar.selectbox("Select a state to view details", state_options)

# Raw data viewer
with st.expander("📂 Show Raw Data"):
    st.dataframe(df)

# Display selected state metrics
state_data = df[df["State"] == selected_state]
col1, col2, col3 = st.columns(3)
col1.metric("👮‍♀️ Total Crimes", int(state_data['Total_Cases']))
col2.metric("🧍 Total Victims", int(state_data['Total_Victims']))
score = float(state_data['Women_Safety_Score'])
color = "🟢" if score > 0.7 else "🟠" if score > 0.4 else "🔴"
col3.metric(f"{color} Safety Score (0 to 1)", round(score, 2))

st.markdown("---")

# Charts for Top 10 Safe & Risky States
col1, col2 = st.columns(2)

with col1:
    st.subheader("✅ Top 10 Safest States")
    safest = df.sort_values('Women_Safety_Score', ascending=False).head(10)
    fig1, ax1 = plt.subplots()
    sns.barplot(data=safest, x='Women_Safety_Score', y='State', palette='Greens', ax=ax1)
    ax1.set_xlabel("Safety Score")
    ax1.set_title("Safest States for Women")
    st.pyplot(fig1)

with col2:
    st.subheader("⚠️ Top 10 Riskiest States")
    riskiest = df.sort_values('Women_Safety_Score', ascending=True).head(10)
    fig2, ax2 = plt.subplots()
    sns.barplot(data=riskiest, x='Women_Safety_Score', y='State', palette='Reds_r', ax=ax2)
    ax2.set_xlabel("Safety Score")
    ax2.set_title("Riskiest States for Women")
    st.pyplot(fig2)

st.markdown("---")
st.markdown("📊 **Data Source:** [National Crime Records Bureau (2018)]()")
