import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import textwrap
from fpdf import FPDF
import io

# ----------------- APP CONFIG -----------------
st.set_page_config(
    page_title="BAAMT - Behavioural Advocacy & Messaging Tool",
    layout="wide"
)

# ----------------- APP HEADER -----------------
st.title("🧠 BAAMT")
st.markdown("""
**Behavioural Advocacy and Messaging Tool**  
BAAMT helps advocacy organizations design messaging strategies based on the moral values of their target audience.
""")

# ----------------- INSTRUCTIONS -----------------
st.markdown("""
### Instructions
Complete the assessment below carefully. Rate each statement on a scale from 1 (Strongly Disagree) to 5 (Strongly Agree).  
Your responses will generate a **Behavioural Profile**, recommended **Messaging Strategies**, and a detailed **Advocacy Report** tailored to your audience.
""")

# ----------------- AUDIENCE CONTEXT -----------------
st.subheader("Audience Context")
audience = st.selectbox("Select Target Audience", ["General Public", "Policymakers", "Stakeholders"])
geography = st.selectbox("Select Geography", ["India", "Global", "Other"])
stakeholder = st.selectbox("Select Stakeholder Type", ["None", "NGO", "Government", "Media"])
campaign = st.selectbox("Select Campaign Type", ["Behaviour Change", "Policy Advocacy", "Awareness"])

# ----------------- BEHAVIOURAL ASSESSMENT -----------------
st.subheader("Behavioural Assessment")
st.markdown("""
Rate the following statements from 1 (Strongly Disagree) to 5 (Strongly Agree).  
These questions are based on **Moral Foundations Theory**, which suggests people’s moral reasoning is shaped by care, fairness, loyalty, authority, and purity values. Your answers will help us suggest effective advocacy framing.
""")

questions = [
    "Preventing suffering should be a top priority in public policy.",
    "Fair treatment matters even if it requires economic trade-offs.",
    "Society functions best when people respect authority and institutions.",
    "Loyalty to one's community should guide political decision-making.",
    "Purity and moral cleanliness are important social values.",
    "Avoiding harm to vulnerable beings is an ethical responsibility.",
    "Rules and laws should be followed even when inconvenient.",
    "People should prioritize fairness in markets and economic systems.",
    "Communities should protect their cultural traditions.",
    "Certain practices are morally wrong regardless of consequences."
]

responses = []
for q in questions:
    responses.append(st.slider(q, min_value=1, max_value=5, value=3))

# ----------------- CALCULATIONS -----------------
care = (responses[0] + responses[5]) / 2
fairness = (responses[1] + responses[7]) / 2
authority = (responses[2] + responses[6]) / 2
loyalty = (responses[3] + responses[8]) / 2
purity = (responses[4] + responses[9]) / 2

# Behavioural segment
segment = "Mixed moral audiences whose responses are likely to depend on contextual framing and coalition-based messaging. For instance, some individuals may prioritize harm reduction while others focus on tradition or authority."

# Reform orientation
reform = "This audience may be receptive to transformative or constructive advocacy narratives that highlight social change, fairness, and protection of vulnerable groups. Messaging should include practical examples of improvements and societal benefits."

# Risk sensitivity
risk = "Moderate sensitivity to moral and social risk. Advocacy can focus on evidence-based messages, illustrative stories, and harm reduction without triggering resistance."

# Trust orientation
trust = "Trust levels toward institutions vary. Messaging may need to emphasize transparency, reliability, and track records of organizations or policies."

# Advocacy lever
lever = "Primary advocacy approaches could include public campaigns, coalition building, and evidence-sharing with community leaders."

# Geographic messaging
geo = "Messaging should consider local culture, traditions, and legal frameworks, highlighting context-specific benefits and examples."

# Campaign strategy
strategy = "A comprehensive campaign plan should integrate messaging, coalition support, and iterative feedback mechanisms to ensure engagement across diverse moral audiences."

# Full advocacy brief
brief = "The advocacy strategy combines moral framing, evidence-based messages, and actionable steps for influencing the target audience. Include clear examples, recommended channels, and potential risks."

# Message framing examples
framing = "Example frames: highlighting care and harm reduction, demonstrating fairness and equity, appealing to loyalty with community-based examples, emphasizing respect for authorities, and invoking purity as ethical conduct."

# Coalition strategy
coalition = "Engage local NGOs, policy influencers, and media partners to strengthen message credibility and amplify outreach."

# Policy pathway
policy = "Recommend stepwise policy measures, including pilot projects, evaluations, and evidence dissemination."

# Opposition risk analysis
risk_analysis = "Assess potential objections from stakeholders and plan preemptive clarifications, data, and coalition responses."

# ----------------- RADAR CHART -----------------
st.subheader("Audience Moral Profile")
labels = np.array(["Care", "Fairness", "Authority", "Loyalty", "Purity"])
stats = np.array([care, fairness, authority, loyalty, purity])

angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
stats = np.concatenate((stats, [stats[0]]))
angles += angles[:1]

fig, ax = plt.subplots(figsize=(5,5), subplot_kw=dict(polar=True))
ax.plot(angles, stats, color='red', linewidth=2, linestyle='solid')
ax.fill(angles, stats, color='red', alpha=0.25)
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels)
ax.set_yticks([1,2,3,4,5])
ax.set_ylim(1,5)
st.pyplot(fig)

# ----------------- PDF GENERATION -----------------
def generate_pdf():
    pdf = FPDF()
    pdf.add_page()

    # Use a Unicode-safe font
    try:
        pdf.add_font("DejaVu", "", "DejaVuSans.ttf", uni=True)
        pdf.set_font("DejaVu", "", 11)
    except:
        pdf.set_font("Arial", "", 11)

    pdf.set_font("DejaVu", "B", 16)
    pdf.cell(0, 10, "BAAMT Advocacy Strategy Report", ln=True)
    pdf.ln(5)

    pdf.set_font("DejaVu", "", 11)
    pdf.cell(0, 8, f"Audience: {audience}", ln=True)
    pdf.cell(0, 8, f"Geography: {geography}", ln=True)
    pdf.cell(0, 8, f"Stakeholder: {stakeholder}", ln=True)
    pdf.cell(0, 8, f"Campaign Objective: {campaign}", ln=True)
    pdf.ln(5)

    def add_section(title, text):
        pdf.set_font("DejaVu", "B", 12)
        pdf.cell(0, 7, title, ln=True)
        pdf.set_font("DejaVu", "", 11)
        wrapped = textwrap.wrap(text, 90)
        for line in wrapped:
            line = line.replace("\u200b","")  # remove zero-width spaces
            pdf.multi_cell(0, 7, line)

    add_section("Behavioural Segment", segment)
    add_section("Reform Orientation", reform)
    add_section("Risk Sensitivity Profile", risk)
    add_section("Institutional Trust Orientation", trust)
    add_section("Primary Advocacy Lever", lever)
    add_section("Geographic Messaging Adjustment", geo)
    add_section("Campaign Strategy Plan", strategy)
    add_section("Advocacy Strategy Brief", brief)
    add_section("Message Framing Examples", framing)
    add_section("Coalition Strategy", coalition)
    add_section("Policy Pathway", policy)
    add_section("Opposition Risk Analysis", risk_analysis)

    # Save PDF to bytes
    pdf_bytes = pdf.output(dest="S").encode("latin-1", "replace")
    return pdf_bytes

# ----------------- GENERATE & DOWNLOAD -----------------
if st.button("Generate BAAMT Strategy Report"):
    st.subheader("Generated Report")
    st.write(segment)
    st.write(reform)
    st.write(risk)
    st.write(trust)
    st.write(lever)
    st.write(geo)
    st.write(strategy)
    st.write(brief)

    pdf_bytes = generate_pdf()
    st.download_button(
        label="Download BAAMT Report (PDF)",
        data=pdf_bytes,
        file_name="BAAMT_report.pdf",
        mime="application/pdf"
    )

    st.markdown("""
    You can also share this report via email by attaching the downloaded PDF.
    """)
