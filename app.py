import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page config
st.set_page_config(page_title="Student Performance Dashboard", layout="wide")

st.title("📊 Academic Intervention Dashboard for At-Risk Students")

# Load dataset
df = pd.read_csv("merged_dataset.csv")

# ---------------------------
# BASIC METRICS
# ---------------------------
st.subheader("📌 Overall Student Statistics")

col1, col2, col3 = st.columns(3)
col1.metric("Total Students", len(df))
col2.metric("Average Exam Score", round(df['ExamScore'].mean(), 2))
col3.metric("Average Attendance", round(df['Attendance'].mean(), 2))

# ---------------------------
# PERFORMANCE CATEGORIES
# ---------------------------
df['PerformanceCategory'] = pd.cut(
    df['ExamScore'],
    bins=[0, 50, 75, 100],
    labels=['Struggling', 'Average', 'Top']
)

st.subheader("📈 Student Performance Distribution")

col1, col2 = st.columns(2)

with col1:
    fig1, ax1 = plt.subplots(figsize=(4, 3))
    df['PerformanceCategory'].value_counts().plot(kind='bar', ax=ax1)
    ax1.set_title("Performance Distribution")
    ax1.set_xlabel("")
    ax1.set_ylabel("Students")
    st.pyplot(fig1)


# ---------------------------
# ATTENDANCE IMPACT
# ---------------------------
st.subheader("📉 Attendance Impact on Exam Score")

with col2:
    fig2, ax2 = plt.subplots(figsize=(4, 3))
    sns.scatterplot(
        x='Attendance',
        y='ExamScore',
        hue='PerformanceCategory',
        data=df,
        ax=ax2,
        legend=False
    )
    ax2.set_title("Attendance vs Score")
    st.pyplot(fig2)



# ---------------------------
# CORRELATION HEATMAP
# ---------------------------
st.subheader("🔥 Correlation Heatmap")


fig3, ax3 = plt.subplots(figsize=(6, 4))
sns.heatmap(
    df.corr(numeric_only=True),
    cmap='coolwarm',
    ax=ax3
)
st.pyplot(fig3)



# ---------------------------
# AT-RISK STUDENTS
# ---------------------------
st.subheader("⚠️ At-Risk Students (Low Attendance & Low Score)")

at_risk = df[
    (df['Attendance'] < 75) |
    (df['ExamScore'] < 60)
]

st.write(f"Total At-Risk Students: {len(at_risk)}")
st.dataframe(at_risk)

# ---------------------------
# INTERVENTION INSIGHTS
# ---------------------------
st.subheader("🎯 Suggested Academic Interventions")

st.markdown("""
- 📌 Increase **attendance monitoring**
- 📌 Provide **extra tutoring** for struggling students
- 📌 Reduce **stress levels**
- 📌 Encourage **assignment completion**
- 📌 Offer **online learning resources**
""")

st.success("Dashboard ready for academic decision-making 🚀")
