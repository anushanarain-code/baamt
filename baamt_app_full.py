import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from fpdf import FPDF
import textwrap

st.set_page_config(page_title="BAAMT - Behavioural Advocacy and Messaging Tool", layout="wide")

st.title("🧠 BAAMT")
st.subheader("Behavioural Advocacy and Messaging Tool")
st.markdown("""
BAAMT helps advocacy organizations design messaging strategies based on the moral values of their target audience. 
Complete the assessment below to generate a behavioural profile and recommended messaging strategy.
""")

# ---------- Audience Context ----------
st.header("Audience Information")
st.markdown("**Please select the target audience, geography, and campaign type.**")

audience = st.selectbox("Select Target Audience", ["General Public", "Policy Makers", "Youth", "Professionals"])
geography = st.selectbox("Select Geography", ["India", "Global", "Europe", "USA"])
stakeholder = st.selectbox("Select Stakeholder Group", ["General Public", "Community Leaders", "Organizations"])
campaign = st.selectbox("Select Campaign Type", ["Behaviour Change", "Policy Advocacy", "Education & Awareness"])

st.divider()

# ---------- Behavioural Assessment ----------
st.header("Behavioural Assessment")
st.markdown("""
Rate the following statements from 1 (Strongly Disagree) to 5 (Strongly Agree). 
These questions are based on **Moral Foundations Theory**, which suggests that people's ethical and moral judgments are shaped by universal domains such as care/harm, fairness, authority, loyalty, and purity.
""")

# Example questions
questions = {
    "Care/Harm": "Preventing suffering should be a top priority in public policy.",
    "Fairness": "Fair treatment matters even if it requires economic trade-offs.",
    "Authority": "Society functions best when people respect authority and institutions.",
    "Loyalty": "Loyalty to one's community should guide political decision-making.",
    "Purity": "Purity and moral cleanliness are important social values."
}

responses = {}
for key, q in questions.items():
    responses[key] = st.slider(q, 1, 5, 3)

st.divider()

# ---------- Compute Scores ----------
# Simple average per foundation
scores = {k: v for k, v in responses.items()}

# Generate radar chart
labels = list(scores.keys())
values = list(scores.values())
values += values[:1]  # close the circle

angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(6,6), subplot_kw=dict(polar=True))
ax.plot(angles, values, color="blue", linewidth=2, marker='o')
ax.fill(angles, values, color="skyblue", alpha=0.25)
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels)
ax.set_yticks([1,2,3,4,5])
ax.set_yticklabels(["1","2","3","4","5"])
ax.grid(True)
st.pyplot(fig)

st.divider()

# ---------- Generate Results ----------
st.header("Audience Moral Profile")
for key, val in scores.items():
    st.write(f"**{key}:** {val}")

# Behavioural Segment (longer, reader-friendly)
segment = ("Mixed moral audiences whose responses depend on contextual framing and coalition-based messaging. "
           "For example, some individuals prioritize harm reduction while others focus on tradition or authority. "
           "Understanding these differences helps in designing effective messaging campaigns.")

st.subheader("Behavioural Segment")
st.write(segment)

# Reform Orientation
reform = ("This audience may be receptive to transformative or constructive advocacy narratives that highlight social change, fairness, and protection of vulnerable groups. "
          "Messaging should include practical examples, societal benefits, and clear steps for positive action.")

st.subheader("Reform Orientation")
st.write(reform)

# Risk Profile
risk = ("Moderate sensitivity to moral and social risk. Advocacy messages can focus on evidence, illustrative stories, and harm reduction techniques without triggering resistance. "
        "Examples include explaining the benefits of a policy through concrete scenarios or case studies.")

st.subheader("Risk Sensitivity Profile")
st.write(risk)

# Institutional Trust
trust = ("Trust levels toward institutions vary. Messaging may need to emphasize transparency, reliability, and track records of organizations or policies. "
         "Highlight real-world successes to strengthen credibility.")

st.subheader("Institutional Trust Orientation")
st.write(trust)

# Advocacy Lever
lever = ("Primary advocacy approaches could include public campaigns, coalition building, and sharing evidence with community leaders. "
         "Practical examples include organizing community meetings, targeted social media campaigns, or policy briefings.")

st.subheader("Primary Advocacy Lever")
st.write(lever)

# Campaign Strategy
strategy = ("A comprehensive campaign plan should integrate messaging, coalition support, and iterative feedback mechanisms to ensure engagement across diverse moral audiences. "
            "It should be adaptable to local culture and legal frameworks, highlighting tangible benefits.")

st.subheader("Campaign Strategy Plan")
st.write(strategy)

# Full Advocacy Strategy
brief = ("The advocacy strategy combines moral framing, evidence-based messages, and actionable steps for influencing the target audience. "
         "Include clear examples, recommended channels, and potential risks. "
         "For instance, a campaign to reduce harm could include both storytelling and quantitative evidence to persuade multiple audience segments.")

st.subheader("Full Advocacy Strategy Brief")
st.write(brief)

st.divider()

# ---------- PDF Generation ----------
def generate_pdf():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    def add_section(title, text):
        pdf.set_font("Arial", "B", 12)
        pdf.cell(0, 7, title, ln=True)
        pdf.set_font("Arial", "", 11)
        wrapped = textwrap.wrap(text, 90)
        for line in wrapped:
            pdf.multi_cell(0, 6, line)  # safely wrap long text
        pdf.ln(2)

    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "BAAMT Advocacy Strategy Report", ln=True)
    pdf.ln(4)

    pdf.set_font("Arial", "", 11)
    pdf.multi_cell(0,6, f"Audience: {audience}")
    pdf.multi_cell(0,6, f"Geography: {geography}")
    pdf.multi_cell(0,6, f"Stakeholder: {stakeholder}")
    pdf.multi_cell(0,6, f"Campaign Objective: {campaign}")

    add_section("Behavioural Segment", segment)
    add_section("Reform Orientation", reform)
    add_section("Risk Sensitivity Profile", risk)
    add_section("Institutional Trust Orientation", trust)
    add_section("Primary Advocacy Lever", lever)
    add_section("Campaign Strategy Plan", strategy)
    add_section("Full Advocacy Strategy Brief", brief)

    return pdf.output(dest="S").encode("latin-1")  # stable encoding

if st.button("Download BAAMT Report (PDF)"):
    pdf_bytes = generate_pdf()
    st.download_button(
        label="Download PDF Report",
        data=pdf_bytes,
        file_name="BAAMT_Report.pdf",
        mime="application/pdf"
    )
