import streamlit as st

st.set_page_config(page_title="PharmaSage AI", layout="wide")

st.title("PharmaSage AI")
st.caption("Agentic AI–powered Drug Repurposing Intelligence Platform")

# Sidebar – User Input
st.sidebar.header("Research Input")
molecule = st.sidebar.text_input("Molecule Name", "Metformin")
objective = st.sidebar.text_area(
    "Research Objective",
    "Identify new therapeutic indications"
)

if st.sidebar.button("Run Analysis"):
    st.success("Agentic AI analysis started...")

# Main Dashboard
st.subheader("Agent Execution Status")
col1, col2, col3, col4 = st.columns(4)

col1.metric("Literature Agent", "Completed")
col2.metric("Clinical Agent", "Completed")
col3.metric("Patent Agent", "Running")
col4.metric("Market Agent", "Queued")

st.subheader("Ranked Repurposing Opportunities")
st.table({
    "Indication": ["Oncology", "Autoimmune Disorders", "Neurology"],
    "Evidence Score": [0.89, 0.76, 0.64],
    "Risk Level": ["Medium", "Low", "Medium"]
})

st.subheader("Report Output")
st.button("Download AI-Generated Report")
import matplotlib.pyplot as plt

st.subheader("Evidence Score Comparison (Sample Visualization)")

indications = ["Oncology", "Autoimmune", "Neurology"]
scores = [0.89, 0.76, 0.64]

fig, ax = plt.subplots()
ax.bar(indications, scores)
ax.set_xlabel("Therapeutic Indication")
ax.set_ylabel("Evidence Score")
ax.set_ylim(0, 1)

st.pyplot(fig)
st.subheader("Evidence Contribution by Domain (Sample)")

labels = ["Literature", "Clinical Trials", "Patents", "Market"]
sizes = [40, 30, 20, 10]

fig2, ax2 = plt.subplots()
ax2.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90)
ax2.axis("equal")

st.pyplot(fig2)
